# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fanhui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#提交页面  每次我想要保存数据时候都会出现这个页面 显示提交成功

from PyQt5 import QtCore, QtGui, QtWidgets
#主页面调用  有一个掉用的函数点击返回主页面
from admin import *

class TJ_MainWindow(QtWidgets.QMainWindow):

    def __init__(self,parent=None,mainwindow=None):
        super(TJ_MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.admin = parent
        self.mainwindow=mainwindow

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 239)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.get_admin)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "提交成功"))
        self.pushButton.setText(_translate("MainWindow", "返回主页面"))

    #调用这个函数就会报错
    def get_admin(self):
        print(self.admin)
        self.admin.show()
        self.mainwindow.hide()





