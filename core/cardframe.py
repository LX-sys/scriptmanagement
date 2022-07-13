# -*- coding:utf-8 -*-
# @time:2022/7/1317:40
# @author:LX
# @file:cardframe.py
# @software:PyCharm

'''卡片模板'''


import sys
from datetime import datetime
import json
import typing

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QScrollArea, QVBoxLayout, QPushButton, QLabel, QComboBox, QWidget, QSpacerItem, \
    QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

from card2 import Card,TitleCard

class CardFrame(QWidget):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)

        self.card_obj = []
        self._h = 50
        self.Init()

    def Init(self):
        self.resize(1240, 700)
        self.vbox = QVBoxLayout(self)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.addCard(TitleCard())
        for i in range(18):
            self.addCard(Card())
        self.createCard()

    # 卡片数量
    def cardCount(self)->int:
        return len(self.card_obj)

    # 添加卡片
    def addCard(self,card:QWidget):
        print(self.cardCount(),self.getCapacity())
        if self.cardCount() <= self.getCapacity():
            self.card_obj.append(card)
            # 获取一下高度
            self._h = card.size().height()
        else:
            print("超过页面显示的最大数量")

    # 获取容量,一页能展示多少个
    def getCapacity(self)->int:
        # -1防止移除
        return (self.size().height()//self._h) - 1

    def createCard(self):
        for card in self.card_obj:
            self.vbox.addWidget(card)
        self.vbox.addItem(self.verticalSpacer)

    def resizeEvent(self, e: QtGui.QResizeEvent) -> None:
        print(self.getCapacity())
        super(CardFrame, self).resizeEvent(e)

    def wheelEvent(self, e: QtGui.QWheelEvent) -> None:
        direction = e.angleDelta().y()
        if direction < 0:
            print("下")
        else:
            print("上")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = CardFrame()
    win.show()

    sys.exit(app.exec_())
