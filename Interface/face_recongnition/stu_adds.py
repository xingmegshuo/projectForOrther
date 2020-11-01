# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stu_adds.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from insert_db import *
from tijiaocg import *
import csv
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from grade import *

class ADD_MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None, mainwindow=None):
        super(ADD_MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        # self.Ui = Ui_MainWindow()
        # self.tijiao = TJ_MainWindow(parent, self)


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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 290, 101, 31))
        self.pushButton.setObjectName("pushButton")
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
        self.pushButton.clicked.connect(self.loadFile)
        self.pushButton_2.clicked.connect(self.saves)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        print('---------------',dir(_translate))
        MainWindow.setWindowTitle(_translate("MainWindow", "录入学生信息"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "姓名"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "学号"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "班级"))
        self.pushButton.setText(_translate("MainWindow", "提交图片"))
        self.pushButton_2.setText(_translate("MainWindow", "提交"))

    def loadFile(self):
            print("load--file")
            # QFileDialog就是系统对话框的那个类第一个参数是上下文，第二个参数是弹框的名字，第三个参数是开始打开的路径，第四个参数是需要的格式
            fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'c:\\', 'Image files(*.jpg *.gif *.png)')
            # self.label.setPixmap(QPixmap(fname))
            try:
                self.fname = fname
            except:
                QMessageBox.warning(self,
                                    "警告",
                                    "用户名或密码错误！",
                                    QMessageBox.Yes)
                self.lineEdit.setFocus()
    def saves(self):
        try:
            data = {
                'name': self.lineEdit.text(),
                'number':self.lineEdit_2.text(),
                'classnumber':self.lineEdit_3.text(),
                'picture':self.fname

            }
            insert_data('student',data)

            self.close()
        except:
            QMessageBox.warning(self,
                                "警告",
                                "没有图片！",
                                QMessageBox.Yes)
            self.lineEdit.setFocus()



class TCXG_MainWindow(QtWidgets.QMainWindow):

    def __init__(self,key):
        self.key = key
        super(TCXG_MainWindow, self).__init__()
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

        MainWindow.setWindowTitle(_translate("MainWindow", "录入学生信息"))
        print(self.key)
        self.lineEdit.setPlaceholderText(_translate("MainWindow", str(self.key[1])))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", str(self.key[2])))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", str(self.key[3])))

        self.pushButton_2.setText(_translate("MainWindow", "提交"))



    def saves(self):
        print(self.key)
        print(self.lineEdit_2.text())
        change('check_in','status="{}"'.format(self.lineEdit_2.text()),"id='{}'".format(self.key[0]))
        self.close()


class cj_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(cj_MainWindow, self).__init__()
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
        # self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        # self.lineEdit.setGeometry(QtCore.QRect(270, 90, 281, 31))
        # self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 160, 281, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 240, 281, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 310, 281, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 390, 111, 31))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "计算成绩信息"))
        # self.lineEdit.setPlaceholderText(_translate("MainWindow", "学号"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "课时"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "课程"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "成绩"))

        self.pushButton_2.setText(_translate("MainWindow", "提交"))



    def saves(self):
        try:
            # number = self.lineEdit.text()
            sc = select_wheres('student')

            for id in sc:
                print(id)
                nums = len(select_where('check_in',"classname='{}' and stu_id='{}' and status='{}'".format(self.lineEdit_3.text(),id[0],'签到成功')))
                s = int(self.lineEdit_4.text())/int(self.lineEdit_2.text())*nums
                if not os.path.exists("{}.csv".format(self.lineEdit_3.text())):
                    with open("{}.csv".format(self.lineEdit_3.text()), "w+", newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        # 先写入columns_name
                        writer.writerow(
                            ['姓名', '课程', '成绩'])
                        # 写入多行用writerows
                        writer.writerows([[id[1],self.lineEdit_3.text(),s]])
                    # print(text)
                else:
                    with open("{}.csv".format(self.lineEdit_3.text()), "a+", newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        # 写入多行用writerows
                        writer.writerows([[id[1],self.lineEdit_3.text(),s]])
            self.close()
        except:
            QMessageBox.warning(self,
                                "警告",
                                "提交错误！",
                                QMessageBox.Yes)
            self.lineEdit.setFocus()












