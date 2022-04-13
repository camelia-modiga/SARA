import cv2 as cv
import pyautogui
from PyQt5.QtCore import pyqtSignal, QThread
import numpy as np
import time

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def run(self):
        cap = cv.VideoCapture(0)

        if not cap.isOpened:
            print('--(!)Error opening video capture')
            exit(0)
        while True:
            ret, frame = cap.read()
            cvImg = cv.flip(frame, 1)
            gray = cv.cvtColor(cvImg, cv.COLOR_BGR2GRAY)
            face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in face_rects:
                cv.rectangle(cvImg, (x + int(w / 2), y + int(h / 2)), (x + int(w / 2), y +
                                                                       int(h / 2)), (0, 255, 0), 3)

                pyautogui.moveTo(x, y)

                # if time.time() > 2000:
                #     pyautogui.leftClick()
