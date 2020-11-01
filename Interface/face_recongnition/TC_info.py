from PyQt5 import QtCore, QtGui,  QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5. QtWidgets import *
from PyQt5.QtCore import *



class Stu_mainWindow( QtWidgets.QMainWindow):

    def __init__(self):
        super(Stu_mainWindow, self).__init__()
        self.SetupUi(self)

    def SetupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setWindowIcon(QIcon('logo.png'))
        self.centralWM_KQget =  QtWidgets.QWidget(MainWindow)
        self.centralWM_KQget.setObjectName("centralWM_KQget")
        # 姓名
        self.seeKQ =  QtWidgets.QPushButton(self.centralWM_KQget)
        self.seeKQ.setGeometry(QtCore.QRect(280, 200, 75, 23))
        self.seeKQ.setObjectName("pushButton")



        # 学号
        self.M_KQ =  QtWidgets.QPushButton(self.centralWM_KQget)
        self.M_KQ.setGeometry(QtCore.QRect(280, 250, 75, 23))
        self.M_KQ.setObjectName("pushButton")
        # 班级
        self.M_PWD =  QtWidgets.QPushButton(self.centralWM_KQget)
        self.M_PWD.setGeometry(QtCore.QRect(280, 400, 75, 23))
        self.M_PWD.setObjectName("pushButton")
        # 签到
        self.F_KQ =  QtWidgets.QPushButton(self.centralWM_KQget)
        self.F_KQ.setGeometry(QtCore.QRect(280, 350, 75, 23))
        self.F_KQ.setObjectName("pushButton")
        # 照片
        self.JS_KQ =  QtWidgets.QPushButton(self.centralWM_KQget)
        self.JS_KQ.setGeometry(QtCore.QRect(280, 300, 75, 23))
        self.JS_KQ.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralWM_KQget)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.seeKQ.setText(_translate('MainWindow', "查看考勤信息"))
        self.M_KQ.setText(_translate('MainWindow', "修改考勤信息"))
        self.F_KQ.setText(_translate('MainWindow', "查询学生信息"))
        self.JS_KQ.setText(_translate('MainWindow', "计算考勤成绩"))
        self.M_PWD.setText(_translate('MainWindow', "修改密码"))
        self.seeKQ.setFixedSize(250, 35)
        self.M_KQ.setFixedSize(250, 35)
        self.JS_KQ.setFixedSize(250, 35)
        self.F_KQ.setFixedSize(250, 35)
        self.M_PWD.setFixedSize(250, 35)


if __name__ == "__main__":
    import sys

    app =  QtWidgets.QApplication(sys.argv)
    MainWindow =  QtWidgets.QMainWindow()
    ui = Stu_mainWindow()

    ui.SetupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())