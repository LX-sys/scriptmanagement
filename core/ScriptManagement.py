# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScriptManagement.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from core.utility import time,sys


from core.utility import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QtCore,
    QtWidgets,
    QShortcut,
    QKeySequence
)

from core.utility import Mysql_PersonalInfo

from core.register import Register
from core.table import TableRight,TableBottom
from core.cardframe.cardframe import CardFrame
from core.menusys.menuSys import MenuSys
from core.card import Card
from core.newJS import NewJS
from core.updateJS import UpdateJS
from core.token import JWT,QtJWT
from core.jstemplate.JStemplate_tree import JSTemplate
from core.viewJS import ViewJS
from core.py2_py3.py2_py3 import Py2Py3
from core.login_info import LoginInfo


# JSM
class ScriptManagement(QMainWindow):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.__info = None
        self.__login_info = LoginInfo()
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
        self.stackedWidget.setStyleSheet('''
QWidget{
border:none;
background-color: qlineargradient(spread:pad, x1:0.484, y1:1, x2:0.488, y2:0, stop:0 rgba(43, 192, 228, 253), stop:1 rgba(234, 236, 198, 255));
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
        # ????????????
        self.card_body = CardFrame(self.splitter_h)

        # ??????
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
"font:50pt \"??????\";\n"
"background-color: none;\n"
"color:qlineargradient(spread:pad, x1:0.295955, y1:0.471, x2:0.54, y2:0.619273, stop:0.488636 rgba(125, 60, 221, 77))\n"
"}\n"
"")
        self.label_j2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_j2.setObjectName("label_j2")
        self.label_m1 = QtWidgets.QLabel(self.widget)
        self.label_m1.setGeometry(QtCore.QRect(106, 11, 60, 60))
        self.label_m1.setStyleSheet("QLabel{\n"
"font:50pt \"??????\";\n"
"background-color: none;\n"
"    color:qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"}\n"
"")
        self.label_m1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_m1.setObjectName("label_m1")
        self.label_s1 = QtWidgets.QLabel(self.widget)
        self.label_s1.setGeometry(QtCore.QRect(60, 40, 60, 60))
        self.label_s1.setStyleSheet("QLabel{\n"
"font:50pt \"??????\";\n"
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
"font:50pt \"??????\";\n"
"background-color: none;\n"
"color:rgb(27, 27, 27);\n"
"}\n"
"")
        self.label_j1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_j1.setObjectName("label_j1")
        self.label_s2 = QtWidgets.QLabel(self.widget)
        self.label_s2.setGeometry(QtCore.QRect(54, 40, 60, 60))
        self.label_s2.setStyleSheet("QLabel{\n"
"font:50pt \"??????\";\n"
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
"font:50pt \"??????\";\n"
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
        self.lineEdit_name.setStyleSheet('''
QLineEdit{
color: rgb(0, 0, 0);
border:3px solid rgb(0, 0, 0);
border-top:none;
border-left:none;
border-right:none;
font: 14pt "??????";
}
QLineEdit:focus{
	border-bottom-color:rgb(0, 0, 127);
}
        ''')
        self.lineEdit_name.setText("")
        self.lineEdit_name.setPlaceholderText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_pwd = QtWidgets.QLabel(self.widget_2)
        self.label_pwd.setGeometry(QtCore.QRect(475, 260, 51, 21))
        self.label_pwd.setStyleSheet("QLabel{\n"
"    color: rgb(80, 80, 80);\n"
"    font: 10pt \"????????????\";\n"
"}")
        self.label_pwd.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_pwd.setObjectName("label_pwd")
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_pwd.setGeometry(QtCore.QRect(480, 290, 200, 40))
        self.lineEdit_pwd.setStyleSheet('''
QLineEdit{
color: rgb(0, 0, 0);
border:3px solid rgb(0, 0, 0);
border-top:none;
border-left:none;
border-right:none;
font: 14pt "??????";
}
QLineEdit:focus{
	border-bottom-color:rgb(0, 0, 127);
}
        ''')
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.label_name = QtWidgets.QLabel(self.widget_2)
        self.label_name.setGeometry(QtCore.QRect(475, 170, 51, 21))
        self.label_name.setStyleSheet("QLabel{\n"
"    color: rgb(80, 80, 80);\n"
"    font: 10pt \"????????????\";\n"
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
"font: 13pt \"????????????\";\n"
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
"font: 13pt \"????????????\";\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(0, 0, 0);\n"
"}")
        self.btn_registered.setObjectName("btn_registered")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(240, 10, 661, 81))
        self.label.setStyleSheet("QLabel{\n"
"    color: rgb(47, 47, 47);\n"
"    font: 60pt \"??????\";\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(800, 10, 61, 16))
        self.label_2.setStyleSheet("QLabel{\n"
"    color:rgb(107, 107, 107);\n"
"    font: 11pt \"????????????\";\n"
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
        self.stackedWidget.setCurrentIndex(1)
        self.right_Tabwidget.setCurrentIndex(0)
        self.crad_affiliated.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)

    def Init(self):
        self.smj_personal_info = Mysql_PersonalInfo()
        self.splitter_h.setSizes([int(self.width() * 0.99), int(self.width() * 0.01)])
        self.splitter_v.setSizes([int(self.width() * 0.99), int(self.width() * 0.01)])

        # token
        self.__token = JWT()
        self.__th_token = QtJWT(self,self.__token)

    def loginObj(self)->LoginInfo:
        return self.__login_info

    # view??????
    def view_Event(self,card:Card):
        jspath = card.jspath()
        if jspath:
            if not hasattr(self,"view_js"):
                self.view_js = ViewJS()
            self.view_js.external_load_path(jspath)
            self.view_js.show()
        else:
            print("???:",jspath)

    def newjs_Event(self,info:dict):
        # ????????????
        card = Card(info=info)
        card.addViewEvent(self.view_Event)
        self.card_body.external_cardBodyObj().addCard(card)
        self.card_body.external_cardBodyObj().createCard()


    # ????????????
    def newJS_Event(self):
        self.newjs_obj = NewJS()
        self.newjs_obj.external_set_name(self.loginObj().name()) # ???????????????
        self.newjs_obj.newjsed.connect(self.newjs_Event)
        self.newjs_obj.show()

    def external_update_js(self,update_obj:UpdateJS,card:Card):
        if card:
            update_obj.setCard(card,self.loginObj())
        else:
            # ?????????????????????
            QMessageBox.warning(self,"??????","???????????????")

    # ????????????
    def update_js_Event(self,info:dict):
        print(info)
        o_number = int(info.get("o_number", None))
        up_number = info.get("up_number",None)
        task = info.get("task",None)
        jspath = info.get("jspath",None)

        if up_number:
            # print(self.card_body.getCardInfo(o_number).info())
            self.card_body.getCardInfo(o_number).updateNumber(up_number)
        if task:
            self.card_body.getCardInfo(o_number).updateTask(task)
        if jspath:
            self.card_body.getCardInfo(o_number).updatePath(jspath)


    # ????????????
    def updateJS_Event(self):
        self.update_obj = UpdateJS()
        self.update_obj.externaled.connect(lambda id:self.external_update_js(self.update_obj,self.card_body.getCardInfo(int(id))))
        self.update_obj.updateEnded.connect(self.update_js_Event)
        self.update_obj.show()

    # ??????????????????
    def toLogin_Event(self):
        # ??????????????????,??????????????????,???????????????,???????????????
        self.stackedWidget.setCurrentIndex(1)
        self.lineEdit_name.setText("")
        self.lineEdit_pwd.setText("")
        self.lineEdit_name.setFocus()
        self.menu_sys.allDisable(False)

    # ????????????
    def code_Event(self):
        self.js_template = JSTemplate()
        self.js_template.show()


    # py2 print ????????? py3 print
    def py2_to_py3_print_Event(self):
        if not hasattr(self,"py2_print"):
            self.py2_print = Py2Py3()
        self.py2_print.show()

    # ??????
    def myMenu(self):
        self.menu_sys = MenuSys(self)
        self.menu_sys.addMenuHeader(["??????","??????","??????"])
        self.menu_sys.addMenuChild("??????",["????????????","????????????","??????","??????????????????"])
        self.menu_sys.addMenuChild("??????",["????????????","?????????????????????","py2_print???py3_print"])
        self.menu_sys.addMenuChild("??????",["??????????????????"])
        # ????????????
        self.menu_sys.connect("??????", "????????????", self.newJS_Event)
        self.menu_sys.connect("??????", "????????????", self.updateJS_Event)
        self.menu_sys.connect("??????", "??????????????????", self.toLogin_Event)
        self.menu_sys.connect("??????", "?????????????????????", self.code_Event)
        self.menu_sys.connect("??????", "py2_print???py3_print", self.py2_to_py3_print_Event)
        # ???????????????
        self.menu_sys.setShortcut("??????","????????????", "Ctrl+N")
        self.menu_sys.setShortcut("??????","????????????", "Ctrl+U")
        self.menu_sys.setShortcut("??????","??????????????????", "Ctrl+E")
        self.menu_sys.setShortcut("??????","?????????????????????", "Ctrl+Shift+C")
        # =================
        # ??????????????????,??????????????????
        self.menu_sys.allDisable(False)


    # ????????????
    def find_Event(self):
        print("??????")

    # ?????????
    def myShortcuts(self):
        QShortcut(QKeySequence(self.tr("Ctrl+F")), self, self.find_Event)
        QShortcut(QKeySequence(self.tr("Ctrl+I")), self, self.newJS_Event)

    # ??????tab????????????
    def bottomSpreadEvent(self):
        self.crad_affiliated.splitterChange(self.splitter_v,int(self.width() * 0.7), int(self.width() * 0.3))

    def rightSpreadEvent(self):
        self.right_Tabwidget.splitterChange(self.splitter_h, int(self.width() * 0.7), int(self.width() * 0.3))

    # ????????????
    def login_Event(self):
        d = {
            # ????????????
            'exp': time.time() + 60*60*8,  # (Expiration Time) ???token???????????????????????????
            'iat': time.time(),  # (Issued At) ?????????????????????????????????
            'iss': 'LX',  # token????????????

            # ????????????
            'data': {
                'username': 'lx',
                "pwd": "123456",
                'timestamp': time.time()
            }
        }
        text_name = self.lineEdit_name.text()
        text_password = self.lineEdit_pwd.text()

        if text_name == "" or text_password == "":
            QMessageBox.warning(self, "??????", "?????????????????????????????????", QMessageBox.Yes, QMessageBox.Yes)
            return

        if self.smj_personal_info.login(text_name, text_password):
            # ??????????????????
            QMessageBox.information(self, "??????", "???????????????", QMessageBox.Yes, QMessageBox.Yes)
            self.stackedWidget.setCurrentIndex(0)
            # ??????????????????--??????
            self.menu_sys.allDisable(True)
            # ??????token,??????????????????
            self.__token.setData(d)
            self.__token.encode() # ??????token
            # ?????????????????????
            self.loginObj().setInfo(text_name, text_password,self.__info)
            # print(self.loginObj().info())
            self.__th_token.start()
        else:
            # ??????????????????
            QMessageBox.warning(self, "??????", "???????????????????????????", QMessageBox.Yes, QMessageBox.Yes)
        self.lineEdit_name.setText("")
        self.lineEdit_pwd.setText("")
        self.lineEdit_name.setFocus()

    # ????????????
    def register_Event(self):
        self.reg = Register()
        self.reg.show()

    # ??????
    def myEvent(self):
        self.crad_affiliated.clickTab(self.bottomSpreadEvent)
        self.right_Tabwidget.clickTab(self.rightSpreadEvent)

        # ??????
        self.btn_login.clicked.connect(self.login_Event)
        self.lineEdit_pwd.returnPressed.connect(self.login_Event)
        # ??????
        self.btn_registered.clicked.connect(self.register_Event)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "jsm"))
        self.label_j2.setText(_translate("self", "J"))
        self.label_m1.setText(_translate("self", "M"))
        self.label_s1.setText(_translate("self", "S"))
        self.label_j1.setText(_translate("self", "J"))
        self.label_s2.setText(_translate("self", "S"))
        self.label_m2.setText(_translate("self", "M"))
        self.label_pwd.setText(_translate("self", "??????"))
        self.label_name.setText(_translate("self", "??????"))
        self.btn_login.setText(_translate("self", "??????"))
        self.btn_registered.setText(_translate("self", "??????"))
        self.label.setText(_translate("self", "??????????????????"))
        self.label_2.setText(_translate("self", "@ LX"))
        self.menu.setTitle(_translate("self", "??????"))
        self.action.setText(_translate("self", "????????????"))
        self.action_2.setText(_translate("self", "????????????"))
        self.action_4.setText(_translate("self", "??????"))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = ScriptManagement()
    win.show()

    sys.exit(app.exec_())
    