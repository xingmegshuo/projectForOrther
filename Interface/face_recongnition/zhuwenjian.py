from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from face import *
from x_g_stu_two import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from create_table import create


class hello_mainWindow(QtWidgets.QMainWindow):


    def __init__(self):
        super(hello_mainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)



    def setupUi(self, MainWindow):
        self.mainwindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setWindowIcon(QIcon('logo.png'))

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 400, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_teacher = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_teacher.setGeometry(QtCore.QRect(280, 500, 75, 23))
        self.pushButton_teacher.setObjectName("pushButton")
        self.pushButton_ai = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_ai .setGeometry(QtCore.QRect(280, 600, 75, 23))
        self.pushButton_ai .setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "管理员登录"))
        self.pushButton_teacher.setText(_translate("MainWindow", "教师登录"))
        self.pushButton_ai.setText(_translate("MainWindow", "学生签到"))
        self.pushButton.setFixedSize(250, 35)  # 设置按钮大小
        self.pushButton_teacher.setFixedSize(250, 35)  # 设置按钮大小
        self.pushButton_ai.setFixedSize(250, 35)  # 设置按钮大小
        qt_button = '''QPushButton{
                    color: #fff;
                    background-color: #ff6fa2;
                    border-color: #ff6fa2;
                    height: 32px;
                    border-radius: 4px;
            }'''
        self.pushButton.setStyleSheet(qt_button)
        self.pushButton_teacher.setStyleSheet(qt_button)
        self.pushButton_ai.setStyleSheet(qt_button)
        self.pushButton.clicked.connect(self.word_get)
        self.pushButton_ai.clicked.connect(self.face_r)
        self.pushButton_teacher.clicked.connect(self.ste_get)

    def word_get(self):
        self.ua = Face_MainWindow(1)
        self.ua.show()
        self.mainwindow.hide()

    def ste_get(self):
        self.ua = Face_MainWindow(2)
        self.ua.show()
        self.mainwindow.hide()


    def face_r(self):
        self.qd = QD_MainWindow()
        self.qd.show()


if __name__ == '__main__':
    create()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = hello_mainWindow()
    MainWindow.show()
    ui.setupUi(MainWindow)
    sys.exit(app.exec_())