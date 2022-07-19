import sys
import typing

from PyQt5.QtWidgets import QApplication, QWidget,QScrollArea,QVBoxLayout,QSpacerItem,QScrollBar
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt

from core.card import Card


# 自定义滚动区域
class CardFrameBody(QScrollArea):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        # 窗口,布局,垫片
        self.win = QWidget()
        self.vbox = QVBoxLayout(self.win)
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.card_obj = []  # 卡片对象
        self.overflow_card_obj = []  # 溢出卡片对象
        self._h = 50

        self.setUI()
        self.Init()

    def setUI(self):
        self.setWidget(self.win)
        self.setWidgetResizable(True)  # 大小自适应

        # 创建布局
        self.vbox.setContentsMargins(0, 3, 3, 0)
        self.vbox.setSpacing(3)

    def Init(self):
        for _ in range(20):
            self.addCard(Card())

        self.createCard()

    # 添加卡片
    def addCard(self, card: QWidget):
        if self.cardCount() <= self.getCapacity():
            self.card_obj.append(card)
            # 获取一下高度
            self._h = card.size().height()
        else:
            self.overflow_card_obj.insert(0, card)
            # print("超过页面显示的最大数量")

    # 卡片数量
    def cardCount(self) -> int:
        return len(self.card_obj)

    # 溢出卡片数量
    def overflowCardCount(self) -> int:
        return len(self.overflow_card_obj)

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
        for _ in range(self.getCapacity()-len(self.card_obj)):
            if self.overflow_card_obj:
                card = self.overflow_card_obj.pop()
                self.card_obj.append(card)
                temp.append(card)
        if temp:
            self.createCard(temp)
        super(CardFrameBody, self).resizeEvent(e)


    def wheelEvent(self, e: QtGui.QWheelEvent) -> None:
        # print(e.angleDelta())
        super(CardFrameBody, self).wheelEvent(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = CardFrameBody()
    win.show()

    sys.exit(app.exec_())