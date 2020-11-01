from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#导入stu_adds文件  实现添加学生
from stu_adds import *
#导入add_teacher文件 实现添加老师
from add_teacher import *
#导入x_g_stu文件 实现修改学生信息
from x_g_stu import *
#导入chazhao文件 实现查找信息
from chazhao_id import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#导入stu_adds文件  实现添加学生
from stu_adds import *
#导入add_teacher文件 实现添加老师
from add_teacher import *
#导入x_g_stu文件 实现修改学生信息
from x_g_stu import *
#导入chazhao文件 实现查找信息
from tmysql import *
from chazhao_id import *
from zhuwenjian import *
import csv
import os




class Stea_mainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super( Stea_mainWindow,self).__init__()
        self.SetupUi(self)
        #实例化类


    #添加文本框和按钮
    def SetupUi(self,MainWindow):
        self.mianwindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setWindowIcon(QIcon('logo.png'))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        #修改按钮
        self.modify = QtWidgets.QPushButton(self.centralWidget)
        self.modify.setGeometry(QtCore.QRect(280, 300, 75, 23))
        self.modify.setObjectName("pushButton")
        self.modify1 = QtWidgets.QPushButton(self.centralWidget)
        self.modify1.setGeometry(QtCore.QRect(280, 200, 75, 23))
        self.modify1.setObjectName("pushButton")
        #查找按钮
        self.finds = QtWidgets.QPushButton(self.centralWidget)
        self.finds.setGeometry(QtCore.QRect(280, 400, 75, 23))
        self.finds.setObjectName("pushButton")
        # 添加老师按钮
        self.teacehers = QtWidgets.QPushButton(self.centralWidget)
        self.teacehers.setGeometry(QtCore.QRect(280, 500, 75, 23))
        self.teacehers.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(MainWindow)

        #点击按钮调用get_Xg
        self.modify.clicked.connect(self.get_Xg)
        self.modify1.clicked.connect(self.get)
        #点击按钮调用get_find
        self.finds.clicked.connect(self.get_find)
        self.teacehers.clicked.connect(self.get_cj)



    #添加输入框和按钮属性

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.modify.setText(_translate('MainWindow', "导出所有"))
        self.modify1.setText(_translate('MainWindow', "查找"))
        self.finds.setText(_translate('MainWindow', "修改"))
        self.teacehers.setText(_translate('MainWindow', "计算学生成绩"))
        self.modify.setFixedSize(250, 35)
        self.finds.setFixedSize(250, 35)
        self.teacehers.setFixedSize(250, 35)
        self.modify1.setFixedSize(250, 35)


    def get_Xg(self):

            student = select_wheres('student')
            for i in student:
                text = select_where('check_in','stu_id="{}"'.format(i[0]))
                for k in text:
                    if not os.path.exists("student.csv"):
                        with open("student.csv", "w+", newline="") as csvfile:
                            writer = csv.writer(csvfile)
                            # 先写入columns_name
                            writer.writerow(
                                ['姓名','签到状态','课程','时间'])
                            # 写入多行用writerows
                            writer.writerows([[i[2],k[2],k[3],k[4]]])
                        # print(text)
                    else:
                        with open("student.csv", "a+", newline="") as csvfile:
                            writer = csv.writer(csvfile)
                            # 写入多行用writerows
                            writer.writerows([[i[2],k[2],k[3],k[4]]])
            QMessageBox.warning(self,
                                "提示",
                                "以保存student,excel表！",
                                QMessageBox.Yes)

            self.close()


    def get(self):
        self.s = MyWindow()
        self.s.show()





    #打开chazhao文件
    def get_find(self):
        self.xg = TE_MainWindow()
        self.xg.show()

    def get_cj(self):
        self.cg = cj_MainWindow()
        self.cg.show()









class Admin_mainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Admin_mainWindow,self).__init__()
        self.key = 1
        self.SetupUi(self)
        # self.admin = parent
        #实例化类
        self.stu = ADD_MainWindow(self)
        self.xg = STU_MainWindow(self)
        self.teacehers = STEc_MainWindow()
        self.finde = CZ_MainWindow()
        # self.mianwindow = mainwindow

    #添加文本框和按钮
    def SetupUi(self,MainWindow):
        self.mianwindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)

        MainWindow.setWindowIcon(QIcon('logo.png'))

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        # 录入按钮
        self.add = QtWidgets.QPushButton(self.centralWidget)
        self.add.setGeometry(QtCore.QRect(280, 200, 75, 23))
        self.add.setObjectName("pushButton")
        #修改按钮
        self.modify = QtWidgets.QPushButton(self.centralWidget)
        self.modify.setGeometry(QtCore.QRect(280, 300, 75, 23))
        self.modify.setObjectName("pushButton")
        #查找按钮
        # self.finds = QtWidgets.QPushButton(self.centralWidget)
        # self.finds.setGeometry(QtCore.QRect(280, 500, 75, 23))
        # self.finds.setObjectName("pushButton")

        #添加老师按钮
        self.teaceher = QtWidgets.QPushButton(self.centralWidget)
        self.teaceher.setGeometry(QtCore.QRect(280, 400, 75, 23))
        self.teaceher.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        #点击按钮调用get_stu方法
        self.add.clicked.connect(self.get_stu)
        #点击按钮调用get_tec方法
        self.teaceher.clicked.connect(self.get_tec)
        #点击按钮调用get_Xg
        self.modify.clicked.connect(self.get_Xg)
        #点击按钮调用get_find
        # self.finds.clicked.connect(self.get_find)


    #添加输入框和按钮属性
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.add.setText(_translate('MainWindow',"录入"))
        self.modify.setText(_translate('MainWindow', "删除"))
        # self.finds.setText(_translate('MainWindow', "返回"))

        self.teaceher.setText(_translate('MainWindow', "教师注册"))
        self.add.setFixedSize(250, 35)
        self.modify.setFixedSize(250, 35)
        # self.finds.setFixedSize(250, 35)
        self.teaceher.setFixedSize(250, 35)

    #打开stu_adds文件
    def get_stu(self):
        self.stu.show()


    #打开add_teacher
    def get_tec(self):
        self.teacehers.show()


    #打开x_g_stu文件
    def get_Xg(self):
        self.xg.show()


    #打开chazhao文件
    # def get_find(self):
    #     self.mianwindow = hello_mainWindow()
    #     self.mianwindow.show()
    #     self.close()


if __name__ == "__main__":
    app =  QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    myshow = Stea_mainWindow()
    myshow.show()
    sys.exit(app.exec_())



