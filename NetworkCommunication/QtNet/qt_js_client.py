# -*- coding:utf-8 -*-
# @time:2022/8/514:56
# @author:LX
# @file:qt_js_sever.py
# @software:PyCharm
import sys
from PyQt5.QtNetwork import QUdpSocket, QHostAddress
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QVBoxLayout

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtNetwork import QTcpSocket, QHostAddress
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QTextEdit, QSplitter, QPushButton, \
    QHBoxLayout, QVBoxLayout,QLineEdit


class Client(QWidget):
    def __init__(self):
        super(Client, self).__init__()
        self.resize(500, 450)
        # 1
        self.browser = QTextBrowser(self)
        self.edit = QTextEdit(self)

        self.splitter = QSplitter(self)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.addWidget(self.browser)
        self.splitter.addWidget(self.edit)
        self.splitter.setSizes([350, 100])

        self.send_btn = QPushButton('Send', self)
        self.close_btn = QPushButton('Close', self)

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        # 2
        self.sock = QTcpSocket(self)
        # QHostAddress.LocalHost
        self.sock.connectToHost(QHostAddress.ConvertLocalHost, 6666)
        self.layout_init()
        self.signal_init()

    def layout_init(self):
        self.h_layout.addStretch(1)
        self.h_layout.addWidget(self.close_btn)
        self.h_layout.addWidget(self.send_btn)
        self.v_layout.addWidget(self.splitter)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def signal_init(self):
        self.send_btn.clicked.connect(self.write_data_slot)  # 3
        self.close_btn.clicked.connect(self.close_slot)  # 4
        self.sock.connected.connect(self.connected_slot)  # 5
        self.sock.readyRead.connect(self.read_data_slot)  # 6

    def write_data_slot(self):
        message = self.edit.toPlainText()
        self.browser.append('Client: {}'.format(message))
        datagram = message.encode()
        self.sock.write(datagram)
        self.edit.clear()

    def connected_slot(self):
        message = 'Connected! Ready to chat! :)'
        self.browser.append(message)

    def read_data_slot(self):
        while self.sock.bytesAvailable():
            datagram = self.sock.read(self.sock.bytesAvailable())
            message = datagram.decode()
            self.browser.append('Server: {}'.format(message))

    def close_slot(self):
        self.sock.close()
        self.close()

    def closeEvent(self, event):
        self.sock.close()
        event.accept()


class ClientABC(QWidget):
    def __init__(self,*args,**kwargs):
        super(ClientABC,self).__init__(*args,**kwargs)
        self.resize(500,450)

        self.sock = QTcpSocket(self)
        self.sock.connectToHost(QHostAddress.LocalHost, 6666)

        self.sock.readyRead.connect(self.read_data_slot)
        self.Init()


    def Init(self):
        self.line = QLineEdit(self)
        self.line.returnPressed.connect(self.send_data_slot)

    def send_data_slot(self):
        text = self.line.text()
        self.sock.write(text.encode())
        self.line.clear()

    def read_data_slot(self):
        while self.sock.bytesAvailable():
            datagram = self.sock.read(self.sock.bytesAvailable())
            message = datagram.decode()
            print(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ClientABC()
    demo.show()
    sys.exit(app.exec_())