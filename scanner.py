# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import nmap
import json
from sqlalchemy.sql.expression import true
from gevent.resolver import hostname_types
from _ast import arguments


class Ui_scanner(QtWidgets.QWidget):
    select = -1
    Printer = '9100'
    webcam = '81,554'
    arg = {'主机探测(不扫描端口)': '-sn -sV', 'TCP方式主机探测': '-PS -sV -O', 'ICMP方式主机探测': '-PE -PP -sV -O',
           'IP协议方式主机探测': '-PO -sV -O', 'TCP SYN扫描': '-sS -sV -O', 'TCP ACK扫描': '-sA -sV -O', 'UDP扫描': '-sU -sV -O',
           '操作系统侦测': '-O'}

    def __init__(self, parent=None):
        self.scanResults = {}
        super(Ui_scanner, self).__init__()

    def setupUi(self, scanner):
        scanner.setObjectName("scanner")
        scanner.resize(1240, 700)
        self.gridLayoutWidget = QtWidgets.QWidget(scanner)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 10, 1151, 631))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ip = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ip.setObjectName("ip")
        self.gridLayout.addWidget(self.ip, 1, 2, 1, 1)

        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.port = QtWidgets.QWidget()
        self.port.setObjectName("port")
        self.tableWidget = QtWidgets.QTableWidget(self.port)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 481, 551))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 选中一行
        # self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(75)
        self.tableWidget.resizeRowsToContents()
        # self.tableWidget.setMouseTracking(True)
        # self.tableWidget.entered(QModelIndex).connect(self.showToolTip(QModelIndex))
        self.tabWidget.addTab(self.port, "")
        self.hoststate = QtWidgets.QWidget()
        self.hoststate.setObjectName("hoststate")
        self.textEdit_2 = QtWidgets.QTextEdit(self.hoststate)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 0, 481, 551))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setReadOnly(True)
        self.tabWidget.addTab(self.hoststate, "")
        self.os = QtWidgets.QWidget()
        self.os.setObjectName("os")
        self.textEdit = QtWidgets.QTextEdit(self.os)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 481, 551))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.tabWidget.addTab(self.os, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label_up = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_up.setObjectName("label_up")
        self.gridLayout_2.addWidget(self.label_up, 0, 0, 1, 1)

        self.uphost = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.uphost.setObjectName("uphost")
        self.uphost.setEnabled(False)
        self.gridLayout_2.addWidget(self.uphost, 0, 1, 1, 1)

        self.label_down = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_down.setObjectName("label_down")
        self.gridLayout_2.addWidget(self.label_down, 1, 0, 1, 1)

        self.downhost = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.downhost.setObjectName("downhost")
        self.downhost.setEnabled(False)
        self.gridLayout_2.addWidget(self.downhost, 1, 1, 1, 1)

        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        # self.gridLayout_2.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.comboBox_2, 2, 1, 1, 1)

        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        """self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        """
        self.comboBox_3.addItems(
            ['主机探测(不扫描端口)', 'TCP方式主机探测', 'ICMP方式主机探测', 'IP方式主机探测', 'TCP SYN扫描', 'TCP ACK扫描', 'UDP扫描'])

        self.gridLayout_2.addWidget(self.comboBox_3, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.startportScan)  # 与扫描函数关联
        self.gridLayout_2.addWidget(self.pushButton, 4, 1, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_2, 2, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)

        self.listWidget.itemClicked.connect(self.outp)  # 显示信息随选择的item变化
        self.comboBox_2.currentIndexChanged.connect(self.comboboxchange)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.port_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.port_input.setText("")
        self.port_input.setObjectName("port_input")
        self.gridLayout.addWidget(self.port_input, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)
        # self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        # self.pushButton.setObjectName("pushButton_2")
        # self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
        self.retranslateUi(scanner)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(scanner)

    def retranslateUi(self, scanner):
        _translate = QtCore.QCoreApplication.translate
        scanner.setWindowTitle(_translate("scanner", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("scanner", "端口"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("scanner", "协议"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("scanner", "状态"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("scanner", "服务"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("scanner", "版本"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("scanner", "应用信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.port), _translate("scanner", "端口信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hoststate), _translate("scanner", "主机状态"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.os), _translate("scanner", "操作系统侦测"))
        self.comboBox_2.setItemText(0, _translate("scanner", "主机"))
        self.comboBox_2.setItemText(1, _translate("scanner", "摄像头"))
        self.comboBox_2.setItemText(2, _translate("scanner", "打印机"))
        self.label.setText(_translate("scanner", "设备类型"))
        self.label_2.setText(_translate("scanner", "扫描方案"))
        self.label_up.setText(_translate("scanner", "上线主机数"))
        self.label_down.setText(_translate("scanner", "下线主机数"))
        self.pushButton.setText(_translate("scanner", "扫描"))
        self.label_3.setText(_translate("scanner", "目标地址"))
        self.label_4.setText(_translate("scanner", "主机列表"))
        self.label_5.setText(_translate("scanner", "端口"))

    # def showToolTip(self,index):
    #    QToolTip.showText(QCursor.pos(), str(index.data()))
    def comboboxchange(self):
        temp = str(self.comboBox_2.currentText())
        if temp == '摄像头' or temp == '打印机':
            self.comboBox_3.clear()
            # self.comboBox_3.addItems(['TCP SYN扫描','TCP ACK扫描','UDP扫描'])
            self.comboBox_3.addItems(['TCP SYN扫描', 'TCP ACK扫描'])
        else:
            self.comboBox_3.clear()
            self.comboBox_3.addItems(
                ['主机探测(不扫描端口)', 'TCP方式主机探测', 'ICMP方式主机探测', 'IP方式主机探测', 'TCP SYN扫描', 'TCP ACK扫描', 'UDP扫描'])

    def outp(self, item):
        # self.tableWidget.clearContents()
        selectedhost = str(item.text())
        # print(str(item.text()))
        selecteddict = self.scanResults['scan'][selectedhost]
        self.tableWidget.setRowCount(0)
        # 输出端口信息
        if 'udp' in selecteddict:
            print('a')
            rowCount = self.tableWidget.rowCount()
            for port in selecteddict['udp']:
                self.tableWidget.insertRow(rowCount)
                self.tableWidget.setItem(rowCount, 0, QTableWidgetItem(str(port)))
                self.tableWidget.setItem(rowCount, 1, QTableWidgetItem('udp'))
                self.tableWidget.setItem(rowCount, 2, QTableWidgetItem(selecteddict['upp'][port]['state']))
                self.tableWidget.setItem(rowCount, 3, QTableWidgetItem(selecteddict['upp'][port]['name']))
                self.tableWidget.setItem(rowCount, 4, QTableWidgetItem(selecteddict['upp'][port]['version']))
                self.tableWidget.setItem(rowCount, 4, QTableWidgetItem(selecteddict['upp'][port]['product']))
        if 'tcp' in selecteddict:
            print('b')
            for port in selecteddict['tcp']:
                rowCount = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowCount)
                self.tableWidget.setItem(rowCount, 0, QTableWidgetItem(str(port)))
                self.tableWidget.setItem(rowCount, 1, QTableWidgetItem('tcp'))
                self.tableWidget.setItem(rowCount, 2, QTableWidgetItem(selecteddict['tcp'][port]['state']))
                self.tableWidget.setItem(rowCount, 3, QTableWidgetItem(selecteddict['tcp'][port]['name']))
                self.tableWidget.setItem(rowCount, 4, QTableWidgetItem(selecteddict['tcp'][port]['version']))
                self.tableWidget.setItem(rowCount, 4, QTableWidgetItem(selecteddict['tcp'][port]['product']))

        self.tableWidget.resizeColumnsToContents()
        # 输出主机状态
        hostinfo = '主机状态:'
        hostinfo += (str(selecteddict['status']['state']) + '\n')
        print('c')
        hostinfo += ('主机名称:' + str(selecteddict['hostnames'][0]['name']) + '\n')
        print('d')
        if 'ipv4' in selecteddict['addresses']:
            hostinfo += ('ipv4地址:' + str(selecteddict['addresses']['ipv4']) + '\n')
            print('e')
        if 'ipv6' in selecteddict['addresses']:
            hostinfo += ('ipv6地址:' + str(selecteddict['addresses']['ipv6']) + '\n')
            print('f')
        print('ff')
        mac = ''
        if 'mac' in selecteddict['addresses']:
            print('g')
            hostinfo += ('mac地址:' + str(selecteddict['addresses']['mac']) + '\n')
            print('h')
            mac = selecteddict['addresses']['mac']
            print('i')
        print('ii')
        if mac == '':
            hostinfo += ('供应商信息:未知')
        else:
            hostinfo += (mac + ' 供应商信息:' + str(selecteddict['vendor'][mac]))

        print('j')
        self.textEdit_2.setPlainText(hostinfo)
        print('k')
        # 输出操作系统侦测信息
        osinfo = ''
        if 'osmatch' in selecteddict:
            for guess in selecteddict['osmatch']:
                print("k!!")
                osinfo += '---------------\n'
                osinfo += ("osname:" + str(guess['name']) + '\n')
                osinfo += ("accuracy:" + str(guess['accuracy']) + '\n')
                print("kk")
                for next in guess['osclass']:
                    osinfo += ("ostype:" + str(next['type']) + '\n')
                    osinfo += ("osvendor:" + str(next['vendor']) + '\n')
                    osinfo += ("osfamily:" + str(next['osfamily']) + '\n')
                    osinfo += ("osgen:" + str(next['osgen']) + '\n')
                    print("kkk")
        else:
            osinfo = '没有相关信息'
        self.textEdit.setPlainText(osinfo)

    def startportScan(self):

        self.listWidget.clear()
        self.tableWidget.setRowCount(0)
        self.pushButton.setEnabled(False)
        if self.comboBox_2.currentText() == '主机':
            if self.comboBox_3.currentText() == '主机探测(不扫描端口)':
                if self.port_input.text() != '':
                    QMessageBox.information(self, "Over!", "请不要输入端口号！")
                    return
            self.select = 1
            if str(self.port_input.text()) == '':
                self.thread = Scanthread(str(self.ip.text()), None, self.arg[self.comboBox_3.currentText()])
            else:
                self.thread = Scanthread(str(self.ip.text()), str(self.port_input.text()),
                                         self.arg[self.comboBox_3.currentText()])
        elif self.comboBox_2.currentText() == '摄像头':
            self.select = 2
            if self.port_input.text() == '':
                print("ooo")
                temp = self.webcam
            else:
                temp = str(self.webcam + ',' + str(self.port_input.text()))
            self.thread = Scanthread(str(self.ip.text()), temp, self.arg[self.comboBox_3.currentText()])
        else:
            self.select = 3
            if self.port_input.text() == '':
                temp = self.Printer
            else:
                temp = str(self.Printer + ',' + str(self.port_input.text()))
            self.thread = Scanthread(str(self.ip.text()), temp, self.arg[self.comboBox_3.currentText()])

            # self.thread = Scanthread(str(self.ip.text()),str(self.port_input.text()),self.arg[self.comboBox_3.currentText()])

        # 连接信号
        self.thread._signal.connect(self.outputportScan)
        # self.thread._signal.connect(self.outputhost)
        # 开始线程
        self.thread.start()

    def outputportScan(self, msg):
        self.scanResults = msg
        nmScan = msg
        print(nmScan)
        self.pushButton.setEnabled(True)

        """主机输出"""
        # 主机探测(no port)
        self.uphost.setText(nmScan['nmap']['scanstats']['uphosts'])
        self.uphost.setStyleSheet("color:red")
        self.uphost.setStyleSheet("color:gray")
        self.downhost.setText(nmScan['nmap']['scanstats']['downhosts'])
        # temp=''
        # js=json.dumps(nmScan['scan'], sort_keys=False, indent=1, separators=(',', ':'))
        # self.textEdit_2.setPlainText(js)
        # QMessageBox.information(self, "Over!", "扫面结束！")
        i = 0
        if self.select == 1:
            for hostip in self.scanResults['scan'].keys():
                self.listWidget.addItem(hostip)
        else:
            for hostip in self.scanResults['scan'].keys():
                if 'tcp' in nmScan['scan'][hostip]:
                    # print()
                    if (554 in nmScan['scan'][hostip]['tcp'] and nmScan['scan'][hostip]['tcp'][554][
                        'state'] == 'open') or (
                            9100 in nmScan['scan'][hostip]['tcp'] and nmScan['scan'][hostip]['tcp'][9100][
                        'state'] == 'open') or (
                            81 in nmScan['scan'][hostip]['tcp'] and nmScan['scan'][hostip]['tcp'][81][
                        'state'] == 'open'):
                        self.listWidget.addItem(hostip)
        QMessageBox.information(self, "Over!", "扫面结束！")


class Scanthread(QtCore.QThread):  # 子线程扫描
    _signal = pyqtSignal(dict)
    hostnames = ''
    tports = ''
    arg = ''

    def __init__(self, h, p, a):
        self.arg = a
        self.hostnames = h
        self.tports = p
        super(Scanthread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        nmScan = nmap.PortScanner()
        if self.tports:
            temp = nmScan.scan(hosts=self.hostnames, ports=self.tports, arguments=self.arg)
        else:
            temp = nmScan.scan(hosts=self.hostnames, ports=None, arguments=self.arg)
        self._signal.emit(temp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    demo = Ui_scanner()
    demo.setupUi(window)
    window.show()
    sys.exit(app.exec_())
