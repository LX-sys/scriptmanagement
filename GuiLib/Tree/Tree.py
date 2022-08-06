# -*- coding:utf-8 -*-
# @time:2022/8/612:00
# @author:LX
# @file:Tree.py
# @software:PyCharm


import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QPoint, Qt,pyqtSignal,QSize
from PyQt5.QtGui import QMouseEvent, QCursor
from PyQt5.QtWidgets import (QApplication, QTreeWidget, QMenu,
                             QListWidgetItem, QMessageBox, QTreeWidgetItem)


class Tree(QTreeWidget):
    def __init__(self,*args,**kwargs):
        super(Tree,self).__init__(*args,**kwargs)

        # 注册右键菜单
        # self.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.customContextMenuRequested.connect(self.menu_Event)
        self.myEvent()
        self.Init()

    def Init(self):
        self.setHeaderVisable(False)

    # 隐藏头
    def setHeaderVisable(self,visable:bool):
        self.header().setVisible(visable)

    # 创建树
    def createTree(self, tree_dict: dict):
        '''
        {
        "dasd":["301","302"]

        }
        :return:
        '''
        # 展开
        # self.treeWidget.setItemsExpandable()
        for info, v_list in tree_dict.items():
            item = QTreeWidgetItem(self)
            item.setText(0, info)
            self.addTopLevelItem(item)
            for v in v_list:
                item_c = QTreeWidgetItem(item)
                item_c.setText(0, v)
                # item_c.setText(1, v[1])
                self.addTopLevelItem(item_c)

    # 获取鼠标右键选中的菜单文本
    def getMouseSelectMenuText(self) -> str:
        try:
            return self.currentItem().text(0)
        except:
            return ""

    def menu_Event(self,pos:QPoint):
        # 获取鼠标右键选中的菜单文本
        text = self.getMouseSelectMenuText()
        print(text)
        # 创建菜单
        menu = QMenu()
        # 添加菜单项
        look_action = menu.addAction("查看信息")
        menu.addAction(look_action)

        # 显示菜单
        menu.exec_(QCursor.pos())

    def myEvent(self):
        pass

if __name__ == '__main__':
    # 测试
    app = QApplication(sys.argv)
    tree = Tree()
    tree.show()
    sys.exit(app.exec_())
