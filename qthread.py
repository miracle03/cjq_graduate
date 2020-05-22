# -*- coding: utf-8 -*-
'''
PyQt5关于QThread的使用小demo
'''
import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, \
    QPushButton, QLineEdit, QLabel, QToolTip, QComboBox, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal

import server


class Demo(QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500, 500)
        self.setWindowTitle('Demo')
        self.setFixedSize(self.width(), self.height())
        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(20, 20, 460, 250)
        self.btn_start = QPushButton('start', self)
        self.btn_start.setGeometry(200, 350, 100, 50)
        self.btn_start.clicked.connect(self.slot_btn_start)

    def slot_btn_start(self):
        self.thread_1 = ThreadDemo()
        self.thread_1.start()
    def check(self):
        server.check()



class ThreadDemo(QThread):
    trigger = pyqtSignal(str)

    def __init__(self):
        super(ThreadDemo, self).__init__()

    def run(self):
        w=Demo()
        w.check()


def _main():
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':

    _main()