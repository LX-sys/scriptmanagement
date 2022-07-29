# -*- coding:utf-8 -*-
# @time:2022/7/1518:15
# @author:LX
# @file:table.py
# @software:PyCharm
from core.utility import sys,re

# from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QDockWidget,QMainWindow
# from PyQt5.Qt import Qt

from core.utility import (
    QApplication,
    QWidget,
    QTabWidget,
    QDockWidget,
    QMainWindow,
    qt_Qt

)

from core.crad_affiliated import CradAffiliated


# 自定义拖拽窗口
class MyQDockWidget(QDockWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.dockWidgetContents = QWidget()
        self.setWidget(self.dockWidgetContents)

        self.lock = True
        self.setContentsMargins(0,0,0,0)
        # self.defaultStyleSheet()
        # 禁止关闭
        self.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        # self.setTitleBarWidget(QWidget())


    def setText(self,text:str):
        self.setWindowTitle(text)

    def defaultStyleSheet(self):
        self.setStyleSheet('''
                background-color: rgb(0, 255, 127);
                ''')

    def getWidget(self) -> QWidget:
        return self.dockWidgetContents




class TableABC(QTabWidget):
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)

        self.resize(400,300)
        # 方向
        self.direction = "top"
        self.tab_width = 30
        # 所有tab的开关
        self.tab_switch = dict()
        self.cu_index = 0
        # tab对应拖拽窗口
        self.tab_doc = dict()

        self.setMovable(True)
        self.setDocumentMode(True)

        self.add("hello")
        self.add("world")

        self.Init()
        self.myEvent()

    def Init(self):
        self.tableDirection()
        self.defaultStyleSheet()
        self.tableWidth()

    def add(self,text:str):
        if text not in self.tab_doc:
            self.tab = QMainWindow()
            self.docw = MyQDockWidget()
            self.tab.addDockWidget(qt_Qt.RightDockWidgetArea, self.docw)
            self.addTab(self.tab, text)

            self.tab_switch[str(self.count()-1)] = False
            self.tab_doc[text] = self.docw.getWidget()

    def defaultStyleSheet(self):
        self.setStyleSheet('''
QWidget{
background-color: rgb(197, 197, 197);
border:none;
}
QTabBar{
background-color:none;
}
QTabBar::tab{
font: 8pt "微软雅黑";
color: rgb(217, 217, 217);
height:25px;
background-color: rgb(33, 33, 33);
}
QTabBar::tab:selected{
color: rgb(255, 255, 255);
background-color: rgb(113, 113, 113);
}
        ''')

    # 宽度
    def setTableWidth(self,w:int=30):
        self.tab_width = w

    def tableWidth(self):
        style = self.styleSheet()
        self.setStyleSheet(re.sub("height:(.*)px;", "height:{}px;".format(self.tab_width), style))

    # 设置table的方向
    def setTableDirection(self, dir:str = "top"):
        self.direction = dir

    def tableDirection(self):
        if self.direction == "left":
            self.setTabPosition(QTabWidget.West)
        elif self.direction == "right":
            self.setTabPosition(QTabWidget.East)
        elif self.direction == "bottom":
            self.setTabPosition(QTabWidget.South)
        else:
            self.setTabPosition(QTabWidget.North)

    # 小标签点击事件
    def tabEvent(self,index:int):
        # 记录当前点击的tab
        self.cu_index = index
        # text = self.tabText(index)
        # print(self.tab_doc[text])

    def getWidget(self,text:str)->QWidget:
        return self.tab_doc[text]

    def myEvent(self):
        self.tabBarClicked.connect(self.tabEvent)

    # 配合布局伸缩器而改变大小
    def splitterChange(self,splitter,*args):
        index = str(self.cu_index)
        switch = self.tab_switch[index]
        if not switch:
            splitter.setSizes(args)
            self.tab_switch[index] = True
        else:
            '''
                这里应该给使用父类的宽度,而不应该使用self.width()
            '''
            parent_width = splitter.parent().width()
            width_x = parent_width-1
            width_y = 1
            splitter.setSizes([width_x, width_y])
            self.tab_switch[index] = False

    def tt(self,index):
        print(index)

    # 单机tab事件,添加响应事件
    def clickTab(self, f):
        self.tabBarClicked.connect(f)


# 底部tap
class TableBottom(TableABC):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def Init(self):
        self.setTableDirection("bottom")
        super(TableBottom, self).Init()
        # 对象
        self.card_aff = CradAffiliated(self.getWidget("hello"))

    def defaultStyleSheet(self):
        self.setStyleSheet('''
QWidget{
border:none;
background-color: rgb(255, 255, 255);
border-top:1px solid rgb(62, 62, 62);

}
QTabBar{
background-color:  rgb(113, 113, 113);
}
QTabBar::tab{
font: 8pt "微软雅黑";
color: rgb(217, 217, 217);
height:25px;
background-color: rgb(113, 113, 113);
}
QTabBar::tab:selected{
color: rgb(255, 255, 255);
background-color: rgb(33, 33, 33);
}
        ''')


# 右侧tap
class TableRight(TableABC):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def Init(self):
        self.setTableDirection("right")
        self.setTableWidth(60)
        super(TableRight, self).Init()

    def defaultStyleSheet(self):
        self.setStyleSheet('''
QWidget{
background-color: rgb(255, 255, 255);
border-left:0px solid rgb(62, 62, 62);
}
QTabBar{
background-color:  rgb(113, 113, 113);
border:none;
}
QTabBar::tab{
font: 8pt "微软雅黑";
color: rgb(217, 217, 217);
height:25px;
background-color: rgb(113, 113, 113);
}
QTabBar::tab:selected{
color: rgb(255, 255, 255);
background-color: rgb(33, 33, 33);
}
        ''')




if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = TableBottom()
    win.show()

    sys.exit(app.exec_())
