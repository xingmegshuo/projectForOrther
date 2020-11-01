
#添加教师信息
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from insert_db import *


class STEc_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(STEc_MainWindow, self).__init__()
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
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 160, 281, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 240, 281, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")

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

        self.pushButton_2.clicked.connect(self.saves)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        print('---------------', dir(_translate))
        MainWindow.setWindowTitle(_translate("MainWindow", "录入老师信息"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "姓名"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "账号"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "密码"))

        self.pushButton_2.setText(_translate("MainWindow", "提交"))



    def saves(self):
        data = {

            'account': self.lineEdit_2.text(),
            'password': make_password(self.lineEdit_3.text()),


        }
        insert_data('user', data)

        self.close()










