# -*- coding:utf-8 -*-
# @time:2022/7/1518:15
# @author:LX
# @file:table.py
# @software:PyCharm
import sys
import typing

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QTabWidget
from PyQt5.Qt import Qt


class Table(QTabWidget):
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

    def Init(self):
        self.setTableDirection("right")
        self.defaultStyleSheet()
        self.setTableWidth(0)

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

    def setTableWidth(self,w:int):
        style = self.styleSheet()
        print(style)

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

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     win = Table()
#     win.show()
#
#     sys.exit(app.exec_())
import re
ll = '''
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
'''


print(re.findall("height:.*;",ll))