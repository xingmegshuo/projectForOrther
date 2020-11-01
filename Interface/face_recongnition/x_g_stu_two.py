# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stu_adds.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
from insert_db import *
from face_re import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class QD_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(QD_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 600)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 90, 281, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 290, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(self.face_r)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "签到页面"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入课程"))

        self.pushButton_2.setText(_translate("MainWindow", "提交"))


    def face_r(self):
        # try:
        data = select_all('student')
        data = {i[2]:i[4].lower() for i in data}
        stu_has = list(set(identification(data)))
        print(data)
        for i in data.keys():
            stu_id = select_where('student',"number='{}'".format(i))[0][0]
            if i in stu_has:
                print(i,stu_has)
                insert_data('check_in',{'stu_id':stu_id,'status':'签到成功','classname':self.lineEdit.text()})
            else:
                insert_data('check_in',{'stu_id':stu_id,'status':'未签到','classname':self.lineEdit.text()})


        # except:
        #      QMessageBox.warning(self,
        #             "警告",
        #             "没有内容！",
        #             QMessageBox.Yes)





