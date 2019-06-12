import numpy as np
import cv2 as cv
from oeq_validation import Validate as Vl


class Process:

    def __init__(self):
        self.vl = Vl()

    def q_1_5(self, img):
        detect = self.vl.circles(img)
        img = cv.imread(img, cv.IMREAD_GRAYSCALE)
        image = cv.threshold(img, 210, 255, cv.THRESH_BINARY)[1]
        predict_data = []

        row_1_14 = detect[0:14]
        row_1_14_sorted = sorted(row_1_14, key=lambda t: t[0])
        q1_1_7 = row_1_14_sorted[0:7]
        j_1 = 0
        for i in q1_1_7:
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([1, j_1])])
            j_1 = j_1 + 1

        row_2_14 = detect[14:28]
        row_2_14_sorted = sorted(row_2_14, key=lambda t: t[0])
        q2_1_7 = row_2_14_sorted[0:7]
        j_2 = 0
        for i in q2_1_7:
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([2, j_2])])
            j_2 = j_2 + 1

        row_3_14 = detect[28:42]
        row_3_14_sorted = sorted(row_3_14, key=lambda t: t[0])
        q3_1_7 = row_3_14_sorted[0:7]
        j_3 = 0
        for i in q3_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([3, j_3])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_3 = j_3 + 1

        row_4_14 = detect[42:56]
        row_4_14_sorted = sorted(row_4_14, key=lambda t: t[0])
        q4_1_7 = row_4_14_sorted[0:7]
        # q24_1_7 = row_4_14_sorted[7:14]
        j_4 = 0
        for i in q4_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([4, j_4])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_4 = j_4 + 1

        row_5_14 = detect[56:70]
        row_5_14_sorted = sorted(row_5_14, key=lambda t: t[0])
        q5_1_7 = row_5_14_sorted[0:7]
        # q25_1_7 = row_5_14_sorted[7:14]
        j_5 = 0
        for i in q5_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([5, j_5])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_5 = j_5 + 1

        return predict_data

    def q_6_10(self, img):
        detect = self.vl.circles(img)
        img = cv.imread(img, cv.IMREAD_GRAYSCALE)
        image = cv.threshold(img, 210, 255, cv.THRESH_BINARY)[1]
        predict_data = []

        row_6_14 = detect[70:84]
        row_6_14_sorted = sorted(row_6_14, key=lambda t: t[0])
        q6_1_7 = row_6_14_sorted[0:7]
        j_6 = 0
        for i in q6_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([6, j_6])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_6 = j_6 + 1

        row_7_14 = detect[84:98]
        row_7_14_sorted = sorted(row_7_14, key=lambda t: t[0])
        q7_1_7 = row_7_14_sorted[0:7]
        j_7 = 0
        for i in q7_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([7, j_7])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_7 = j_7 + 1

        row_8_14 = detect[98:112]
        row_8_14_sorted = sorted(row_8_14, key=lambda t: t[0])
        q8_1_7 = row_8_14_sorted[0:7]
        # q28_1_7 = row_8_14_sorted[7:14]
        j_8 = 0
        for i in q8_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([8, j_8])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_8 = j_8 + 1

        row_9_14 = detect[112:126]
        row_9_14_sorted = sorted(row_9_14, key=lambda t: t[0])
        q9_1_7 = row_9_14_sorted[0:7]
        # q29_1_7 = row_9_14_sorted[7:14]
        j_9 = 0
        for i in q9_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([9, j_9])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_9 = j_9 + 1

        row_10_14 = detect[126:140]
        row_10_14_sorted = sorted(row_10_14, key=lambda t: t[0])
        q10_1_7 = row_10_14_sorted[0:7]
        # q30_1_7 = row_10_14_sorted[7:14]
        j_10 = 0
        for i in q10_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([10, j_10])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_10 = j_10 + 1

        return predict_data

    def q_11_15(self, img):
        detect = self.vl.circles(img)
        img = cv.imread(img, cv.IMREAD_GRAYSCALE)
        image = cv.threshold(img, 210, 255, cv.THRESH_BINARY)[1]
        predict_data = []

        row_11_14 = detect[140:154]
        row_11_14_sorted = sorted(row_11_14, key=lambda t: t[0])
        q11_1_7 = row_11_14_sorted[0:7]
        # q31_1_7 = row_11_14_sorted[7:14]
        j_11 = 0
        for i in q11_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([11, j_11])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_11 = j_11 + 1

        row_12_14 = detect[154:168]
        row_12_14_sorted = sorted(row_12_14, key=lambda t: t[0])
        q12_1_7 = row_12_14_sorted[0:7]
        # q32_1_7 = row_12_14_sorted[7:14]
        j_12 = 0
        for i in q12_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([12, j_12])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_12 = j_12 + 1

        row_13_14 = detect[168:182]
        row_13_14_sorted = sorted(row_13_14, key=lambda t: t[0])
        q13_1_7 = row_13_14_sorted[0:7]
        # q33_1_7 = row_13_14_sorted[7:14]
        j_13 = 0
        for i in q13_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([13, j_13])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_13 = j_13 + 1

        row_14_14 = detect[182:196]
        row_14_14_sorted = sorted(row_14_14, key=lambda t: t[0])
        q14_1_7 = row_14_14_sorted[0:7]
        # q34_1_7 = row_14_14_sorted[7:14]
        j_14 = 0
        for i in q14_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([14, j_14])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_14 = j_14 + 1

        row_15_14 = detect[196:210]
        row_15_14_sorted = sorted(row_15_14, key=lambda t: t[0])
        q15_1_7 = row_15_14_sorted[0:7]
        # q35_1_7 = row_15_14_sorted[7:14]
        j_15 = 0
        for i in q15_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([15, j_15])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_15 = j_15 + 1

        return predict_data

    def q_16_20(self, img):
        detect = self.vl.circles(img)
        img = cv.imread(img, cv.IMREAD_GRAYSCALE)
        image = cv.threshold(img, 210, 255, cv.THRESH_BINARY)[1]
        predict_data = []

        row_16_14 = detect[210:224]
        row_16_14_sorted = sorted(row_16_14, key=lambda t: t[0])
        q16_1_7 = row_16_14_sorted[0:7]
        # q36_1_7 = row_16_14_sorted[7:14]
        j_16 = 0
        for i in q16_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([16, j_16])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_16 = j_16 + 1

        row_17_14 = detect[224:238]
        row_17_14_sorted = sorted(row_17_14, key=lambda t: t[0])
        q17_1_7 = row_17_14_sorted[0:7]
        # q37_1_7 = row_17_14_sorted[7:14]
        j_17 = 0
        for i in q17_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([17, j_17])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_17 = j_17 + 1

        row_18_14 = detect[238:252]
        row_18_14_sorted = sorted(row_18_14, key=lambda t: t[0])
        q18_1_7 = row_18_14_sorted[0:7]
        # q38_1_7 = row_18_14_sorted[7:14]
        j_18 = 0
        for i in q18_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([18, j_18])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_18 = j_18 + 1

        row_19_14 = detect[252:266]
        row_19_14_sorted = sorted(row_19_14, key=lambda t: t[0])
        q19_1_7 = row_19_14_sorted[0:7]
        # q39_1_7 = row_19_14_sorted[7:14]
        j_19 = 0
        for i in q19_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([19, j_19])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_19 = j_19 + 1

        row_20_14 = detect[266:280]
        row_20_14_sorted = sorted(row_20_14, key=lambda t: t[0])
        q20_1_7 = row_20_14_sorted[0:7]
        # q40_1_7 = row_20_14_sorted[7:14]
        j_20 = 0
        for i in q20_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([20, j_20])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_20 = j_20 + 1

        return predict_data

    def q_21_25(self, img):
        detect = self.vl.circles(img)
        img = cv.imread(img, cv.IMREAD_GRAYSCALE)
        image = cv.threshold(img, 210, 255, cv.THRESH_BINARY)[1]
        predict_data = []

        row_1_14 = detect[0:14]
        row_1_14_sorted = sorted(row_1_14, key=lambda t: t[0])
        # q1_1_7 = row_1_14_sorted[0:7]
        q21_1_7 = row_1_14_sorted[7:14]
        j_21 = 0
        for i in q21_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([21, j_21])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_21 = j_21 + 1

        row_2_14 = detect[14:28]
        row_2_14_sorted = sorted(row_2_14, key=lambda t: t[0])
        # q2_1_7 = row_2_14_sorted[0:7]
        q22_1_7 = row_2_14_sorted[7:14]
        j_22 = 0
        for i in q22_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([22, j_22])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_22 = j_22 + 1

        row_3_14 = detect[28:42]
        row_3_14_sorted = sorted(row_3_14, key=lambda t: t[0])
        # q3_1_7 = row_3_14_sorted[0:7]
        q23_1_7 = row_3_14_sorted[7:14]
        j_23 = 0
        for i in q23_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([23, j_23])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_23 = j_23 + 1

        row_4_14 = detect[42:56]
        row_4_14_sorted = sorted(row_4_14, key=lambda t: t[0])
        # q4_1_7 = row_4_14_sorted[0:7]
        q24_1_7 = row_4_14_sorted[7:14]
        j_24 = 0
        for i in q24_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([24, j_24])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_24 = j_24 + 1

        row_5_14 = detect[56:70]
        row_5_14_sorted = sorted(row_5_14, key=lambda t: t[0])
        # q5_1_7 = row_5_14_sorted[0:7]
        q25_1_7 = row_5_14_sorted[7:14]
        j_25 = 0
        for i in q25_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([25, j_25])])
            # cv2.imwrite('test/' + str(j) + '.png', crop_size)
            j_25 = j_25 + 1

        return predict_data

    def q_26_30(self, img):
        detect = self.vl.circles(img)
        img = cv.imread(img, cv.IMREAD_GRAYSCALE)
        image = cv.threshold(img, 210, 255, cv.THRESH_BINARY)[1]
        predict_data = []

        row_6_14 = detect[70:84]
        row_6_14_sorted = sorted(row_6_14, key=lambda t: t[0])
        # q6_1_7 = row_6_14_sorted[0:7]
        q26_1_7 = row_6_14_sorted[7:14]
        j_26 = 0
        for i in q26_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([26, j_26])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_26 = j_26 + 1

        row_7_14 = detect[84:98]
        row_7_14_sorted = sorted(row_7_14, key=lambda t: t[0])
        # q7_1_7 = row_7_14_sorted[0:7]
        q27_1_7 = row_7_14_sorted[7:14]
        j_27 = 0
        for i in q27_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([27, j_27])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_27 = j_27 + 1

        row_8_14 = detect[98:112]
        row_8_14_sorted = sorted(row_8_14, key=lambda t: t[0])
        # q8_1_7 = row_8_14_sorted[0:7]
        q28_1_7 = row_8_14_sorted[7:14]
        j_28 = 0
        for i in q28_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([28, j_28])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_28 = j_28 + 1

        row_9_14 = detect[112:126]
        row_9_14_sorted = sorted(row_9_14, key=lambda t: t[0])
        # q9_1_7 = row_9_14_sorted[0:7]
        q29_1_7 = row_9_14_sorted[7:14]
        j_29 = 0
        for i in q29_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([29, j_29])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_29 = j_29 + 1

        row_10_14 = detect[126:140]
        row_10_14_sorted = sorted(row_10_14, key=lambda t: t[0])
        # q10_1_7 = row_10_14_sorted[0:7]
        q30_1_7 = row_10_14_sorted[7:14]
        j_30 = 0
        for i in q30_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([30, j_30])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_30 = j_30 + 1

        return predict_data

    def q_31_35(self, img):
        detect = self.vl.circles(img)
        img = cv.imread(img, cv.IMREAD_GRAYSCALE)
        image = cv.threshold(img, 210, 255, cv.THRESH_BINARY)[1]
        predict_data = []

        row_11_14 = detect[140:154]
        row_11_14_sorted = sorted(row_11_14, key=lambda t: t[0])
        # q11_1_7 = row_11_14_sorted[0:7]
        q31_1_7 = row_11_14_sorted[7:14]
        j_31 = 0
        for i in q31_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([31, j_31])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_31 = j_31 + 1

        row_12_14 = detect[154:168]
        row_12_14_sorted = sorted(row_12_14, key=lambda t: t[0])
        # q12_1_7 = row_12_14_sorted[0:7]
        q32_1_7 = row_12_14_sorted[7:14]
        j_32 = 0
        for i in q32_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([32, j_32])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_32 = j_32 + 1

        row_13_14 = detect[168:182]
        row_13_14_sorted = sorted(row_13_14, key=lambda t: t[0])
        # q13_1_7 = row_13_14_sorted[0:7]
        q33_1_7 = row_13_14_sorted[7:14]
        j_33 = 0
        for i in q33_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([33, j_33])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_33 = j_33 + 1

        row_14_14 = detect[182:196]
        row_14_14_sorted = sorted(row_14_14, key=lambda t: t[0])
        # q14_1_7 = row_14_14_sorted[0:7]
        q34_1_7 = row_14_14_sorted[7:14]
        j_34 = 0
        for i in q34_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([34, j_34])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_34 = j_34 + 1

        row_15_14 = detect[196:210]
        row_15_14_sorted = sorted(row_15_14, key=lambda t: t[0])
        # q15_1_7 = row_15_14_sorted[0:7]
        q35_1_7 = row_15_14_sorted[7:14]
        j_35 = 0
        for i in q35_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([35, j_35])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_35 = j_35 + 1

        return predict_data

    def q_36_40(self, img):
        detect = self.vl.circles(img)
        img = cv.imread(img, cv.IMREAD_GRAYSCALE)
        image = cv.threshold(img, 210, 255, cv.THRESH_BINARY)[1]
        predict_data = []

        row_16_14 = detect[210:224]
        row_16_14_sorted = sorted(row_16_14, key=lambda t: t[0])
        # q16_1_7 = row_16_14_sorted[0:7]
        q36_1_7 = row_16_14_sorted[7:14]
        j_36 = 0
        for i in q36_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([36, j_36])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_36 = j_36 + 1

        row_17_14 = detect[224:238]
        row_17_14_sorted = sorted(row_17_14, key=lambda t: t[0])
        # q17_1_7 = row_17_14_sorted[0:7]
        q37_1_7 = row_17_14_sorted[7:14]
        j_37 = 0
        for i in q37_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([37, j_37])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_37 = j_37 + 1

        row_18_14 = detect[238:252]
        row_18_14_sorted = sorted(row_18_14, key=lambda t: t[0])
        # q18_1_7 = row_18_14_sorted[0:7]
        q38_1_7 = row_18_14_sorted[7:14]
        j_38 = 0
        for i in q38_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([38, j_38])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_38 = j_38 + 1

        row_19_14 = detect[252:266]
        row_19_14_sorted = sorted(row_19_14, key=lambda t: t[0])
        # q19_1_7 = row_19_14_sorted[0:7]
        q39_1_7 = row_19_14_sorted[7:14]
        j_39 = 0
        for i in q39_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([39, j_39])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_39 = j_39 + 1

        row_20_14 = detect[266:280]
        row_20_14_sorted = sorted(row_20_14, key=lambda t: t[0])
        # q20_1_7 = row_20_14_sorted[0:7]
        q40_1_7 = row_20_14_sorted[7:14]
        j_40 = 0
        for i in q40_1_7:
            # print(i)
            # print(j)
            start_row, start_col = i[1] - 40, i[0] - 40
            end_row, end_col = i[1] + 40, i[0] + 40
            crop = image[start_row:end_row, start_col:end_col]
            crop_size = cv.resize(crop, (40, 40))
            predict_data.append([np.array(crop_size), np.array([40, j_40])])
            # cv.imwrite('test/' + str(j) + '.png', crop_size)
            j_40 = j_40 + 1

        return predict_data



