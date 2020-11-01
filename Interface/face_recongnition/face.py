from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from admin import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from tool import MySQL



class Face_MainWindow(QtWidgets.QMainWindow):

    def __init__(self,key):
        self.key = key
        super(Face_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        # self.mainwindow = mainwindow



    def setupUi(self, MainWindow):
        self.mianwindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setWindowIcon(QIcon('logo.png'))
        MainWindow.setStyleSheet("background-image:url(Background.jpg)")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(900, 385, 250, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(900, 450, 250, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(850,  385, 30, 24))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(850,  450, 30, 24))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(900, 500, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        if self.key == 1:
            self.pushButton.clicked.connect(self.word_get)
        else:
            self.pushButton.clicked.connect(self.ste_get)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "登录页面"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入帐号"))
        self.lineEdit.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.lineEdit_2.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.label.setText(_translate("MainWindow", "帐号"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton.setFixedSize(250, 35)
        self.pushButton.setStyleSheet(
            '''QPushButton{
                    color: #fff;
                    background-color: #ff6fa2;
                    border-color: #ff6fa2;
                    height: 32px;
                    border-radius: 4px;
            }''')




    def word_get(self):

        self.admin = Admin_mainWindow()
        MainWindow = QtWidgets.QMainWindow()
        con = MySQL()
        sql = '''select * from user'''
        con.query(sql)
        data = con.show()
        user = {i[1]:i[2] for i in data}
        login_user = self.lineEdit.text()
        login_password = make_password(self.lineEdit_2.text())
        # print(login_password)
        if login_password == user.get(login_user):
            self.admin.show()
            self.mianwindow.hide()

        else:
            QMessageBox.warning(self,
                    "警告",
                    "用户名或密码错误！",
                    QMessageBox.Yes)
            self.lineEdit.setFocus()

    def ste_get(self):
        self.admin = Stea_mainWindow()
        MainWindow = QtWidgets.QMainWindow()
        con = MySQL()
        sql = '''select * from user'''
        con.query(sql)
        data = con.show()
        user = {i[1]:i[2] for i in data}
        login_user = self.lineEdit.text()
        login_password = make_password(self.lineEdit_2.text())
        if login_password == user.get(login_user):
            self.admin.show()
            self.mianwindow.hide()

        else:
            QMessageBox.warning(self,
                    "警告",
                    "用户名或密码错误！",
                    QMessageBox.Yes)
            self.lineEdit.setFocus()


