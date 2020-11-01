# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '显示.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

#查找学生信息
from PyQt5 import QtCore, QtGui, QtWidgets
from insert_db import *
#实现功能:根据学生学号来获取学生信息 并用QLabel文字来显示出来
class XS_MainWindow(QtWidgets.QMainWindow):

    def __init__(self,key):
        self.key = key
        super(XS_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 600)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 50, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 100, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 140, 72, 15))
        self.label_3.setObjectName("label_3")
        #设置可变值来显示学生姓名
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 60, 72, 15))
        self.label_4.setObjectName("label_4")
        #设置可变值来显示学生学号
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 100, 72, 15))
        self.label_5.setObjectName("label_5")
        #设置可变值来显示学生班级
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 140, 90, 25))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "课程："))
        self.label_2.setText(_translate("MainWindow", "状态："))
        self.label_3.setText(_translate("MainWindow", "时间："))

        self.label_4.setText(_translate("MainWindow", str(self.key[3])))
        self.label_5.setText(_translate("MainWindow", str(self.key[2])))
        self.label_6.setText(_translate("MainWindow", str(self.key[4])))

