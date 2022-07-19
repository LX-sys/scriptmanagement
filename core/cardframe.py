# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt

from card import TitleCard,Card

# 设置
class CardFrame(QWidget):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)

        self.card_obj = []  # 卡片对象
        self.overflow_card_obj = []  # 溢出卡片对象
        self._h = 50

        self.setupUi()
        for i in range(24):
            self.addCard(Card())
        self.createCard()

        self.defaultStyleSheet()

    
    def setupUi(self):
        self.resize(1240, 700)
        self.var_body = QtWidgets.QVBoxLayout(self)
        self.var_body.setContentsMargins(0, 0, 0, 0)
        self.var_body.setSpacing(0)
        self.var_body.addWidget(TitleCard())

        self.scrollArea = QtWidgets.QScrollArea(self)
        # 设置滚动条不显示
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scrollArea.setWidgetResizable(True)
        self.scrollwidge = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout(self.scrollwidge)
        self.vbox.setContentsMargins(6, 0, 6, 0)
        self.vbox.setSpacing(5)

        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.scrollArea.setWidget(self.scrollwidge)
        self.var_body.addWidget(self.scrollArea)



    def defaultStyleSheet(self):
        self.setStyleSheet('''
        border:none;
        ''')

    # 在底部添加窗口
    def endWidget(self,widget:QWidget):
        self.var_body.addWidget(widget)

    # 添加卡片
    def addCard(self, card: QWidget):
        print(self.cardCount(),self.getCapacity())
        if self.cardCount() <= self.getCapacity():
            self.card_obj.append(card)
            # 获取一下高度
            self._h = card.size().height()
        else:
            self.overflow_card_obj.insert(0,card)
            print("超过页面显示的最大数量")

    # 卡片数量
    def cardCount(self) -> int:
        return len(self.card_obj)

    # 获取容量,一页能展示多少个
    def getCapacity(self) -> int:
        # -1防止移除
        return (self.size().height() // self._h) - 1

    def createCard(self, create: list = None):
        if not create:
            data = self.card_obj
        else:
            data = create
        for card in data:
            self.vbox.addWidget(card)

        # 先删除垂直间隔,在添加,人其拥有处于最下面
        self.vbox.removeItem(self.spacerItem)
        self.vbox.addItem(self.spacerItem)

    def resizeEvent(self, e: QtGui.QResizeEvent) -> None:
        temp = []
        print(self.getCapacity()-len(self.card_obj))
        for _ in range(self.getCapacity()-len(self.card_obj)):
            if self.overflow_card_obj:
                card = self.overflow_card_obj.pop()
                self.card_obj.append(card)
                temp.append(card)
            print("---")
        if temp:
            self.createCard(temp)
        super(CardFrame, self).resizeEvent(e)

    def wheelEvent(self, e: QtGui.QWheelEvent) -> None:
        # print("-->>",e.y())

        # print(e.globalY())
        # now = time.time()
        # print("滚动时间差:",now-self.rolling_time[0])
        # self.rolling_time[0]=now
        # direction = e.angleDelta().y()
        #
        # # self.s+=direction
        # if direction < 0:
        #     print("下")
        # else:
        #     print("上")
        super(CardFrame, self).wheelEvent(e)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = CardFrame()
    win.show()

    sys.exit(app.exec_())

