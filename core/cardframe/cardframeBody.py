

from core.utility import sys,typing

from core.utility import (
    QApplication,
    QWidget,
    QVBoxLayout,
    pyqtSignal,
    QScrollArea,
    QtGui,
    QtWidgets,
    qt_Qt
)

from core.card import Card
from core.cardframe.js_path import JSPath

class MyQScrollArea(QScrollArea):
    scrolled = pyqtSignal(bool)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setStyleSheet('''
QWidget{
	background-color: qlineargradient(spread:pad, x1:0.295955, y1:0.471, x2:0.705, y2:0.778, stop:0.488636 rgba(34, 178, 221, 5));
}
QScrollBar:vertical{
border-radius:5px; 
padding-top:14px; 
padding-bottom:14px; 
}
QScrollBar::handle:vertical
{
    background:qlineargradient(spread:pad, x1:0.023, y1:0.023, x2:1, y2:1, stop:0 rgba(130, 247, 255, 164), stop:1 rgba(181, 218, 221, 255));  
    border-radius:4px;  
    margin-left:4px;
    margin-right:4px;
}
QScrollBar::sub-line:vertical,
QScrollBar::add-line:vertical{
image:url("");
}
QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical{
background-color:qlineargradient(spread:pad, x1:0.295955, y1:0.471, x2:0.705, y2:0.778, stop:0.488636 rgba(34, 178, 221, 5));
}
        ''')
        # 不显示滚动条
        self.setHorizontalScrollBarPolicy(qt_Qt.ScrollBarAlwaysOff)

    def wheelEvent(self, e: QtGui.QWheelEvent) -> None:
        if e.angleDelta().y() < 0:
            self.scrolled.emit(True)

        super(MyQScrollArea, self).wheelEvent(e)



# 自定义滚动区域
class CardFrameBody(QWidget):
    # 修改脚本使用次数信号
    updateCounted = pyqtSignal(dict)

    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.resize(600,500)

        self.scrollArea = MyQScrollArea(self)
        # 窗口,布局,垫片
        self.win = QWidget()
        self.vbox = QVBoxLayout(self.win)
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.scrollArea.setWidget(self.win)
        self.card_obj = []  # 卡片对象
        self.overflow_card_obj = []  # 溢出卡片对象
        self._h = 50
        # 统计脚本路径
        '''
        {
        # 卡片编号:脚本路径,共享路径卡片编号
        "1":{"path":"xxx","number":["1","2"]},
        }
        '''
        self.jspath_obj = JSPath()

        self.setUI()
        self.Init()
        self.scrollArea.scrolled.connect(self.load_page)

    def setUI(self):
        self.scrollArea.setWidgetResizable(True)  # 大小自适应
        # 背景设置为
        self.setStyleSheet('''
        	background-color: qlineargradient(spread:pad, x1:0.484, y1:1, x2:0.488, y2:0, stop:0 rgba(166, 249, 255, 253), stop:1 rgba(243, 254, 255, 255));
        ''')
        # 创建布局
        self.vbox.setContentsMargins(0, 3, 3, 0)
        self.vbox.setSpacing(3)

    def Init(self):
        self.body_vbox = QVBoxLayout(self)
        self.body_vbox.setContentsMargins(0,0,0,0)
        self.body_vbox.addWidget(self.scrollArea)
        # for _ in range(3):
        #     self.addCard(Card())

        self.createCard()

    # 添加卡片
    def addCard(self, card: QWidget):
        if self.cardCount() <= self.getCapacity():
            if not self.is_card_exist(card.number()):
                self.card_obj.append(card)
                self.jspath_obj.addJSPath(card)
                # 当脚本路径不唯一时
                if not self.jspath_obj.isOnly(card.jspath()):
                    number_list = self.jspath_obj.getNumberList(card.jspath())
                    count = str(len(number_list))
                    # 先更新自己脚本使用次数
                    card.updateCount(count)
                    # 只需要更新其他脚本的使用次数,移除自己
                    number_list.remove(card.number())
                    # 发送信号,构建信息
                    info ={
                        "number":number_list,
                        "count":count
                    }
                    self.updateCounted.emit(info)

                # 获取一下高度
                self._h = card.size().height()
            else:
                print("编号重复")
        else:
            if card not in self.overflow_card_obj:
                self.overflow_card_obj.insert(0, card)
            # print("超过页面显示的最大数量:",self.overflowCardCount())

    # 卡片数量
    def cardCount(self) -> int:
        return len(self.card_obj)

    def card(self)-> typing.List[Card]:
        return self.card_obj

    # 判断IP是否重复
    def is_card_exist(self, number: str) -> bool:
        for card in self.card_obj:
            if card.number() == number:
                return True
        return False

    # 溢出卡片数量
    def overflowCardCount(self) -> int:
        return len(self.overflow_card_obj)

    # 获取容量,一页能展示多少个
    def getCapacity(self) -> int:
        # -1防止移除
        return (self.height() // self._h) - 1

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
        # self.scrollArea.setMaximumHeight(self.height())
        super(CardFrameBody, self).resizeEvent(e)

    # 加载页面
    def load_page(self)-> None:
        if self.overflowCardCount():
            self.vbox.addWidget(self.overflow_card_obj.pop())
            self.vbox.removeItem(self.spacerItem)
            self.vbox.addItem(self.spacerItem)
            print("加载剩余个数:", self.overflowCardCount())

    # 删除卡片-卡片对象
    def removeCard(self, card: Card):
        if card in self.card_obj:
            self.card_obj.remove(card)
            self.vbox.removeWidget(card)
            card.deleteLater()
            return True
        else:
            print("卡片不存在")
            return False

    # 根据ID删除卡片
    def removeCard_ID(self,id:int):
        left = 0
        right = len(self.card_obj) - 1
        while left <= right:
            mid = (left + right) // 2
            if int(self.card_obj[mid].id_()) == id:
                self.removeCard(self.card_obj[mid])
                return True
            elif int(self.card_obj[mid].id_()) > id:
                right = mid - 1
            else:
                left = mid + 1
        return False

    # 根据编号删除卡片
    def removeCard_number(self,number:str):
        for card in self.card_obj:
            if card.number() == number:
                self.removeCard(card)
                return True
        return False

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = CardFrameBody()
    win.show()

    sys.exit(app.exec_())