# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xiugai_stu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#修改窗口


from PyQt5 import QtCore, QtGui, QtWidgets
from x_g_stu_two import *
#调用提交窗口
from tijiaocg import  *
#实现功能：传入学生学号根据学号提交 来获取学生信息
from insert_db import *
from Xs import *
from stu_adds import *

class STU_MainWindow(QtWidgets.QMainWindow):

    def __init__(self,parent=None,mainwindow=None):
        super(STU_MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        # self.Ui = Ui_MainWindow()
        self.tijiao = TJ_MainWindow(parent,self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(979, 697)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        #输入学生的学号文本框
        self.lineEdit.setGeometry(QtCore.QRect(290, 90, 391, 41))
        self.lineEdit.setObjectName("lineEdit")
        #点击提交 按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 200, 151, 51))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 979, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #调用函数来判断是否有这个学号
        self.pushButton.clicked.connect(self.click_tijiao)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入要删除的学生学号"))
        self.pushButton.setText(_translate("MainWindow", "提交"))

    #判断学生学号函数
    def click_tijiao(self):
        data = self.lineEdit.text()
        print(data)

        if self.lineEdit.text() == data:
            id = select_where('student',"number='{}'".format(data))[0][0]
            delete_from('check_in','stu_id="{}"'.format(id))
            delete_from('student',"id='{}'".format(id))
            # self.Ui.show()
            self.tijiao.show()


class TEA_MainWindow(QtWidgets.QMainWindow):

    def __init__(self,parent=None,mainwindow=None):
        super(TEA_MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        # self.Ui = Ui_MainWindow()
        self.tijiao = TJ_MainWindow(parent,self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(979, 697)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        #输入学生的学号文本框
        self.lineEdit.setGeometry(QtCore.QRect(290, 90, 391, 41))
        self.lineEdit.setObjectName("lineEdit")
        #点击提交 按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 200, 151, 51))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 979, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #调用函数来判断是否有这个学号
        self.pushButton.clicked.connect(self.click_tijiao)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入要查找的学生学号"))
        self.pushButton.setText(_translate("MainWindow", "提交"))

    #判断学生学号函数
    def click_tijiao(self):
        number = self.lineEdit.text()
        try:
            sc = select_where('student','number="{}"'.format(number))[0][0]

            text = select_where('check_in','stu_id="{}"'.format(sc))[0]
            self.xs = XS_MainWindow(text)
            self.xs.show()
            self.close()
        except:
            QMessageBox.warning(self,
                                "警告",
                                "没有这个学号！",
                                QMessageBox.Yes)
            self.lineEdit.setFocus()


class TE_MainWindow(QtWidgets.QMainWindow):

    def __init__(self,parent=None,mainwindow=None):
        super(TE_MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        # self.Ui = Ui_MainWindow()
        self.tijiao = TJ_MainWindow(parent,self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(979, 697)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        #输入学生的学号文本框
        self.lineEdit.setGeometry(QtCore.QRect(290, 90, 391, 41))
        self.lineEdit.setObjectName("lineEdit")
        #点击提交 按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 200, 151, 51))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 979, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #调用函数来判断是否有这个学号
        self.pushButton.clicked.connect(self.click_tijiao)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入要修改的学生学号"))
        self.pushButton.setText(_translate("MainWindow", "提交"))

    #判断学生学号函数
    def click_tijiao(self):
        number = self.lineEdit.text()
        try:
            sc = select_where('student','number="{}"'.format(number))[0][0]

            text = select_where('check_in','stu_id="{}" and status="{}"'.format(sc,'未签到'))[0]
            self.xs = TCXG_MainWindow(text)

            self.xs.show()
            self.close()
        except:
            QMessageBox.warning(self,
                                "警告",
                                "没有这个学号！",
                                QMessageBox.Yes)
            self.lineEdit.setFocus()













