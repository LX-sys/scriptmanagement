# -*- coding:utf-8 -*-
# @time:2022/7/1317:40
# @author:LX
# @file:cardframe.py
# @software:PyCharm

'''卡片模板'''


import sys
import time
from datetime import datetime
import json
import typing

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QScrollArea, QVBoxLayout, QPushButton, QLabel, QComboBox, QWidget, QSpacerItem, \
    QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

from card import Card,TitleCard

class ScrollAreaABC(QScrollArea):

    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.resize(1240, 700)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ScrollAreaWidget = QWidget(self)

    def widget(self) -> QWidget:
        return self.ScrollAreaWidget

    def resizeEvent(self, e: QtGui.QResizeEvent) -> None:

        self.ScrollAreaWidget.resize(e.size())
        super(ScrollAreaABC, self).resizeEvent(e)

class CardF(ScrollAreaABC):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.card_obj = []  # 卡片对象
        self.overflow_card_obj = []  # 溢出卡片对象

        self.Init()
        self.addCard(TitleCard())
        for i in range(16):
            self.addCard(Card())
        self.createCard()

    def Init(self):
        self.vbox = QVBoxLayout(self)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

    # 添加卡片
    def addCard(self, card: QWidget):
        self.card_obj.append(card)
        # print(self.cardCount(),self.getCapacity())
        # if self.cardCount() <= self.getCapacity():
        #     self.card_obj.append(card)
        #     # 获取一下高度
        #     self._h = card.size().height()
        # else:
        #     self.overflow_card_obj.insert(0,card)
        #     print("超过页面显示的最大数量")
        # 创建卡片
    def createCard(self, create: list = None):
        if not create:
            data = self.card_obj
        else:
            data = create
        for card in data:
            self.vbox.addWidget(card)

        # 先删除垂直间隔,在添加,人其拥有处于最下面
        self.vbox.removeItem(self.verticalSpacer)
        self.vbox.addItem(self.verticalSpacer)


class CardFrame(QScrollArea):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)

        self.card_obj = []  # 卡片对象
        self.overflow_card_obj = [] # 溢出卡片对象
        self.s = 0
        self.rolling_time = [0,0]
        self._h = 50
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Init()

    def Init(self):
        self.resize(1240, 700)
        self.ScrollAreaWidget = QWidget(self)
        self.xx = QVBoxLayout(self)
        self.ScrollAreaWidget.resize(1240,700)
        self.ScrollAreaWidget.setStyleSheet('''
        background-color: rgb(188, 255, 218);
        ''')
        # self.ScrollAreaWidget.move(30,30)
        # self.setWidget(self.ScrollAreaWidget)
        self.vbox = QVBoxLayout(self.ScrollAreaWidget)
        self.vw = QWidget(self.ScrollAreaWidget)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        #
        # self.addCard(TitleCard())
        # for i in range(17):
        #     self.addCard(Card())
        # self.createCard()
        # for i in range(3):
        #     self.addCard(Card())
        # self.createCard()

    # 卡片数量
    def cardCount(self)->int:
        return len(self.card_obj)

    # 添加卡片
    def addCard(self,card:QWidget):
        self.card_obj.append(card)
        # print(self.cardCount(),self.getCapacity())
        # if self.cardCount() <= self.getCapacity():
        #     self.card_obj.append(card)
        #     # 获取一下高度
        #     self._h = card.size().height()
        # else:
        #     self.overflow_card_obj.insert(0,card)
        #     print("超过页面显示的最大数量")

    # 获取容量,一页能展示多少个
    def getCapacity(self)->int:
        # -1防止移除
        return (self.size().height()//self._h) - 1

    # 创建卡片
    def createCard(self,create:list=None):
        if not create:
            data = self.card_obj
        else:
            data = create
        for card in data:
            self.vbox.addWidget(card)

        # 先删除垂直间隔,在添加,人其拥有处于最下面
        # self.vbox.removeItem(self.verticalSpacer)
        # self.vbox.addItem(self.verticalSpacer)


    def resizeEvent(self, e: QtGui.QResizeEvent) -> None:
        # temp = []
        # print(self.getCapacity()-len(self.card_obj))
        # for _ in range(self.getCapacity()-len(self.card_obj)):
        #     if self.overflow_card_obj:
        #         card = self.overflow_card_obj.pop()
        #         self.card_obj.append(card)
        #         temp.append(card)
        #     print("---")
        # if temp:
        #     self.createCard(temp)
        self.ScrollAreaWidget.resize(e.size())
        super(CardFrame, self).resizeEvent(e)

    def wheelEvent(self, e: QtGui.QWheelEvent) -> None:
        # now = time.time()
        # print("滚动时间差:",now-self.rolling_time[0])
        # self.rolling_time[0]=now
        direction = e.angleDelta().y()
        # self.s+=direction
        if direction < 0:
            print("下")
        else:
            print("上")
        super(CardFrame, self).wheelEvent(e)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = CardF()
    win.show()

    sys.exit(app.exec_())
