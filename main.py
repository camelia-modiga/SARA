from PyQt5.QtWidgets import *
from PyQt5 import uic
from theme_config import *

import sys


class SpeachWindow(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi("assets/speech.ui", self)
        self.setWindowTitle('Tap and talk')
        self.setStyleSheet("background-color:" + BACKGROUND_COLOR)
        self.label = self.findChild(QLabel, "label")
        self.label.setStyleSheet("QLabel{ font-size: 25pt;"
                                 "font-family: URW Bookman;"
                                 "font-style: italic;"
                                 "color: " + TITLE_COLOR + "; }")
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.setStyleSheet("QPushButton{"
                                  "background-color:" + BUTTON_COLOR_STYLE_1 + ";}")

        # self.button.setIcon(QIcon('assets/mic.png')) self.emailButton = self.findChild(QPushButton, "emailButton")
        # self.emailButton.setStyleSheet("QPushButton{" "background-color:" + BUTTON_COLOR_STYLE_1 + ";" "color:" +
        # BUTTON_TEXT_COLOR_STYLE_1 + ";}")

        self.textEdit = self.findChild(QTextEdit, "textEdit")
        self.textEdit.setStyleSheet("QTextEdit{"
                                    "color:" + TEXT_EDIT_COLOR + ";}")


class TextWindow(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi("assets/text.ui", self)
        self.setWindowTitle('Tap and listen')
        self.setStyleSheet("background-color:" + BACKGROUND_COLOR)
        self.label = self.findChild(QLabel, "label")
        self.label.setStyleSheet("QLabel{ font-size: 25pt;"
                                 "font-family: URW Bookman;"
                                 "font-style: italic;"
                                 "color: " + TITLE_COLOR + "; }")
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.setStyleSheet("QPushButton{"
                                  "background-color:" + BUTTON_COLOR_STYLE_1 + ";}")

        self.textEdit = self.findChild(QTextEdit, "textEdit")
        self.textEdit.setStyleSheet("QTextEdit{"
                                    "color:" + TEXT_EDIT_COLOR + ";}")


class MenuWindow(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi("assets/menu.ui", self)
        self.speech_window = None
        self.text_window = None
        self.setWindowTitle('Welcome')
        self.setStyleSheet("background-color:" + BACKGROUND_COLOR)
        self.titleLabel = self.findChild(QLabel, "title_label")
        self.titleLabel.setStyleSheet("QLabel{ font-size: 40pt;"
                                      "font-family: URW Bookman;"
                                      "font-style: italic;"
                                      "color: " + TITLE_COLOR + "; }")
        self.speechButton = self.findChild(QPushButton, "speechButton")
        self.speechButton.setStyleSheet("QPushButton{"
                                        "background-color:" + BUTTON_COLOR_STYLE_1 + ";"
                                                                                     "color:" + BUTTON_TEXT_COLOR_STYLE_1 + ";}")
        self.textButton = self.findChild(QPushButton, "textButton")
        self.textButton.setStyleSheet("QPushButton{"
                                      "background-color:" + BUTTON_COLOR_STYLE_1 + ";"
                                                                                   "color:" + BUTTON_TEXT_COLOR_STYLE_1 + ";}")
        self.speechButton.clicked.connect(self.show_speech_window)
        self.textButton.clicked.connect(self.show_text_window)

    def show_speech_window(self):
        if self.speech_window is None:
            self.speech_window = SpeachWindow()
        self.speech_window.show()
        self.hide()

    def show_text_window(self):
        if self.text_window is None:
            self.text_window = TextWindow()
        self.text_window.show()
        self.hide()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.startButton = None
        uic.loadUi("assets/start.ui", self)
        self.setWindowTitle('S.A.R.A')
        self.titleLabel = self.findChild(QLabel, "title_label")
        self.titleLabel.setStyleSheet("QLabel{ font-size: 40pt;"
                                      "font-family: URW Bookman;"
                                      "font-style: italic;"
                                      "color: " + TITLE_COLOR + ";}")
        self.subtitleLabel = self.findChild(QLabel, "subtitle_label")
        self.subtitleLabel.setStyleSheet("QLabel{ font-size: 25pt;"
                                         "font-family: URW Bookman;"
                                         "font-style: italic;"
                                         "color: " + TITLE_COLOR + ";}")
        self.startButton = self.findChild(QPushButton, "startButton")
        self.startButton.setStyleSheet("QPushButton{"
                                       "background-color:" + BUTTON_COLOR_STYLE_1 + ";"
                                                                                    "color:" + BUTTON_TEXT_COLOR_STYLE_1 + ";}")
        self.menu_window = None
        self.startButton.clicked.connect(self.show_menu_window)

    def show_menu_window(self):
        if self.menu_window is None:
            self.menu_window = MenuWindow()
        self.menu_window.show()
        self.hide()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
