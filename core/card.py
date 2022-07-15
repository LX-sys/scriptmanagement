# -*- coding:utf-8 -*-
# @time:2022/7/1315:33
# @author:LX
# @file:card.py
# @software:PyCharm

'''卡片'''

import sys
from datetime import datetime
import json
import typing

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QFrame,QHBoxLayout,QPushButton,QLabel,QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor,QCursor

# 重写QComboBox取消滚动
class myQComboBox(QComboBox):
    def wheelEvent(self, e: QtGui.QWheelEvent) -> None:
        pass


# 共享ID
class ID:
    # 静态变量
    _instance = None
    _flag = False


    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls.__ID = 0
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.__ID = 0

    @classmethod
    def add(cls):
        cls.__ID += 1

    @classmethod
    def getID(cls) -> int:
        return cls.__ID


# CardFrame
class CardABC(QFrame):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)

        # 对象容器,对象字典(便于查找)
        self.obj = []
        self.obj_dict = dict()
        self.Init()

    def defaultStyleSheet(self):
        pass

    def Init(self):
        self.resize(1200, 50)
        # self.setMaximumHeight(50)
        self.hbox = QHBoxLayout(self)

    def getHbox(self)->QHBoxLayout:
        return self.hbox

    def getIDobj(self,id:str)->QWidget:
        return self.obj_dict[id]

    # 添加子项
    def addChild(self, widget:QWidget,index=None,id:str=None):
        if index or index == 0:
            self.obj.insert(index,widget)
        else:
            self.obj.append(widget)

        if id:
            self.obj_dict[id] = widget

    # 创建子项
    def createChild(self):
        for bt in self.obj:
            self.hbox.addWidget(bt)

    def myEvent(self):
        pass


# 标题卡片
class TitleCard(CardABC):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setMinimumHeight(60)
        self.setMaximumHeight(60)
        self.defaultStyleSheet()

        self.addTitle(["ID","脚本编号","任务名称","阅览脚本","被使用次数","进度","创建时间","修改时间","修改时间","参与者","操作记录"])

    def defaultStyleSheet(self):
        self.setStyleSheet('''
QFrame{
	background-color: rgb(0, 0, 0);
}
QLabel{
	color:rgb(120, 174, 255);
	font: 12pt "黑体";
}
        ''')

    def addTitle(self,title:list):
        for t in title:
            l = QLabel(t,self)
            l.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.addChild(l)
        self.createChild()


# 标准卡片
class Card(CardABC):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.defaultStyleSheet()
        self.createCard()

        # 创建共享ID
        self.id = ID()
        self.id.add()
        self.updateID(self.id.getID())

        # 设置光标
        self.setCursor(Qt.OpenHandCursor)

        self.myEvent()

    def defaultStyleSheet(self):
        self.setStyleSheet('''
QFrame{
	background-color: qlineargradient(spread:pad, x1:0, y1:0.528136, x2:1, y2:0.517, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(187, 187, 187, 255));
}
QLabel,QComboBox,QPushButton{
background-color:none;
	color: rgb(0, 0, 0);
	font: 12pt "黑体";
}
QPushButton{
border:none;
}
QPushButton:hover{
	color: rgb(28, 58, 255);
}
        ''')

    # 创建标准卡片
    def createCard(self):
        CENTER = Qt.AlignHCenter | Qt.AlignVCenter # 文本居中

        id_ = QLabel("1",self)  # 最大显示数字100万
        id_.setMinimumSize(60,30)
        id_.setMaximumSize(60,30)
        id_.setAlignment(CENTER)

        number = QLabel("50049",self) # 最大显示数字100万
        number.setMinimumSize(60, 30)
        number.setMaximumSize(60, 30)
        number.setAlignment(CENTER)

        task = QLabel("Solar Survey", self)
        task.setMinimumSize(200, 30)
        task.setMaximumSize(200, 30)
        task.setAlignment(CENTER)

        view = QPushButton("View", self)
        view.setMinimumSize(70,30)
        view.setMaximumSize(70,30)

        count = QPushButton("3", self)
        count.setMinimumSize(60,30)
        count.setMaximumSize(60,30)

        schedule = myQComboBox(self)
        schedule.setMinimumSize(80,25)
        schedule.setMaximumSize(80,25)
        schedule.addItems(["未完成","完成","详情"])

        create_time = QLabel("2022.1.21 10:30", self)
        create_time.setMinimumSize(150,30)
        create_time.setMaximumSize(150,30)
        create_time.setAlignment(CENTER)

        update_time = QLabel("2022.1.21 10:30", self)
        update_time.setMinimumSize(150, 30)
        update_time.setMaximumSize(150, 30)
        update_time.setAlignment(CENTER)

        participator = myQComboBox(self)
        participator.setMinimumSize(80, 25)
        participator.setMaximumSize(80, 25)
        participator.addItems(["刘璇", "丁梓靖", "赵银鹏"])

        history = QPushButton("历史", self)
        history.setMinimumSize(60,30)
        history.setMaximumSize(60,30)

        self.addChild(id_,id="id")
        self.addChild(number,id="number")
        self.addChild(task,id="task")
        self.addChild(view,id="view")
        self.addChild(count,id="count")
        self.addChild(schedule,id="schedule")
        self.addChild(create_time,id="create_time")
        self.addChild(update_time,id="update_time")
        self.addChild(participator,id="participator")
        self.addChild(history,id="history")

        self.createChild()

    # 修改id
    def updateID(self, id: int):
        self.getIDobj("id").setText(str(id))

    # 修改数字
    def updateNumber(self, number: str):
        self.getIDobj("number").setText(number)

    # 修改任务名
    def updateTask(self, task: str):
        self.getIDobj("task").setText(task)

    # 修改使用次数
    def updateCount(self, count: int):
        self.getIDobj("count").setText(str(count))

    # 创建脚本时间
    def createTime(self):
        self.getIDobj("create_time").setText(datetime.now().strftime("%Y-%m-%d %H:%M"))

    # 修改脚本时间
    def updateTime(self):
        self.getIDobj("update_time").setText(datetime.now().strftime("%Y-%m-%d %H:%M"))

    # 完成情况改变时事件
    def boxchangeEvent(self, text: str):
        text = self.getIDobj("schedule").currentText()
        style = '''
        QFrame{
            background-color: <color>;
        }
        QLabel,QComboBox,QPushButton{
            background-color:none;
            color: rgb(0, 0, 0);
            font: 12pt "黑体";
        }
        QPushButton{
        border:none;
        }
        QPushButton:hover{
            color: rgb(28, 58, 255);
        }
                    '''
        if text == "完成":
            style = style.replace("<color>",
                                  "qlineargradient(spread:pad, x1:0, y1:0.528136, x2:1, y2:0.517, stop:0 rgba(86, 255, 109, 255), stop:1 rgba(158, 221, 185, 255))")
        if text == "未完成":
            style = style.replace("<color>",
                                  "qlineargradient(spread:pad, x1:0, y1:0.528136, x2:1, y2:0.517, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(187, 187, 187, 255));")
        if text == "详情":
            style = style.replace("<color>",
                                  "qlineargradient(spread:reflect, x1:1, y1:0.528, x2:0.057, y2:0.54, stop:0 rgba(215, 226, 185, 255), stop:1 rgba(216, 235, 13, 255));")
        self.setStyleSheet(style)

    def myEvent(self):
        self.getIDobj("schedule").currentIndexChanged.connect(self.boxchangeEvent)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = TitleCard()
    win.show()

    sys.exit(app.exec_())
