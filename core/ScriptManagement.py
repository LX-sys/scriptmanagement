# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScriptManagement.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence

from core.table import TableRight,TableBottom
from cardframe import CardFrame


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
        self.resize(1300, 800)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet('''
QWidget{
background-color: rgb(222, 222, 222);
}
QLabel,QLineEdit{
	color: rgb(0, 0, 0);
	font: 12pt "黑体";
}
QLineEdit{
	color: rgb(0, 85, 255);
}
QPushButton{
	color: rgb(84, 84, 84);
	background-color: rgb(0, 255, 0);
}
        ''')
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

        # 右下
        self.right_Tabwidget = TableRight(self.splitter_h)
        self.crad_affiliated = TableBottom(self.splitter_v)

        self.gridLayout_2.addWidget(self.splitter_v, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_name = QtWidgets.QLabel(self.page_2)
        self.label_name.setGeometry(QtCore.QRect(525, 380, 51, 21))
        self.label_name.setStyleSheet('''
QLabel{
	color: rgb(80, 80, 80);
	font: 10pt "微软雅黑";
}
        ''')
        self.label_name.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_name.setObjectName("label_name")
        self.lineEdit_name = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_name.setGeometry(QtCore.QRect(530, 410, 200, 40))
        self.lineEdit_name.setStyleSheet('''
QLineEdit{
color: rgb(0, 0, 0);
border:3px solid rgb(0, 0, 0);
border-top:none;
border-left:none;
border-right:none;
font: 14pt "黑体";
}
QLineEdit:focus{
	border-bottom-color:rgb(0, 0, 127);
}
        ''')
        self.lineEdit_name.setText("")
        self.lineEdit_name.setPlaceholderText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_pwd = QtWidgets.QLabel(self.page_2)
        self.label_pwd.setGeometry(QtCore.QRect(525, 470, 51, 21))
        self.label_pwd.setStyleSheet('''
QLabel{
	color: rgb(80, 80, 80);
	font: 10pt "微软雅黑";
}
        ''')
        self.label_pwd.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_pwd.setObjectName("label_pwd")
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_pwd.setGeometry(QtCore.QRect(530, 500, 200, 40))
        self.lineEdit_pwd.setStyleSheet('''
QLineEdit{
color: rgb(0, 0, 0);
border:3px solid rgb(0, 0, 0);
border-top:none;
border-left:none;
border-right:none;
font: 14pt "黑体";
}
QLineEdit:focus{
	border-bottom-color:rgb(0, 0, 127);
}
        ''')
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.btn_login = QtWidgets.QPushButton(self.page_2)
        self.btn_login.setGeometry(QtCore.QRect(470, 580, 111, 41))
        self.btn_login.setStyleSheet('''
QPushButton{
border:1px solid rgb(255, 255, 255);
border-radius:4px;
color: rgb(43, 43, 43);
background-color:rgb(0, 255, 127);
font: 13pt "华文琥珀";
}
QPushButton:pressed{
background-color:rgb(0, 227, 110);
}
        ''')
        self.btn_login.setObjectName("btn_login")
        self.btn_registered = QtWidgets.QPushButton(self.page_2)
        self.btn_registered.setGeometry(QtCore.QRect(700, 580, 111, 41))
        self.btn_registered.setStyleSheet('''
QPushButton{
border:1px solid rgb(255, 255, 255);
border-radius:4px;
color:rgb(189, 189, 189);
background-color:rgb(22, 22, 22);
font: 13pt "华文琥珀";
}
QPushButton:pressed{
background-color:rgb(0, 0, 0);
}
        ''')
        self.btn_registered.setObjectName("btn_registered")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(300, 100, 661, 81))
        self.label.setStyleSheet('''
QLabel{
	color: rgb(0, 0, 0);
	font: 40pt "黑体";
}
        ''')
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(790, 110, 61, 16))
        self.label_2.setStyleSheet('''
QLabel{
	color:rgb(107, 107, 107);
	font: 11pt "微软雅黑";
}
        ''')
        self.label_2.setObjectName("label_2")
        self.label_respace_name = QtWidgets.QLabel(self.page_2)
        self.label_respace_name.setGeometry(QtCore.QRect(740, 410, 200, 40))
        self.label_respace_name.setText("")
        self.label_respace_name.setObjectName("label_respace_name")
        self.label_respace_pwd = QtWidgets.QLabel(self.page_2)
        self.label_respace_pwd.setGeometry(QtCore.QRect(740, 500, 200, 40))
        self.label_respace_pwd.setText("")
        self.label_respace_pwd.setObjectName("label_respace_pwd")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
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
        # self.splitter_h.setSizes([int(self.width() * 0.99), int(self.width() * 0.01)])
        self.crad_affiliated.splitterChange(self.splitter_v,int(self.width() * 0.7), int(self.width() * 0.3))

    def rightSpreadEvent(self):
        # self.splitter_h.setSizes([int(self.width() * 0.99), int(self.width() * 0.01)])
        self.right_Tabwidget.splitterChange(self.splitter_h, int(self.width() * 0.7), int(self.width() * 0.3))

    # 事件
    def myEvent(self):
        self.crad_affiliated.clickTab(self.bottomSpreadEvent)
        self.right_Tabwidget.clickTab(self.rightSpreadEvent)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label_name.setText(_translate("self", "姓名"))
        self.label_pwd.setText(_translate("self", "密码"))
        self.btn_login.setText(_translate("self", "登录"))
        self.btn_registered.setText(_translate("self", "注册"))
        self.label.setText(_translate("self", "脚本管理系统"))
        self.label_2.setText(_translate("self", "@ LX"))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = ScriptManagement()
    win.show()

    sys.exit(app.exec_())
    