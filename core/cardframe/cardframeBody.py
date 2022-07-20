import sys
import typing

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget,QScrollArea,QVBoxLayout,QSpacerItem,QScrollBar
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt

from core.card import Card


class MyQScrollArea(QScrollArea):
    scrolled = pyqtSignal(bool)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def wheelEvent(self, e: QtGui.QWheelEvent) -> None:
        self.scrolled.emit(True)

        super(MyQScrollArea, self).wheelEvent(e)



# 自定义滚动区域
class CardFrameBody(QWidget):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.resize(600,500)

        self.scrollArea = MyQScrollArea(self)
        # 窗口,布局,垫片
        self.win = QWidget()
        # self.win.resize(600,500)
        self.vbox = QVBoxLayout(self.win)
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.scrollArea.setWidget(self.win)
        self.card_obj = []  # 卡片对象
        self.overflow_card_obj = []  # 溢出卡片对象
        self._h = 50

        self.setUI()
        self.Init()
        self.scrollArea.scrolled.connect(self.test)

    def setUI(self):
        self.scrollArea.setWidgetResizable(True)  # 大小自适应

        # 创建布局
        self.vbox.setContentsMargins(0, 3, 3, 0)
        self.vbox.setSpacing(3)

    def Init(self):
        for _ in range(20):
            self.addCard(Card())

        self.createCard()

    # 添加卡片
    def addCard(self, card: QWidget):
        self.card_obj.append(card)
        # print(self.cardCount(),self.getCapacity())
        # if self.cardCount() <= self.getCapacity():
        #     self.card_obj.append(card)
        #     # 获取一下高度
        #     self._h = card.size().height()
        # else:
        #     if card not in self.overflow_card_obj:
        #         self.overflow_card_obj.insert(0, card)
        #         # print(self.overflowCardCount())
        #     print("超过页面显示的最大数量")

    # 卡片数量
    def cardCount(self) -> int:
        return len(self.card_obj)

    # 溢出卡片数量
    def overflowCardCount(self) -> int:
        return len(self.overflow_card_obj)

    # 获取容量,一页能展示多少个
    def getCapacity(self) -> int:
        print(self.win.height())
        # -1防止移除
        return (self.win.height() // self._h) - 1

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
        # temp = []
        # for _ in range(self.getCapacity()-len(self.card_obj)):
        #     if self.overflow_card_obj:
        #         card = self.overflow_card_obj.pop()
        #         self.card_obj.append(card)
        #         temp.append(card)
        # if temp:
        #     self.createCard(temp)
        super(CardFrameBody, self).resizeEvent(e)

    def test(self)-> None:
        # print("dsda")
        if self.overflow_card_obj:
            # print("--")
            # self.win.setMinimumHeight(self.height()+120)
            self.addCard(self.overflow_card_obj.pop())
            self.createCard()
            # print("成功")
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = CardFrameBody()
    win.show()

    sys.exit(app.exec_())