from oeq_db import Db
import configparser
from oeq_data import DataHandle
import logging
import pyodbc


class DataWrite:

    def __init__(self, db_obt=Db(), config=configparser.ConfigParser(), dh=DataHandle()):
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
        self.db = db_obt
        self.data = dh

    def engine_con(self):
        # engine = create_engine(
        #     'mssql+pyodbc://sa:209700@localhost:1433/iStarNanChiauDB?driver=SQL+Server+Native+Client+11.0')
        # return engine
        # mssql+pyodbc://sa:209700@localhost:1433/iStarNanChiauDB?driver=SQL+Server+Native+Client+11.0
        con = 'mssql+pyodbc://'+self.user+':'+self.password+'@'+self.host+':'+self.port+'/'+self.database+'?'\
              +'driver=SQL+Server+Native+Client+11.0'
        try:
            return pyodbc.connect('Driver={%s};Server=%s;Database=%s;UID=%s;PWD=%s' % (self.driver, self.server, self.database, self.user, self.password))
        except pyodbc.Error as ex:
            sql_exc = ex.args[1]
            self.log.error(sql_exc)

    def range(self, n):
        a = 1 + 40 * (n - 1)
        b = a + 40 - 1
        return a, b

    def insert_or_update(self, s_id, p_id, lst, scan_data):
        df_mark = self.db.details_of_marks(p_id)
        df_mark = df_mark.sort_values('Number1')
        paper_itr = int(str(lst).split('/')[-1][0:1])
        a, b = self.range(int(paper_itr))
        df_mark = df_mark.iloc[a-1:]
        question_id = df_mark[['QuestionId', 'Number1']]
        start = df_mark[['QuestionId']].iloc[0]
        end = df_mark[['QuestionId']].iloc[-1]
        paper_emty = self.db.empty_paper(p_id, s_id)
        result_empty = self.db.empty_question_result(p_id, s_id, start, end)
        result_empty_break = self.db.empty_question_result_break(p_id, s_id, start, end)

        if paper_emty and result_empty and result_empty_break:
            for _, row in self.data.paper(s_id, p_id).iterrows():
                s_id = row['StudentId']
                p_id = row['PaperId']
                marking_sheet = row['MarkingSheet']
                is_absent = row['IsAbsent']
                is_validReason = row['IsValidReason']
                created_on = row['CreatedOn']
                created_byid = row['CreatedById']
                updated_on = row['UpdatedOn']
                udated_byid = row['UpdatedById']
                self.db.insert_paper_data(s_id, p_id, marking_sheet, is_absent, is_validReason, created_on,
                                          created_byid, updated_on, udated_byid)

            for _, row in self.data.paper_marks_and_result(s_id, p_id, lst, scan_data).iterrows():
                s_id = row['StudentId']
                question_id = row['QuestionId']
                gain = row['GainedMarks']
                creat_on = row['CreatedOn']
                creat_byid = row['CreatedById']
                update_on = row['UpdatedOn']
                update_byid = row['UpdatedById']
                answer = row['Answers']
                is_correct = row['IsCorrect']
                question_maintype = row['QuestionMainType']
                self.db.insert_question_result(s_id, question_id, gain, creat_on, creat_byid, update_on,
                                               update_byid, answer, is_correct, question_maintype)

            for _, row in self.data.paper_mark_result_individual(s_id, p_id, lst, scan_data).iterrows():
                s_id = row['StudentId']
                question_id = row['QuestionId']
                question_topicid = row['QuestionTopicId']
                question_mainskillid = row['QuestionMainSkillId']
                question_sunskillid = row['QuestionSubSkillId']
                gain = row['GainedMarks']
                create_on = row['CreatedOn']
                create_byid = row['CreatedById']
                update_on = row['UpdatedOn']
                update_byid = row['UpdatedById']
                self.db.insert_question_result_breakdown(s_id, question_id, question_topicid,
                                                         question_mainskillid, question_sunskillid, gain, create_on,
                                                         create_byid, update_on, update_byid)

        if not paper_emty and result_empty and result_empty_break:
            for _, row in self.data.paper_marks_and_result(s_id, p_id, lst, scan_data).iterrows():
                s_id = row['StudentId']
                question_id = row['QuestionId']
                gain = row['GainedMarks']
                creat_on = row['CreatedOn']
                creat_byid = row['CreatedById']
                update_on = row['UpdatedOn']
                update_byid = row['UpdatedById']
                answer = row['Answers']
                is_correct = row['IsCorrect']
                question_maintype = row['QuestionMainType']
                self.db.insert_question_result(s_id, question_id, gain, creat_on, creat_byid, update_on,
                                               update_byid, answer, is_correct, question_maintype)

            for _, row in self.data.paper_mark_result_individual(s_id, p_id, lst, scan_data).iterrows():
                s_id = row['StudentId']
                question_id = row['QuestionId']
                question_topicid = row['QuestionTopicId']
                question_mainskillid = row['QuestionMainSkillId']
                question_sunskillid = row['QuestionSubSkillId']
                gain = row['GainedMarks']
                create_on = row['CreatedOn']
                create_byid = row['CreatedById']
                update_on = row['UpdatedOn']
                update_byid = row['UpdatedById']
                self.db.insert_question_result_breakdown(s_id, question_id, question_topicid,
                                                         question_mainskillid, question_sunskillid, gain, create_on,
                                                         create_byid, update_on, update_byid)

        if not paper_emty and not result_empty and result_empty_break:
            for _, row in self.data.paper_mark_result_individual(s_id, p_id, lst, scan_data).iterrows():
                s_id = row['StudentId']
                question_id = row['QuestionId']
                question_topicid = row['QuestionTopicId']
                question_mainskillid = row['QuestionMainSkillId']
                question_sunskillid = row['QuestionSubSkillId']
                gain = row['GainedMarks']
                create_on = row['CreatedOn']
                create_byid = row['CreatedById']
                update_on = row['UpdatedOn']
                update_byid = row['UpdatedById']
                self.db.insert_question_result_breakdown(s_id, question_id, question_topicid,
                                                         question_mainskillid, question_sunskillid, gain, create_on,
                                                         create_byid, update_on, update_byid)

        if not paper_emty and not result_empty_break and not result_empty:
            self.log.info("Data going to be update")
            self.update_df(s_id, p_id, lst, scan_data)

    def update_df(self, student_id, paper_id, lst, scan_data):
        self.data.remove_existing_data(student_id, paper_id, lst)

        for _, row in self.data.paper_marks_and_result(student_id, paper_id, lst, scan_data).iterrows():
            student_id = row['StudentId']
            question_id = row['QuestionId']
            gain = row['GainedMarks']
            creat_on = row['CreatedOn']
            creat_byid = row['CreatedById']
            update_on = row['UpdatedOn']
            update_byid = row['UpdatedById']
            answer = row['Answers']
            is_correct = row['IsCorrect']
            question_maintype = row['QuestionMainType']
            self.db.insert_question_result(student_id, question_id, gain, creat_on, creat_byid, update_on, update_byid,
                                           answer, is_correct, question_maintype)

        for _, row in self.data.paper_mark_result_individual(student_id, paper_id, lst, scan_data).iterrows():
            student_id = row['StudentId']
            question_id = row['QuestionId']
            question_topicid = row['QuestionTopicId']
            question_mainskillid = row['QuestionMainSkillId']
            question_sunskillid = row['QuestionSubSkillId']
            gain = row['GainedMarks']
            create_on = row['CreatedOn']
            create_byid = row['CreatedById']
            update_on = row['UpdatedOn']
            update_byid = row['UpdatedById']
            self.db.insert_question_result_breakdown(student_id, question_id, question_topicid, question_mainskillid,
                                                     question_sunskillid, gain, create_on, create_byid, update_on,
                                                     update_byid)







