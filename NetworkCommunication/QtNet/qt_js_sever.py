# -*- coding:utf-8 -*-
# @time:2022/8/514:56
# @author:LX
# @file:qt_js_sever.py
# @software:PyCharm
import sys
from PyQt5.QtNetwork import QUdpSocket, QHostAddress
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QVBoxLayout

import sys
from PyQt5.QtCore import Qt, QTimer, QDateTime,QIODevice
from PyQt5.QtNetwork import QUdpSocket, QHostAddress
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

import sys
import json
import requests
from PyQt5.QtNetwork import QTcpServer, QHostAddress
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QVBoxLayout,QPlainTextEdit


from core.utility import Mysql_PersonalInfo,tcp_recv,tcp_send
from core.token import JWT,QtJWT


class Server(QWidget):
    def __init__(self):
        super(Server, self).__init__()
        self.resize(500, 450)

        # 1
        self.browser = QTextBrowser(self)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.browser)
        self.setLayout(self.v_layout)

        # 2
        self.server = QTcpServer(self)
        # QHostAddress.LocalHost
        if not self.server.listen(QHostAddress.LocalHost, 6666):
            self.browser.append(self.server.errorString())
        self.server.newConnection.connect(self.new_socket_slot)

    def new_socket_slot(self):
        sock = self.server.nextPendingConnection()

        peer_address = sock.peerAddress().toString()
        peer_port = sock.peerPort()
        news = 'Connected with address {}, port {}'.format(peer_address, str(peer_port))
        self.browser.append(news)

        sock.readyRead.connect(lambda: self.read_data_slot(sock))
        sock.disconnected.connect(lambda: self.disconnected_slot(sock))

    # 3
    def read_data_slot(self, sock):
        while sock.bytesAvailable():
            datagram = sock.read(sock.bytesAvailable())
            message = datagram.decode()
            answer = self.get_answer(message).replace('{br}', '\n')
            new_datagram = answer.encode()
            sock.write(new_datagram)

    def get_answer(self, message):
        payload = {'key': 'free', 'appid': '0', 'msg': message}
        r = requests.get("http://api.qingyunke.com/api.php?", params=payload)
        answer = json.loads(r.text)['content']
        return answer

    # 4
    def disconnected_slot(self, sock):
        peer_address = sock.peerAddress().toString()
        peer_port = sock.peerPort()
        news = 'Disconnected with address {}, port {}'.format(peer_address, str(peer_port))
        self.browser.append(news)

        sock.close()


class ServerABC(QWidget):
    def __init__(self,*args,**kwargs):
        super(ServerABC,self).__init__(*args,**kwargs)
        self.resize(500,450)
        # 创建TCP服务器
        self.server = QTcpServer(self)
        if not self.server.listen(QHostAddress.LocalHost,6666):
            print("监听失败!")
        self.server.newConnection.connect(self.new_socket_slot)

        self.Init()

    def Init(self):
        # 数据库对象
        self.smj_personal_info = Mysql_PersonalInfo()
        # token,token线程
        # self.__token = JWT()
        # self.__th_token = QtJWT(self, self.__token)

    def appendText(self,text):
        self.p_text.appendPlainText(text)


    def new_socket_slot(self):
        sock = self.server.nextPendingConnection()

        peer_address = sock.peerAddress().toString()
        peer_port = sock.peerPort()
        news = 'Connected with address {}, port {}'.format(peer_address, str(peer_port))
        print(news)
        # 读取数据
        sock.readyRead.connect(lambda: self.read_data_slot(sock))

        # sock.disconnected.connect(lambda: self.disconnected_slot(sock))

    # 消息解析
    def messageAnalysis(self,sock:QIODevice,message:dict):
        if not message.get("protocolType",None):
            return -1

        # 登录验证
        if message.get("protocolType") == "login":
            text_name = message.get("data").get("username")
            text_password = message.get("data").get("pwd")
            print(text_name,text_password)
            info = {
                "protocolType": "login",
                "data": {
                    "username": text_name,
                    "pwd": text_password
                },
                "result": None
            }
            # 通过数据库验证
            if self.smj_personal_info.login(text_name, text_password):
                info["result"] = 200
            else:
                info["result"] = 400
            sock.write(tcp_send(info))
            return

        # 注册验证
        if message.get("protocolType") == "register":
            text_name = message.get("data").get("username")
            text_password = message.get("data").get("pwd")
            info = {
                "protocolType": "register",
                "data": {
                    "username": text_name,
                    "pwd": text_password
                },
                "result": None
            }
            # 通过数据库验证
            if self.smj_personal_info.insert(text_name, text_password):
                info["result"] = 200
            else:
                info["result"] = 400
            sock.write(tcp_send(info))
            return

    def read_data_slot(self, sock:QIODevice):
        while sock.bytesAvailable():
            datagram = sock.read(sock.bytesAvailable())
            message = tcp_recv(datagram)
            self.messageAnalysis(sock,message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ServerABC()
    demo.hide()
    sys.exit(app.exec_())