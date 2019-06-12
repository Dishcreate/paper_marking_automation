import pyodbc
import pandas.io.sql
import configparser
import logging
from tkinter import messagebox


class Db:

    def __init__(self, config=configparser.ConfigParser()):
        self.log = logging
        config.sections()
        config.read('CONF.INI')
        self.driver = config['DEFAULT']['driver']
        self.server = config['DEFAULT']['server']
        self.database = config['DEFAULT']['database']
        self.host = config['DEFAULT']['host']
        self.port = config['DEFAULT']['port']
        self.user = config['DEFAULT']['user']
        self.password = config['DEFAULT']['password']
        self.yes = 'yes'

    def connection(self):
        try:
            return pyodbc.connect('Driver={%s};Server=%s;Database=%s;UID=%s;PWD=%s' % (self.driver, self.server,
                                                                                       self.database, self.user,
                                                                                       self.password))
        except pyodbc.Error as ex:
            sqlstate = ex.args[1]+'@connection()'
            messagebox.showerror("Error", sqlstate)

    def details_of_question(self, paper_id):
        query = """
        SELECT PA.id,SE.Id,QS.Id,QQ.Id AS QuestionId,QQ.Number1,QQ.CorrectAnswers, QT.Id,QM.Id,QSS.Id,QSS.Marks
        FROM [Transaction].[Paper] AS PA
        INNER JOIN [Transaction].[Section] AS SE ON PA.Id = SE.PaperId
        INNER JOIN [Transaction].[QuestionSet] AS QS ON SE.Id = QS.SectionId
        INNER JOIN [Transaction].[Question] AS QQ ON QS.Id = QQ.QuestionSetId
        INNER JOIN [Transaction].[QuestionTopic] AS QT ON QQ.Id = QT.QuestionId
        INNER JOIN [Transaction].[QuestionMainSkill] AS QM ON QT.Id = QM.QuestionTopicId
        INNER JOIN [Transaction].[QuestionSubSkill] AS QSS ON QSS.QuestionMainSkillId = QM.Id
        WHERE PA.Id = ? and SE.QuestionMainType = 1
        """
        # logging.basicConfig(filename='systemlog/error.log', level=logging.ERROR)
        try:
            return pandas.io.sql.read_sql(query, self.connection(), params=[paper_id])
        except pyodbc.Error as ex:
            sql = ex.args[0]
            # self.log.error(sql)
            messagebox.showerror("Error", sql)

    def details_of_marks(self, paper_id):
        query = """
        SELECT PA.id,SE.Id,QS.Id,QQ.Id AS QuestionId,QQ.Number1,SUM(QSS.Marks) AS TotalAllocatedMarks
          FROM  [Transaction].[Paper] as PA
          INNER JOIN [Transaction].[Section] as SE ON PA.Id = SE.PaperId
          INNER JOIN [Transaction].[QuestionSet] as QS ON SE.Id = QS.SectionId
          INNER JOIN [Transaction].[Question] as QQ ON QS.Id = QQ.QuestionSetId
          INNER JOIN [Transaction].[QuestionTopic] as QT ON QQ.Id = QT.QuestionId
          INNER JOIN [Transaction].[QuestionMainSkill] as QM ON QT.Id = QM.QuestionTopicId
          INNER JOIN [Transaction].[QuestionSubSkill] as QSS ON QSS.QuestionMainSkillId = QM.Id
          WHERE PA.Id = ? and SE.QuestionMainType = 1
          GROUP BY PA.id,SE.Id,QS.Id,QQ.Id,QQ.Number1
          """
        # logging.basicConfig(filename='systemlog/error.log', level=logging.ERROR)
        try:
            return pandas.io.sql.read_sql(query, self.connection(), params=[paper_id])
        except pyodbc.Error as ex:
            sql = ex.args[0]
            # self.log.error(sql)
            messagebox.showerror("Error", sql)

    def details_of_mark_individual(self, paper_id):
        query = """
        SELECT  QT.QuestionId , QM.QuestionTopicId , QSS.QuestionMainSkillId , QSS.id AS QuestionSubSkillId , QSS.Marks AS GainedMarks
          FROM  [Transaction].[Paper] as PA
          INNER JOIN [Transaction].[Section] as SE ON PA.Id = SE.PaperId
          INNER JOIN [Transaction].[QuestionSet] as QS ON SE.Id = QS.SectionId
          INNER JOIN [Transaction].[Question] as QQ ON QS.Id = QQ.QuestionSetId
          INNER JOIN [Transaction].[QuestionTopic] as QT ON QQ.Id = QT.QuestionId
          INNER JOIN [Transaction].[QuestionMainSkill] as QM ON QT.Id = QM.QuestionTopicId
          INNER JOIN [Transaction].[QuestionSubSkill] as QSS ON QSS.QuestionMainSkillId = QM.Id
          WHERE PA.Id = ? and SE.QuestionMainType = 1
          """
        # logging.basicConfig(filename='systemlog/error.log', level=logging.ERROR)
        try:
            return pandas.io.sql.read_sql(query, self.connection(), params=[paper_id])
        except pyodbc.Error as ex:
            sql = ex.args[0]
            # self.log.error(sql)
            messagebox.showerror("Error", sql)

    def empty_paper(self, paper_id, student_id):
        query = """
        SELECT * FROM [Transaction].[StudentPaperResult]
        WHERE PaperId = ? AND StudentId = ?
        """
        # logging.basicConfig(filename='systemlog/error.log', level=logging.ERROR)
        try:
            return pandas.io.sql.read_sql(query, self.connection(), params=(int(paper_id), student_id)).empty
        except pyodbc.Error as ex:
            sql = ex.args[0]
            # self.log.error(sql)
            messagebox.showerror("Error", sql)

    def empty_question_result(self, paper_id, student_id, start, end):
        # questions = self.details_of_question(paper_id)
        # start = questions["QuestionId"].iloc[0]
        # end = questions["QuestionId"].iloc[-1]
        query = """
            SELECT * FROM [Transaction].[StudentQuestionResult] WHERE QuestionId BETWEEN ? AND ? AND StudentId = ?
        """
        # logging.basicConfig(filename='systemlog/error.log', level=logging.ERROR)
        try:
            return pandas.io.sql.read_sql(query, self.connection(), params=(int(start), int(end), student_id)).empty
        except pyodbc.Error as ex:
            sql = ex.args[0]
            # self.log.error(sql)
            messagebox.showerror("Error", sql)

    def empty_question_result_break(self, paper_id, student_id, start, end):
        # questions = self.details_of_question(paper_id)
        # start = questions["QuestionId"].iloc[0]
        # end = questions["QuestionId"].iloc[-1]
        query ="""
          SELECT * FROM [Transaction].[StudentQuestionResultBreakdown] WHERE QuestionId BETWEEN ? AND ? AND StudentId = ?
        """
        try:
            return pandas.io.sql.read_sql(query, self.connection(), params=(int(start), int(end), student_id)).empty
        except pyodbc.Error as ex:
            sql = ex.args[0]
            # self.log.error(sql)
            messagebox.showerror("Error", sql)

    def update_result(self, paper_id, student_id, start, end):
        # correct_answer = self.details_of_marks(paper_id)
        # start = correct_answer["QuestionId"].iloc[0]
        # end = correct_answer["QuestionId"].iloc[-1]
        query_result ="""
            SELECT * FROM [Transaction].[StudentQuestionResult] WHERE QuestionId BETWEEN ? AND ? AND StudentId = ?
        """
        # logging.basicConfig(filename='systemlog/error.log', level=logging.ERROR)
        try:
            result = pandas.io.sql.read_sql(query_result, self.connection(), params=(int(start),int(end),student_id))
            return result
        except pyodbc.Error as ex:
            sql = ex.args[0]
            # self.log.error(sql)
            messagebox.showerror("Error", sql)

    def delete_result(self, student_id, question_id):
        query1 = """
                    DELETE FROM [Transaction].[StudentQuestionResultBreakdown] WHERE StudentId = ? AND QuestionId = ?  
                """
        query2 = """
                    DELETE FROM [Transaction].[StudentQuestionResult] WHERE StudentId = ? AND QuestionId = ?  
                """
        try:
            cursor = self.connection()
            cursor = cursor.cursor()
            cursor.execute(query1, [student_id, int(question_id)])
            cursor.execute(query2, [student_id, int(question_id)])
            cursor.commit()
            cursor.close()

        except pyodbc.Error as er:
            print(er)
            sql = er.args[0]
            self.log.error(sql)
            # messagebox.showerror("Error", sql)

    def update_question_result(self, student_id, question_id, gain, creat_on, update_on, answer, is_correct):
        query = """
            UPDATE [Transaction].[StudentQuestionResult] SET GainedMarks = ?, CreatedOn = ?, UpdatedOn = ?, Answers = ?, IsCorrect = ? 
            WHERE StudentId = ? AND QuestionId = ?
        """
        # logging.basicConfig(filename='systemlog/info.log', level=logging.INFO)
        try:
            cursor = self.connection()
            cursor = cursor.cursor()
            cursor.execute(query, [gain, creat_on, update_on, str(answer), is_correct, student_id,  int(question_id)])
            cursor.commit()
            cursor.close()
            # self.log.info('{0} row updated successfully.'.format(cursor.rowcount))

        except pyodbc.Error as ex:
            sql = ex.args[0]
            self.log.error(sql)
            messagebox.showerror("Error", sql)

    def update_question_result_breakdown(self, student_id, question_id, gain, creat_on, update_on):
        query = """
                    UPDATE [Transaction].[StudentQuestionResultBreakdown] SET GainedMarks = ?, CreatedOn = ?, UpdatedOn = ?
                    WHERE StudentId = ? AND QuestionId = ?
        """
        # logging.basicConfig(filename='systemlog/info.log', level=logging.INFO)
        try:
            cursor = self.connection()
            cursor = cursor.cursor()
            cursor.execute(query, [gain, creat_on, update_on, student_id, int(question_id)])
            cursor.commit()
            cursor.close()
            # self.log.info('{0} row updated successfully.'.format(cursor.rowcount))

        except pyodbc.Error as ex:
            sql = ex.args[0]
            # self.log.error(sql)
            messagebox.showerror("Error", sql)

    def insert_paper_data(self, student_id, paper_id, marking_sheet, is_absent, is_validReason ,created_on ,created_byid ,updated_on ,udated_byid):
        query = """
            INSERT INTO [Transaction].[StudentPaperResult] 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        try:
            cursor = self.connection()
            cursor = cursor.cursor()
            # question_id = int(question_id)
            cursor.execute(query, (student_id, int(paper_id), marking_sheet, is_absent, is_validReason ,created_on ,int(created_byid) ,updated_on ,int(udated_byid)))
            cursor.commit()
            cursor.close()

        except pyodbc.Error as ex:
            sql = ex.args[0]
            # self.log.error(sql)
            # print(sql)
            messagebox.showerror("Error", sql)

    def insert_question_result(self, student_id, question_id, gain, creat_on, creat_byid, update_on, update_byid, answer, is_correct,question_maintype):
        query = """
            INSERT INTO [Transaction].[StudentQuestionResult] 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        # cursor.execute("INSERT INTO table VALUES (%s, %s, %s)", (var1, var2, var3))
        try:
            # logging.basicConfig(filename='systemlog/info.log', level=logging.INFO)
            cursor = self.connection()
            cursor = cursor.cursor()
            # question_id = int(question_id)
            cursor.execute(query, (student_id, int(question_id), int(gain), creat_on, int(creat_byid), update_on, int(update_byid), answer, is_correct, int(question_maintype)))
            cursor.commit()
            cursor.close()
        except pyodbc.Error as ex:
            sql = ex.args[0]
            self.log.error(sql)
            # print(sql)
            messagebox.showerror("Error", sql)

    def insert_question_result_breakdown(self, student_id, question_id, question_topicid, question_mainskillid, question_sunskillid, gain, create_on, create_byid, update_on, update_byid):
        query = """
            INSERT INTO [Transaction].[StudentQuestionResultBreakdown] 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        # cursor.execute("INSERT INTO table VALUES (%s, %s, %s)", (var1, var2, var3))
        try:
            # logging.basicConfig(filename='systemlog/info.log', level=logging.INFO)
            cursor = self.connection()
            cursor = cursor.cursor()
            # question_id = int(question_id)
            cursor.execute(query, (student_id, int(question_id), int(question_topicid), int(question_mainskillid), int(question_sunskillid), int(gain), create_on, int(create_byid), update_on, int(update_byid)))
            cursor.commit()
            cursor.close()

        except pyodbc.Error as ex:
            sql = ex.args[0]
            # self.log.error(sql)
            # print(sql)
            messagebox.showerror("Error", sql)








