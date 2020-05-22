# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_final.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from multiprocessing import Process

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
import client
import md5
ip=md5.get_ip()
key = "f1c1e25b079d45b7962a9e34772633f5"
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(780, 550)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(110, 100, 571, 301))
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(370, 30, 291, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_refresh = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.horizontalLayout.addWidget(self.pushButton_refresh)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 460, 371, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.pushButton_select = QtWidgets.QPushButton(Form)
        self.pushButton_select.setGeometry(QtCore.QRect(400, 460, 61, 41))
        self.pushButton_select.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Administrator/Desktop/Folder open.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_select.setIcon(icon)
        self.pushButton_select.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_select.setObjectName("pushButton_select")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(620, 440, 121, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #槽函数开始
        self.pushButton_refresh.clicked.connect(self.refresh_1)#刷新目录列表
        self.listWidget.itemClicked.connect(self.select_1)#从列表选择目录
        self.pushButton_select.clicked.connect(self.select_2)
        self.pushButton.clicked.connect(self.add)#添加目录
        self.pushButton_2.clicked.connect(self.update)  # 添加目录
        self.refresh_1()
    def update(self):
        key_1=self.lineEdit_2.text()
        path_1=self.lineEdit.text()
        if (md5.string_md5(key_1) == key):
           md5.dir_md5_update(path_1,ip)
           QMessageBox.information(self.centralwidget, "提示", "更改成功")
        else:
            QMessageBox.information(self.centralwidget, "提示", "密码错误 " )
        self.lineEdit.clear()
        self.lineEdit_2.clear()
    def add(self):
        path_1=self.lineEdit.text()
        row = 0;
        check = 0
        while(row<self.listWidget.count()):
            path_2=self.listWidget.item(row).text()
            if path_1==path_2:
                check=1
                break
            row=row+1

        if check ==0:
            md5.dir_md5_insert(path_1, ip)
            self.lineEdit.clear()
            QMessageBox.information(self.centralwidget, "提示", "添加成功")
        else:
            QMessageBox.information(self.centralwidget, "提示", "该目录已存在")
        self.lineEdit.clear()
    def  select_1(self,item):
        self.lineEdit.clear()
        self.lineEdit.setText(item.text())
    def  select_2(self,item):
        self.lineEdit.clear()
        directory1 = QFileDialog.getExistingDirectory(self.centralwidget, "选择文件夹", "/")
        self.lineEdit.setText(directory1)
    def refresh_1(self):
        result=md5.display_dir(ip)
        self.listWidget.clear()
        for i in result:
            self.listWidget.addItem(i)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "客户端"))
        self.label.setText(_translate("Form", "文件目录"))
        self.pushButton_refresh.setText(_translate("Form", "刷新目录"))
        self.label_2.setText(_translate("Form", "选择目录"))
        self.label_3.setText(_translate("Form", "密码"))
        self.pushButton.setText(_translate("Form", "添加目录"))
        self.pushButton_2.setText(_translate("Form", "更新目录"))

def _main():
    import  sys
    app = QApplication(sys.argv)
    window = QWidget()
    demo = Ui_Form()
    demo.setupUi(window)
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    p = Process(target=client.main)
    p.start()
    p1 = Process(target=_main())
    p1.start()