# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScriptManagement.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5.QtCore import QIODevice
from PyQt5.QtNetwork import QAbstractSocket

from core.utility import time,sys,json


from core.utility import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QtCore,
    QtWidgets,
    QShortcut,
    QKeySequence,
    QTcpSocket,
    QHostAddress
)

from core.utility import tcp_send,tcp_recv

from core.register import Register
from core.table import TableRight,TableBottom
from core.cardframe.cardframe import CardFrame
from core.menusys.menuSys import MenuSys
from core.card import Card
from core.newJS import NewJS
from core.updateJS import UpdateJS
from core.deleteJS import DeleteJS
# from core.token import JWT,QtJWT
from core.jstemplate.JStemplate_tree import JSTemplate
from core.viewJS import ViewJS
from core.py2_py3.py2_py3 import Py2Py3
from core.login_info import LoginInfo
from core.countView import CountView
from core.agreement import createAgreement

from databases.oper_mysql import CardInfo


# JSM
class ScriptManagement(QMainWindow):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.__info = None
        self.__login_info = LoginInfo()
        self.setupUi()
        self.myMenu()
        self.myStatusBar()
        self.myShortcuts()
        self.myEvent()

        self.Init()
        self.InitSocket()

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
        # 核心区域
        self.card_body = CardFrame(self.splitter_h)

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

        self.retranslateUi()
        self.stackedWidget.setCurrentIndex(1)
        self.right_Tabwidget.setCurrentIndex(0)
        self.crad_affiliated.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)

    # 初始化TCP网络连接
    def InitSocket(self):
        # 初始化TCP网络连接
        self.sock = QTcpSocket(self)
        self.sock.connectToHost(QHostAddress.LocalHost, 6666)

        self.sock.readyRead.connect(self.read_data_slot)
        self.sock.disconnected.connect(lambda :print("dasd"))
        self.sock.error.connect(self.isTcpConnected)

    # 判断是否连接到服务器
    def isTcpConnected(self,s):
        if s == QAbstractSocket.SocketError.ConnectionRefusedError:
            # 连接失败提示
            QMessageBox.information(self, "连接失败", "服务器未开启")
            self.sock.close()

    # 读取数据库
    def read_mysql_db(self):
        # 测试读取数据库
        self.cardDB = CardInfo()
        result = self.cardDB.get_name_card_info(self.loginObj().name())
        # 构建
        for data in result:
            # 构建信息
            info = {
                "task": data["task"],
                "number": data["number"],
                "count": data["count"],
                "schedule": data["schedule"],
                "create_time": data["create_time"],
                "update_time": data["update_time"],
                "participator": data["participator"],
                "jspath": data["jspath"]
            }
            self.newjs(info)
        self.cardDB.close()

    def Init(self):
        self.splitter_h.setSizes([int(self.width() * 0.99), int(self.width() * 0.01)])
        self.splitter_v.setSizes([int(self.width() * 0.99), int(self.width() * 0.01)])

    def loginObj(self)->LoginInfo:
        return self.__login_info

    # view事件
    def view_Event(self,card:Card):
        jspath = card.jspath()
        if jspath:
            if not hasattr(self,"view_js"):
                self.view_js = ViewJS()
            self.view_js.external_load_path(jspath)
            self.view_js.show()
        else:
            print("空:",jspath)

    # Count 事件
    def count_Event(self,card:Card):
        jspath = card.jspath()
        jspath_obj = self.card_body.external_cardBodyObj().external_jspath_obj()
        # 使用同一脚本路径的编号
        number_list = jspath_obj.getNumberList(jspath)
        if not hasattr(self, "count_view"):
            self.count_view = CountView()
        self.count_view.setTitle(card.number())
        self.count_view.createList(number_list)
        self.count_view.show()

    # 真正创建卡片的具体实现
    def newjs(self,info:dict):
        if not self.card_body.external_cardBodyObj().is_card_exist(info["number"]):
            # 创建卡片
            card = Card(info=info)
            card.addViewEvent(self.view_Event)
            card.addCountEvent(self.count_Event)
            self.card_body.external_cardBodyObj().addCard(card)
            self.card_body.external_cardBodyObj().createCard()
            return card
        else:
            return False

    def newjs_Event(self,info:dict):
        card = self.newjs(info) # 本地构建信息
        if card:
            # 重新构建服务器信息结构
            temp_info =card.info()

            temp_info["user"] = self.loginObj().name()
            temp_info["ip"] = "192.168.50.21"
            temp_info["scheduleAll"] = "-".join(temp_info["scheduleAll"])
            temp_info["participatorAll"] = "-".join(temp_info["participatorAll"])
            info = createAgreement("newScript",temp_info)
            # 本地构建完成之后在发送到服务器
            self.sock.write(bytes(json.dumps(info), encoding="utf-8"))
        else:
            # 提示卡片已存在
            QMessageBox.warning(self, "提示", "该编号已存在")

    # 新建脚本
    def newJS_Event(self):
        self.newjs_obj = NewJS()
        self.newjs_obj.external_set_name(self.loginObj().name()) # 设置创建者
        self.newjs_obj.newjsed.connect(self.newjs_Event)
        self.newjs_obj.show()

    def external_update_js(self,update_obj:UpdateJS,card:Card):
        if card:
            update_obj.setCard(card,self.loginObj())
        else:
            # 提示没有该脚本
            QMessageBox.warning(self,"提示","没有该脚本")

    # 更新脚本
    def update_js_Event(self,info:dict):
        # print(info)
        o_number = int(info.get("o_number", None))
        up_number = info.get("up_number",None)
        task = info.get("task",None)
        jspath = info.get("jspath",None)

        # 修改脚本,更新脚本使用次数
        jspath_obj = self.card_body.external_cardBodyObj().external_jspath_obj()

        data = {
            "o_number": o_number
        }
        if up_number:
            self.card_body.getCardInfo(o_number).updateNumber(up_number)
            jspath_obj.updateNumber(str(o_number),up_number)
            # 更新数据库
            data["number"]=up_number
        if task:
            data["task"]=task
            self.card_body.getCardInfo(o_number).updateTask(task)
        if jspath:
            # 在修改路径之前,先获取旧路径绑定的编号
            number_list = jspath_obj.getNumberList(self.card_body.getCardInfo(o_number).jspath())
            # number_list.remove(str(o_number))  # 移除自己 ,下面使用减一,比移除自己执行效率高
            # 修改路径
            self.card_body.getCardInfo(o_number).updatePath(jspath)
            jspath_obj.updateJSPath(str(o_number),jspath)
            # 在同步其他脚本的使用次数-1
            number_list_len = len(number_list)-1
            for n in number_list:
                self.card_body.getCardInfo2(n).updateCount(number_list_len)
            # 在计算修改后的路径使用次数
            number_list = jspath_obj.getNumberList(jspath)
            for n in number_list:
                self.card_body.getCardInfo2(n).updateCount(len(number_list))
            data["jspath"]=jspath
        '''
        data最终结构
        {
            "o_number": o_number
            "xx":"nn"    # xx表示字段名称,nn表示字段值
        }
        '''
        info = createAgreement("updateScript", data)
        self.sock.write(tcp_send(info))

    # 修改脚本
    def updateJS_Event(self):
        self.update_obj = UpdateJS()
        self.update_obj.externaled.connect(lambda id:self.external_update_js(self.update_obj,self.card_body.getCardInfo(int(id))))
        self.update_obj.updateEnded.connect(self.update_js_Event)
        self.update_obj.show()

    # 查询待删除的脚本事件
    def find_del_JS_Event(self,info:dict):
        fun = info["fun"]
        number = info["number"]
        card_info = self.card_body.getCardInfo2(number)
        if card_info:
            temp_info = [card_info.id_(),card_info.number(),card_info.schedule(),
                         card_info.task(),card_info.participator(),card_info.create_time(),"可删除"]
            fun(temp_info)
        else:
            # 提示没有该脚本
            QMessageBox.warning(self,"提示","没有该脚本")

    # 卡片删除事件
    def del_js_Event(self,number:str,del_js_obj:DeleteJS):
        # 是否删除提示
        reply = QMessageBox.question(self,"提示","是否删除该脚本",QMessageBox.Yes|QMessageBox.No)
        if reply == QMessageBox.Yes:
            # 获取与该卡片绑定相同路径卡片的编号
            card=self.card_body.getCardInfo2(number)
            jspath_obj = self.card_body.external_cardBodyObj().external_jspath_obj()
            number_list = jspath_obj.getNumberList(card.jspath()) # 使用同一脚本路径的编号
            number_list.remove(number)  # 移除自己

            if self.card_body.delCard_number(number):
                del_js_obj.resetUI()

                # 删除成功后,更新其他脚本的使用次数
                jspath_obj.removeNumber(number)
                for card_number in number_list:
                    self.card_body.getCardInfo2(card_number).updateCount(len(number_list))

                # 删除数据库
                data = {
                    "number":number,
                }
                info = createAgreement("deleteScript",data)

                self.sock.write(tcp_send(info))

    # 删除脚本
    def deleteJS_Event(self):
        self.del_js = DeleteJS()
        self.del_js.findJSed.connect(self.find_del_JS_Event)
        self.del_js.cardDeled.connect(lambda number:self.del_js_Event(number,self.del_js))
        self.del_js.show()

    # 返回登录界面
    def toLogin_Event(self):
        # 返回登录界面,并清空输入框,聚焦输入框,禁用菜单栏
        self.stackedWidget.setCurrentIndex(1)
        self.lineEdit_name.setText("")
        self.lineEdit_pwd.setText("")
        self.lineEdit_name.setFocus()
        self.menu_sys.allDisable(False)

    # 代码片段
    def code_Event(self):
        self.js_template = JSTemplate()
        self.js_template.show()

    # py2 print 转换为 py3 print
    def py2_to_py3_print_Event(self):
        if not hasattr(self,"py2_print"):
            self.py2_print = Py2Py3()
        self.py2_print.show()

    # 菜单
    def myMenu(self):
        self.menu_sys = MenuSys(self)
        self.menu_sys.addMenuHeader(["文件","模板","关于"])
        self.menu_sys.addMenuChild("文件",["新建脚本","修改脚本","删除脚本","设置","返回登录界面"])
        self.menu_sys.addMenuChild("模板",["脚本模板","代码片段与陷阱","py2_print转py3_print"])
        self.menu_sys.addMenuChild("关于",["脚本管理系统"])
        # 绑定事件
        self.menu_sys.connect("文件", "新建脚本", self.newJS_Event)
        self.menu_sys.connect("文件", "修改脚本", self.updateJS_Event)
        self.menu_sys.connect("文件", "删除脚本", self.deleteJS_Event)
        self.menu_sys.connect("文件", "返回登录界面", self.toLogin_Event)
        self.menu_sys.connect("模板", "代码片段与陷阱", self.code_Event)
        self.menu_sys.connect("模板", "py2_print转py3_print", self.py2_to_py3_print_Event)
        # 绑定快捷键
        self.menu_sys.setShortcut("文件","新建脚本", "Ctrl+N")
        self.menu_sys.setShortcut("文件","修改脚本", "Ctrl+U")
        self.menu_sys.setShortcut("文件","删除脚本", "Ctrl+D")
        self.menu_sys.setShortcut("文件","返回登录界面", "Ctrl+E")
        self.menu_sys.setShortcut("模板","代码片段与陷阱", "Ctrl+Shift+C")
        # =================
        # 禁用所有功能,登录之后开放
        self.menu_sys.allDisable(False)

    # 状态栏
    def myStatusBar(self):
        # 状态栏
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    # 搜索事件
    def find_Event(self):
        print("搜索")

    # 快捷键
    def myShortcuts(self):
        QShortcut(QKeySequence(self.tr("Ctrl+F")), self, self.find_Event)
        QShortcut(QKeySequence(self.tr("Ctrl+I")), self, self.newJS_Event)

    # 底部tab展开事件
    def bottomSpreadEvent(self):
        self.crad_affiliated.splitterChange(self.splitter_v,int(self.width() * 0.7), int(self.width() * 0.3))

    def rightSpreadEvent(self):
        self.right_Tabwidget.splitterChange(self.splitter_h, int(self.width() * 0.7), int(self.width() * 0.3))

    # 消息解析
    def messageAnalysis(self, sock: QIODevice, message: dict):
        if not message.get("protocolType", None):
            return -1

        # 登录
        if message.get("protocolType") == "login" and message.get("result")==200:
            # 登录成功提示
            QMessageBox.information(self, "提示", "登录成功！", QMessageBox.Yes, QMessageBox.Yes)
            self.stackedWidget.setCurrentIndex(0)
            # 开放所有功能--菜单
            self.menu_sys.allDisable(True)
            # 设置登录信息类
            self.loginObj().setInfo(message.get("data").get("username"),
                                    message.get("data").get("pwd"),self.__info)
            self.statusbar.showMessage("登录成功-{}".format(self.loginObj().name()))

            # 加载数据库
            self.read_mysql_db()
            return
        elif message.get("protocolType") == "login" and message.get("result")==400:
            # 登录失败提示
            QMessageBox.information(self, "提示", "登录失败,账号或者密码错误!", QMessageBox.Yes, QMessageBox.Yes)

        # 注册
        if message.get("protocolType") == "register" and message.get("result")==200:
            QtWidgets.QMessageBox.information(self, "提示", "注册成功")
            return
        elif message.get("protocolType") == "register" and message.get("result")==400:
            QtWidgets.QMessageBox.warning(self, "警告", "用户名已存在")
            return

        # 新建脚本
        if message.get("protocolType") == "newScript" and message.get("result")==200:
            QtWidgets.QMessageBox.information(self, "提示", "新建脚本成功")
            return
        elif message.get("protocolType") == "newScript" and message.get("result")==400:
            QtWidgets.QMessageBox.warning(self, "警告", "新建脚本失败")
            return

        # 删除脚本
        if message.get("protocolType") == "deleteScript" and message.get("result")==200:
            QtWidgets.QMessageBox.information(self, "提示", "删除脚本成功")
            return
        elif message.get("protocolType") == "deleteScript" and message.get("result")==400:
            QtWidgets.QMessageBox.warning(self, "警告", "删除脚本失败")
            return

    def read_data_slot(self):
        while self.sock.bytesAvailable():
            datagram = self.sock.read(self.sock.bytesAvailable())
            message = tcp_recv(datagram)
            print(message)
            self.messageAnalysis(self.sock, message)

    # 登录事件
    def login_Event(self):
        text_name = self.lineEdit_name.text()
        text_password = self.lineEdit_pwd.text()

        if text_name == "" or text_password == "":
            QMessageBox.warning(self, "警告", "用户名或密码不能为空！", QMessageBox.Yes, QMessageBox.Yes)
            return

        data = {
                "username": text_name,
                "pwd": text_password
            }
        info = createAgreement("login",data)

        # 发送到服务器
        self.sock.write(tcp_send(info))
        print("---发送成功---")
        self.lineEdit_name.setText("")
        self.lineEdit_pwd.setText("")
        self.lineEdit_name.setFocus()

    # 注册
    def register(self,data:dict):
        info = createAgreement("register",data)
        self.sock.write(tcp_send(info))

    # 注册事件
    def register_Event(self):
        self.reg = Register()
        self.reg.registered.connect(self.register)
        self.reg.show()

    # 更新脚本使用次数
    def updateCount_Event(self,info:dict):
        for n in info["number"]:
            card=self.card_body.getCardInfo2(n)
            card.updateCount(int(info["count"]))

    # 事件
    def myEvent(self):
        self.crad_affiliated.clickTab(self.bottomSpreadEvent)
        self.right_Tabwidget.clickTab(self.rightSpreadEvent)

        # 登录
        self.btn_login.clicked.connect(self.login_Event)
        self.lineEdit_pwd.returnPressed.connect(self.login_Event)
        # 注册
        self.btn_registered.clicked.connect(self.register_Event)
        # 更新脚本使用次数
        self.card_body.external_cardBodyObj().updateCounted.connect(self.updateCount_Event)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "jsm"))
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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = ScriptManagement()
    win.show()

    sys.exit(app.exec_())
    