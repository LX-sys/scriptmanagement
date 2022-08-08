
'''

    JSM后台
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtNetwork import QAbstractSocket
from core.utility import (
    QApplication,
    QMainWindow,
    QtCore,
    QWidget,
    QGridLayout,
    QTcpSocket,
    QHostAddress,
    QMessageBox
)
from GuiLib import Tree
from core.agreement import createAgreement

from core.JSM_b_system.Js_exploitation_UI import JSExploitation
from core.JSM_b_system.personage_js_UI import PersonageJS
from core.JSM_b_system.js_ranking_UI import JSRanking
from core.JSM_b_system.account_sys import AccountSys

from core.utility import tcp_send,tcp_recv

class JSMBSystemp(QMainWindow):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)

        # 所有界面类名了列表(这里必须是类名,不能是实例名,且要有一定的顺序,需要继承QWidget)
        self.__UI_class_name = [JSExploitation,PersonageJS,JSRanking,AccountSys]
        # 当前窗口
        self.__current_window = None
        self.setupUi()
        self.Init()
        self.InitSocket()
        self.myEvent()

    # 设置/返回当前窗口
    def currentWindow(self,window:QWidget=None):
        if window is None:
            return self.__current_window
        else:
            self.__current_window = window

    def uiClassName(self)->list:
        return self.__UI_class_name

    def Init(self):
        # 创建树
        self.treeWidget.createTree({
            "脚本开发人员":["刘璇","丁梓靖","赵银鹏"],
            "脚本使用次数排名":"",
            "账号管理": "",
            "脚本活跃图像":""
        })
        # 创建界面
        for ui in self.uiClassName():
            self.addUI(ui())

        # 方法测试,展示新增页面
        # self.stackedWidget.setCurrentIndex(self.stackedWidget.count()-1)
        self.stackedWidget.setCurrentIndex(0)

        # 初始化TCP网络连接

    def InitSocket(self):
        # 初始化TCP网络连接
        self.sock = QTcpSocket(self)
        self.sock.connectToHost(QHostAddress.LocalHost, 6666)

        self.sock.readyRead.connect(self.read_data_slot)
        self.sock.disconnected.connect(lambda: print("dasd"))
        self.sock.error.connect(self.isTcpConnected)

    # 判断是否连接到服务器
    def isTcpConnected(self, s):
        if s == QAbstractSocket.SocketError.ConnectionRefusedError:
            # 连接失败提示
            QMessageBox.information(self, "连接失败", "服务器未开启")
            self.sock.close()

    def read_data_slot(self):
        while self.sock.bytesAvailable():
            datagram = self.sock.read(self.sock.bytesAvailable())
            message = tcp_recv(datagram)
            self.messageAnalysis(self.sock, message)

    def messageAnalysis(self, sock, message):
        if message.get("protocolType") == "accountInfo" and message.get("result") == 200:
            user_info = message.get("data")
            for info in user_info:
                self.currentWindow().addUser(info["user"],info["user"],info["pwd"])
    def addTree(self):
        pass

    def setupUi(self):
        self.setObjectName("self")
        self.resize(1211, 718)
        self.setStyleSheet("QWidget{\n"
"    font: 11pt \"黑体\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget = Tree(self.centralwidget)
        self.treeWidget.setMinimumSize(QtCore.QSize(251, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(251, 16777215))
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        # self.stackedWidget.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)
        self.setCentralWidget(self.centralwidget)
        #
        # self.menubar = QtWidgets.QMenuBar(self)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 1211, 21))
        # self.menubar.setObjectName("menubar")
        # self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def addUI(self,widget:QWidget):
        baseUI = QWidget()
        # 创建网格布局
        gbox = QGridLayout()
        gbox.setContentsMargins(1,0,0,0)
        baseUI.setLayout(gbox)
        # 将界面添加到网格布局中
        gbox.addWidget(widget,0,0)

        self.stackedWidget.addWidget(baseUI)

    def onItemClick_Event(self,item:QTreeWidgetItem):
        text = item.text(0)
        if text == "脚本开发人员":
            self.stackedWidget.setCurrentIndex(0)

        if text in ["刘璇","丁梓靖","赵银鹏"]:
            self.stackedWidget.setCurrentIndex(1)

        if text == "脚本使用次数排名":
            self.stackedWidget.setCurrentIndex(2)

        if text == "账号管理":
            self.stackedWidget.setCurrentIndex(3)
            #
            widget = self.stackedWidget.widget(3).children()[1] # type:AccountSys
            self.currentWindow(widget) # 设置当前窗口

            # 想服务器发送请求,获取所有注册用户的信息
            info = createAgreement("accountInfo",dict())
            self.sock.write(tcp_send(info))

    def myEvent(self):
        self.treeWidget.itemClicked.connect(self.onItemClick_Event)
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "JSM后台"))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = JSMBSystemp()
    win.show()

    sys.exit(app.exec_())
    