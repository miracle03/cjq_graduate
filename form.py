# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QFileDialog, QApplication

class Ui_client(object):
    def setupUi(self, client):
        client.setObjectName("client")
        client.resize(868, 496)
        self.centralwidget = QtWidgets.QWidget()
        self.pushButton = QtWidgets.QPushButton(client)
        self.pushButton.setGeometry(QtCore.QRect(280, 300, 121, 81))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(client)
        QtCore.QMetaObject.connectSlotsByName(client)
        self.pushButton.clicked.connect(self.select)
    def retranslateUi(self, client):
        _translate = QtCore.QCoreApplication.translate
        client.setWindowTitle(_translate("client", "Form"))
        self.pushButton.setText(_translate("client", "PushButton"))
    def select(self):
        fd = QFileDialog.getExistingDirectory(self.centralwidget, "选择文件夹", "")
        print(fd)  # 打印文件夹路径
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formObj = QtWidgets.QMainWindow()
    ui = Ui_client()
    ui.setupUi(formObj)
    formObj.show()
    sys.exit(app.exec_())