import numpy as np
import cv2 as cv
import logging


class Validate:

    def __init__(self):
        logging.basicConfig(filename='systemlog/error.log', level=logging.ERROR)
        logging.basicConfig(filename='systemlog/info.log', level=logging.INFO)
        logging.basicConfig(filename='systemlog/debug.log', level=logging.DEBUG)
        logging.basicConfig(filename='systemlog/warning.log', level=logging.WARNING)
        # self.data = []

    def find_quality_image(self, path):
        # logging.basicConfig(filename='systemlog/system.log', level=logging.DEBUG)
        gray = self.calculate_edge(path)
        img = cv.imread(path, cv.IMREAD_GRAYSCALE)
        (thresh, im_bw) = cv.threshold(img, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        fm = cv.Laplacian(gray, cv.CV_64F).var()
        if thresh >= fm:
            message = path
            info = path + '-' + "The image successfully send to scan process"
            logging.info(info)
            return message, 'success'
        else:
            message = path
            error = path + '-' + "The image can not be scan because of poor quality"
            logging.error(error)
            return message, 'not_success'
            # sys.exit('The quality of the image not satisfy minimal requirement')

    """
        calculate conner edges with coordinate of first conner in top of answer sheet
        @:return : coordinate x , y
        @:return : height , width
        @:return : gray 
    """
    def calculate_edge(self, img):
        img2 = cv.imread(img)
        gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (15, 15), 0)
        return gray

    def range(self, n):
        a = 1 + 40 * (n - 1)
        b = a + 40 - 1
        return a, b

    def circles(self, img):
        img = cv.imread(img, 0)
        img = cv.medianBlur(img, 3)
        data = []

        circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=24, maxRadius=33)

        circles = np.uint16(np.around(circles))

        for i in circles[0, :]:
            if i[1] > 500:
                data.append([i[0], i[1]])
        detect = sorted(data, key=lambda t: t[1])
        return detect

    def array_length(self, img):
        data = self.circles(img)
        len_data = len(data)
        if len_data == 280:
            return True
        else:
            return False

    def calculate_qr_edge(self, img):
        img = cv.imread(img, 0)
        img = cv.medianBlur(img, 3)
        data = []

        circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=20, maxRadius=30)

        circles = np.uint16(np.around(circles))

        for i in circles[0, :]:
            if i[1] < 300:
                data.append([i[0], i[1]])

        detect = sorted(data, key=lambda t: t[0])
        return detect










