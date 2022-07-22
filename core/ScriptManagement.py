# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScriptManagement.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction,QPushButton
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence

from core.table import TableRight,TableBottom
from core.cardframe.cardframe import CardFrame



class ScriptManagement(QMainWindow):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.setupUi()
        self.myMenu()
        self.myShortcuts()
        self.myEvent()

        self.Init()
    
    def setupUi(self):
        self.setObjectName("self")
        self.resize(1208, 781)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("QWidget{\n"
"/*background-color: rgb(222, 222, 222);*/\n"
"    border:none;\n"
"    background-color: qlineargradient(spread:pad, x1:0.023, y1:0.023, x2:1, y2:1, stop:0 rgba(130, 247, 255, 255), stop:1 rgba(190, 191, 221, 255));\n"
"}\n"
"QLabel,QLineEdit{\n"
"background-color:none;\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"黑体\";\n"
"}\n"
"QLineEdit{\n"
"    background-color: qlineargradient(spread:pad, x1:0.295955, y1:0.471, x2:0.705, y2:0.778, stop:0.488636 rgba(34, 178, 221, 5));\n"
"    color: rgb(0, 85, 255);\n"
"}\n"
"QPushButton{\n"
"    color: rgb(84, 84, 84);\n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_v = QtWidgets.QSplitter(self.page)
        self.splitter_v.setLineWidth(0)
        self.splitter_v.setOrientation(QtCore.Qt.Vertical)
        self.splitter_v.setHandleWidth(0)
        self.splitter_v.setChildrenCollapsible(False)
        self.splitter_v.setObjectName("splitter_v")
        self.splitter_h = QtWidgets.QSplitter(self.splitter_v)
        self.splitter_h.setLineWidth(0)
        self.splitter_h.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_h.setHandleWidth(0)
        self.splitter_h.setChildrenCollapsible(False)
        self.splitter_h.setObjectName("splitter_h")
        self.card_body = CardFrame(self.splitter_h)
        print("---")

        # 修改
        self.card_body.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.528136, x2:1, y2:0.517, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(187, 187, 187, 255));")
        self.right_Tabwidget = TableRight(self.splitter_h)
        self.crad_affiliated = TableBottom(self.splitter_v)


        self.gridLayout_2.addWidget(self.splitter_v, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(self.page_2)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 121))
        self.widget.setStyleSheet("QWidget{\n"
"    background-color: qlineargradient(spread:pad, x1:0.295955, y1:0.471, x2:0.705, y2:0.778, stop:0.488636 rgba(34, 178, 221, 5));\n"
"}")
        self.widget.setObjectName("widget")
        self.label_j2 = QtWidgets.QLabel(self.widget)
        self.label_j2.setGeometry(QtCore.QRect(17, 16, 60, 60))
        self.label_j2.setStyleSheet("QLabel{\n"
"font:50pt \"黑体\";\n"
"background-color: none;\n"
"color:qlineargradient(spread:pad, x1:0.295955, y1:0.471, x2:0.54, y2:0.619273, stop:0.488636 rgba(125, 60, 221, 77))\n"
"}\n"
"")
        self.label_j2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_j2.setObjectName("label_j2")
        self.label_m1 = QtWidgets.QLabel(self.widget)
        self.label_m1.setGeometry(QtCore.QRect(106, 11, 60, 60))
        self.label_m1.setStyleSheet("QLabel{\n"
"font:50pt \"黑体\";\n"
"background-color: none;\n"
"    color:qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"}\n"
"")
        self.label_m1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_m1.setObjectName("label_m1")
        self.label_s1 = QtWidgets.QLabel(self.widget)
        self.label_s1.setGeometry(QtCore.QRect(60, 40, 60, 60))
        self.label_s1.setStyleSheet("QLabel{\n"
"font:50pt \"黑体\";\n"
"background-color: none;\n"
"/*color: rgb(170, 255, 255);*/\n"
"    color:qlineargradient(spread:pad, x1:0.295955, y1:0.471, x2:0.54, y2:0.619273, stop:0.488636 rgba(34, 178, 221, 216));\n"
"}\n"
"")
        self.label_s1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_s1.setObjectName("label_s1")
        self.label_j1 = QtWidgets.QLabel(self.widget)
        self.label_j1.setGeometry(QtCore.QRect(20, 20, 60, 60))
        self.label_j1.setStyleSheet("QLabel{\n"
"font:50pt \"黑体\";\n"
"background-color: none;\n"
"color:rgb(27, 27, 27);\n"
"}\n"
"")
        self.label_j1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_j1.setObjectName("label_j1")
        self.label_s2 = QtWidgets.QLabel(self.widget)
        self.label_s2.setGeometry(QtCore.QRect(54, 40, 60, 60))
        self.label_s2.setStyleSheet("QLabel{\n"
"font:50pt \"黑体\";\n"
"background-color: none;\n"
"/*color: rgb(170, 255, 255);*/\n"
"    color:rgb(67, 67, 67);\n"
"}\n"
"")
        self.label_s2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_s2.setObjectName("label_s2")
        self.label_m2 = QtWidgets.QLabel(self.widget)
        self.label_m2.setGeometry(QtCore.QRect(110, 10, 60, 60))
        self.label_m2.setStyleSheet("QLabel{\n"
"font:50pt \"黑体\";\n"
"background-color: none;\n"
"    color:qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"}\n"
"")
        self.label_m2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_m2.setObjectName("label_m2")
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.page_2)
        self.widget_2.setStyleSheet("QWidget{\n"
"    background-color: qlineargradient(spread:pad, x1:0.295955, y1:0.471, x2:0.705, y2:0.778, stop:0.488636 rgba(34, 178, 221, 5));\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.label_respace_pwd = QtWidgets.QLabel(self.widget_2)
        self.label_respace_pwd.setGeometry(QtCore.QRect(690, 290, 200, 40))
        self.label_respace_pwd.setStyleSheet("")
        self.label_respace_pwd.setText("")
        self.label_respace_pwd.setObjectName("label_respace_pwd")
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_name.setGeometry(QtCore.QRect(480, 200, 200, 40))
        self.lineEdit_name.setStyleSheet("QLineEdit{\n"
"color: rgb(0, 0, 0);\n"
"border:3px solid rgb(0, 0, 0);\n"
"border-top:none;\n"
"border-left:none;\n"
"border-right:none;\n"
"font: 14pt \"黑体\";\n"
"}\n"
"QLineEdit:focus{\n"
"    border-bottom-color:rgb(0, 0, 127);\n"
"}")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setPlaceholderText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_pwd = QtWidgets.QLabel(self.widget_2)
        self.label_pwd.setGeometry(QtCore.QRect(475, 260, 51, 21))
        self.label_pwd.setStyleSheet("QLabel{\n"
"    color: rgb(80, 80, 80);\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label_pwd.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_pwd.setObjectName("label_pwd")
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_pwd.setGeometry(QtCore.QRect(480, 290, 200, 40))
        self.lineEdit_pwd.setStyleSheet("QLineEdit{\n"
"color: rgb(0, 0, 0);\n"
"border:3px solid rgb(0, 0, 0);\n"
"border-top:none;\n"
"border-left:none;\n"
"border-right:none;\n"
"font: 14pt \"黑体\";\n"
"}\n"
"QLineEdit:focus{\n"
"    border-bottom-color:rgb(0, 0, 127);\n"
"}")
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.label_name = QtWidgets.QLabel(self.widget_2)
        self.label_name.setGeometry(QtCore.QRect(475, 170, 51, 21))
        self.label_name.setStyleSheet("QLabel{\n"
"    color: rgb(80, 80, 80);\n"
"    font: 10pt \"微软雅黑\";\n"
"}")
        self.label_name.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_name.setObjectName("label_name")
        self.label_respace_name = QtWidgets.QLabel(self.widget_2)
        self.label_respace_name.setGeometry(QtCore.QRect(690, 200, 200, 40))
        self.label_respace_name.setStyleSheet("")
        self.label_respace_name.setText("")
        self.label_respace_name.setObjectName("label_respace_name")
        self.btn_login = QtWidgets.QPushButton(self.widget_2)
        self.btn_login.setGeometry(QtCore.QRect(370, 390, 111, 41))
        self.btn_login.setStyleSheet("QPushButton{\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-radius:4px;\n"
"color: rgb(43, 43, 43);\n"
"background-color:rgb(0, 255, 127);\n"
"font: 13pt \"华文琥珀\";\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(0, 227, 110);\n"
"}")
        self.btn_login.setObjectName("btn_login")
        self.btn_registered = QtWidgets.QPushButton(self.widget_2)
        self.btn_registered.setGeometry(QtCore.QRect(680, 390, 111, 41))
        self.btn_registered.setStyleSheet("QPushButton{\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-radius:4px;\n"
"color:rgb(189, 189, 189);\n"
"background-color:rgb(22, 22, 22);\n"
"font: 13pt \"华文琥珀\";\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(0, 0, 0);\n"
"}")
        self.btn_registered.setObjectName("btn_registered")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(240, 10, 661, 81))
        self.label.setStyleSheet("QLabel{\n"
"    color: rgb(47, 47, 47);\n"
"    font: 60pt \"黑体\";\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(800, 10, 61, 16))
        self.label_2.setStyleSheet("QLabel{\n"
"    color:rgb(107, 107, 107);\n"
"    font: 11pt \"微软雅黑\";\n"
"}")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1208, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(self)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(self)
        self.action_2.setObjectName("action_2")
        self.action_4 = QtWidgets.QAction(self)
        self.action_4.setObjectName("action_4")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_4)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi()
        self.stackedWidget.setCurrentIndex(0)
        self.right_Tabwidget.setCurrentIndex(0)
        self.crad_affiliated.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)


    def Init(self):
        self.splitter_h.setSizes([int(self.width() * 0.99), int(self.width() * 0.01)])
        self.splitter_v.setSizes([int(self.width() * 0.99), int(self.width() * 0.01)])

    # 菜单
    def myMenu(self):
        self.menubar = QMenuBar(self)
        self.menu = QMenu(self.menubar)
        self.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu.menuAction())
        self.menu.setTitle("文件")

        self.about = QMenu(self.menubar)
        self.setMenuBar(self.menubar)
        self.menubar.addAction(self.about.menuAction())
        self.about.setTitle("关于")

        # --------------文件------------------
        self.newjs = QAction("新建脚本",self)
        self.menu.addAction(self.newjs)

        self.updatejs = QAction("修改脚本", self)
        self.menu.addAction(self.updatejs)

        self.setting = QAction("设置", self)
        self.menu.addAction(self.setting)

        # ----------关于-------------------
        self.info_js = QAction("脚本管理系统",self)
        self.about.addAction(self.info_js)

    # 搜索事件
    def find_Event(self):
        print("搜索")

    # 快捷键
    def myShortcuts(self):
        QShortcut(QKeySequence(self.tr("Ctrl+F")), self, self.find_Event)

    # 底部tab展开事件
    def bottomSpreadEvent(self):
        self.crad_affiliated.splitterChange(self.splitter_v,int(self.width() * 0.7), int(self.width() * 0.3))

    def rightSpreadEvent(self):
        self.right_Tabwidget.splitterChange(self.splitter_h, int(self.width() * 0.7), int(self.width() * 0.3))

    # 事件
    def myEvent(self):
        self.crad_affiliated.clickTab(self.bottomSpreadEvent)
        self.right_Tabwidget.clickTab(self.rightSpreadEvent)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label_j2.setText(_translate("self", "J"))
        self.label_m1.setText(_translate("self", "M"))
        self.label_s1.setText(_translate("self", "S"))
        self.label_j1.setText(_translate("self", "J"))
        self.label_s2.setText(_translate("self", "S"))
        self.label_m2.setText(_translate("self", "M"))
        self.label_pwd.setText(_translate("self", "密码"))
        self.label_name.setText(_translate("self", "姓名"))
        self.btn_login.setText(_translate("self", "登录"))
        self.btn_registered.setText(_translate("self", "注册"))
        self.label.setText(_translate("self", "脚本管理系统"))
        self.label_2.setText(_translate("self", "@ LX"))
        self.menu.setTitle(_translate("self", "文件"))
        self.action.setText(_translate("self", "新建脚本"))
        self.action_2.setText(_translate("self", "修改脚本"))
        self.action_4.setText(_translate("self", "设置"))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = ScriptManagement()
    win.show()

    sys.exit(app.exec_())
    