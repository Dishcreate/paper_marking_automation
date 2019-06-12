import pandas as pd
import numpy as np
from oeq_db import Db
import datetime
import logging


class DataHandle:

    def __init__(self, db_obt=Db(), log=logging):
        self.log = log
        self.db = db_obt
        self.paper_data = []

    def range(self, n):
        a = 1 + 40 * (n - 1)
        b = a + 40 - 1
        return a, b

    def start_end(self, itr, start, end):
        if itr == 1:
            return start, end
        if itr > 1:
            return (start - (40 * (itr-1))), (end - (40 * (itr-1)))

    def question_id(self, paper_id, lst):
        df_mark = self.db.details_of_marks(paper_id)
        df_mark = df_mark.sort_values('Number1')
        paper_itr = int(str(lst).split('/')[-1][0:1])
        a, b = self.range(int(paper_itr))

        df_mark = df_mark.iloc[a-1:]
        question_id = df_mark[['QuestionId', 'Number1']]
        return question_id

    def paper(self, student_id, paper_id, id_num=1):
        now = datetime.datetime.now()
        columns = ['StudentId', 'PaperId']
        df = pd.DataFrame(columns=columns)
        df.loc[0] = [str(student_id), int(paper_id)]
        df['MarkingSheet'] = None
        df['IsAbsent'] = False
        df['IsValidReason'] = False
        df['CreatedOn'] = now
        df['CreatedById'] = id_num
        df['UpdatedOn'] = now
        df['UpdatedById'] = id_num
        # print(df)
        return df

    def paper_marks_and_result(self, student_id, paper_id, lst, scan_data, id_num=1):
        paper_itr = int(str(lst).split('/')[-1].replace("'", ""))
        a, b = self.range(int(paper_itr))
        columns = ['Number1', 'Shade']
        shade_df = pd.DataFrame(np.array(scan_data), columns=columns)
        shade_df.Number1 = shade_df.Number1.astype(int)
        shade_df.Shade = shade_df.Shade.astype(int)
        shade_df['Shade'] = shade_df['Shade'].map({0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 0.5})
        c = shade_df[['Number1', 'Shade']].groupby(["Number1"], as_index=False).sum().sort_values('Number1')
        c['Number1'] = c['Number1']+(a-1)
        c['StudentId'] = str(student_id)
        join = self.question_id(paper_id, lst)
        join = pd.merge(join, c, on='Number1')
        join['Answers'] = None  # c['Answers'].values
        join['StudentId'] = join['StudentId'].values.astype('unicode')
        join.Answers = join.Answers.astype(str)
        join['IsCorrect'] = None  # np.where((join['CorrectAnswers'] == join['Answers']), True, False)
        join['GainedMarks'] = join["Shade"].values  # np.where((join['IsCorrect'] == True), join['TotalAllocatedMarks'], 0)
        join.GainedMarks = join.GainedMarks.astype(float)
        join['QuestionMainType'] = int(1)

        now = datetime.datetime.now()
        join['CreatedOn'] = now
        join['CreatedById'] = id_num
        join['UpdatedOn'] = now
        join['UpdatedById'] = id_num
        final = join[['StudentId', 'QuestionId', 'GainedMarks', 'CreatedOn', 'CreatedById', 'UpdatedOn', 'UpdatedById',
                      'Answers', 'IsCorrect', 'QuestionMainType']]
        return final

    def paper_mark_result_individual(self, student_id, paper_id, lst, scan_data, id_num=1):
        df_mark_ind = self.db.details_of_mark_individual(paper_id)
        paper_itr = int(str(lst).split('/')[-1][0:1])
        a, b = self.range(int(paper_itr))

        df_mark_ind = df_mark_ind.iloc[a-1:]
        now = datetime.datetime.now()
        df = self.paper_marks_and_result(student_id, paper_id, lst, scan_data)
        head = len(df)
        df_mark_ind = df_mark_ind.head(head)
        df_mark_ind.insert(0, 'StudentId', student_id)
        df_mark_ind['CreatedOn'] = now
        df_mark_ind['CreatedById'] = id_num
        df_mark_ind['UpdatedOn'] = now
        df_mark_ind['UpdatedById'] = id_num
        df_mark_ind = df_mark_ind.drop('GainedMarks', axis=1)
        df_mark_ind['GainedMarks'] = df['GainedMarks'].values
        return df_mark_ind

    def remove_existing_data(self, student_id, paper_id, lst):
        df_mark_ind = self.question_id(paper_id, lst)
        question_id = df_mark_ind['QuestionId']

        for q_id in question_id:
            self.db.delete_result(student_id, q_id)








