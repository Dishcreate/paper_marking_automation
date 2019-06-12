import numpy as np
from oeq_process import Process
from model import DnnModel


class PredictData:

    def __init__(self):
        self.ip = Process()
        self.model = DnnModel()

    def create_data_array(self, img):
        return np.concatenate((self.ip.q_1_5(img),
                               self.ip.q_6_10(img),
                               self.ip.q_11_15(img),
                               self.ip.q_16_20(img),
                               self.ip.q_21_25(img),
                               self.ip.q_26_30(img),
                               self.ip.q_31_35(img),
                               self.ip.q_36_40(img)), axis=0)

    def paper_df_data(self, img):

        model = self.model.model_creation()
        paper_data = []

        for num, data in enumerate(self.create_data_array(img)):
            circle_num = data[1]
            circle_data = data[0]
            pre_data = circle_data.reshape(-1, 40, 40, 1)
            model_out = model.predict(np.array(pre_data))[0]
            if model_out[:1] > model_out[1:2]:
                paper_data.append([circle_num[0], circle_num[1]])
            else:
                paper_data.append([circle_num[0], 0])

        return paper_data
