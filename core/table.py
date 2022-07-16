# -*- coding:utf-8 -*-
# @time:2022/7/1518:15
# @author:LX
# @file:table.py
# @software:PyCharm
import sys
import re
import typing

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QTabWidget
from PyQt5.Qt import Qt


class TableABC(QTabWidget):
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)

        self.resize(400,300)

        self.setMovable(True)
        self.setDocumentMode(True)

        self.tab = QWidget()
        self.addTab(self.tab,"test1")
        self.tab2 = QWidget()
        self.addTab(self.tab2,"test2")

        self.Init()
        self.myEvent()

    def Init(self):
        self.setTableDirection()
        self.defaultStyleSheet()
        self.setTableWidth()

    def defaultStyleSheet(self):
        self.setStyleSheet('''
QWidget{
background-color: rgb(197, 197, 197);
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

    def setTableWidth(self,w:int=30):
        style = self.styleSheet()
        self.setStyleSheet(re.sub("height:(.*)px;","height:{}px;".format(w),style))

    # 设置table的方向
    def setTableDirection(self, dir:str = "top"):
        if dir == "left":
            self.setTabPosition(QTabWidget.West)
        elif dir == "right":
            self.setTabPosition(QTabWidget.East)
        elif dir == "bottom":
            self.setTabPosition(QTabWidget.South)
        else:
            self.setTabPosition(QTabWidget.North)

    # 小标签点击事件
    def tabEvent(self,index:int):
        pass

    def myEvent(self):
        self.tabBarClicked.connect(self.tabEvent)

# 底部tap
class TableBottom(TableABC):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def Init(self):
        self.setTableDirection("bottom")
        self.defaultStyleSheet()
        self.setTableWidth(30)

    def defaultStyleSheet(self):
        self.setStyleSheet('''
QWidget{
background-color: rgb(255, 255, 255);
border-top:2px solid rgb(62, 62, 62);
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

# 右侧tap
class TableRight(TableABC):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def Init(self):
        self.setTableDirection("right")
        self.defaultStyleSheet()
        self.setTableWidth(60)

    def defaultStyleSheet(self):
        self.setStyleSheet('''
QWidget{
background-color: rgb(255, 255, 255);
border-left:2px solid rgb(62, 62, 62);
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

    # def tabEvent(self, index: int):
    #     pass
        # self.resize(30,self.height())



if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = TableBottom()
    win.show()

    sys.exit(app.exec_())
