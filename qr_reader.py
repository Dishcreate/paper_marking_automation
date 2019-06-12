from pyzbar.pyzbar import decode
import cv2 as cv


class QR:

    def __init__(self):
        self.vl = 1

    def qr(self, img):
        img = cv.imread(img, 0)
        dim = (1600, 2000)
        # resize image
        resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
        qr_code = decode(resized)
        return qr_code

    def qr_details_mark_sheet(self, img):
        qr_code = self.qr(img)
        lst2 = [item[0] for item in qr_code][0]
        student_id = str(lst2).split('/')[-5]
        paper_id = str(lst2).split('/')[-4]
        qr_code = []
        return student_id, paper_id

    def qr_all_details(self, img):
        qr_code = self.qr(img)
        lst2 = [item[0] for item in qr_code][0]
        qr_code = []
        return lst2

    def qr_details_answer_sheet(self, img):
        qr_code = self.qr(img)
        lst2 = [item[0] for item in qr_code][0]
        student_id = str(lst2).split('/')[-4]
        paper_id = str(lst2).split('/')[-3]
        qr_code = []
        return student_id, paper_id

    def type(self, img):
        qr_code = self.qr(img)
        lst2 = [item[0] for item in qr_code][0]
        type_num = str(lst2).split('/')[-1].replace("'", "")
        return type_num

    def mark_or_answer(self, img):
        qr_code = self.qr(img)
        lst = [item[0] for item in qr_code][0]
        id = str(lst).split('/')[-2]
        return id

    def qr_details_oeq(self, img):
        qr_code = self.qr(img)
        lst2 = [item[0] for item in qr_code][0]
        student_id = str(lst2).split('/')[-3]
        paper_id = str(lst2).split('/')[-2]
        qr_code = []
        return student_id, paper_id
