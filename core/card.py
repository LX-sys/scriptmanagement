# -*- coding:utf-8 -*-
# @time:2022/7/1315:33
# @author:LX
# @file:card.py
# @software:PyCharm

'''卡片'''
from core.utility import (
    QApplication,
    QWidget,
    QFrame,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QComboBox,
    QtGui,
    core_Qt
)
from core.utility import (
    re,
    sys,
    datetime
)


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
        self.setMaximumHeight(50)
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
            l.setAlignment(core_Qt.AlignHCenter|core_Qt.AlignVCenter)
            self.addChild(l)
        self.createChild()


# 标准卡片
class Card(CardABC):

    def __init__(self, *args,info:dict=None, **kwargs) -> None:
        super().__init__(*args, **kwargs)



        self.defaultStyleSheet()
        self.test_createCard()

        # 创建共享ID
        self.id = ID()
        self.id.add()

        # 添加路径信息

        self.obj_dict["jspath"] = ""

        if not info:
            info = dict()
        self.createCard(info)

        self.myEvent()

    def defaultStyleSheet(self):
        self.setObjectName("body")
        self.setStyleSheet('''
QFrame#body{
	background-color: none;
	border-radius:7px;
}
QFrame#body:hover{
	border:2px solid qlineargradient(spread:pad, x1:0.295955, y1:0.471, x2:0.54, y2:0.619273, stop:0.488636 rgba(125, 60, 221, 77));
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
QComboBox{
background-color: qlineargradient(spread:pad, x1:0.295955, y1:0.471, x2:0.705, y2:0.778, stop:0.488636 rgba(34, 178, 221, 5));
}
QComboBox QAbstractItemView{
color:rgb(12, 12, 12);
background-color:rgb(141, 236, 249);
selection-background-color:rgb(141, 236, 249);
}
QLabel#id{
color: qlineargradient(spread:pad, x1:0.484, y1:1, x2:0.488, y2:0, stop:0 rgba(101, 53, 255, 253), stop:1 rgba(243, 254, 255, 255));;
}
QPushButton#history{
color:gray;
}
QPushButton#history{
color:gray;
}
QPushButton#history:hover{
color:rgb(81, 81, 81);
}

        ''')

    # 保存数据
    def save_data(self,ip="127.0.0.1",data:dict=None):
        if ip == "127.0.0.1":
            pass

    # 创建卡片
    def createCard(self,info:dict):
        # 卡片信息集
        self.updateID(self.id.getID())
        self.updateTask(info.get("task", "test"))
        self.updateNumber(info.get("number", "-1"))
        self.createTime()
        self.updateTime()
        self.updateCount(1)
        self.updatePath(info.get("jspath", ""))
        print("-->",self.info())

    # 创建标准卡片
    def test_createCard(self):
        CENTER = core_Qt.AlignHCenter | core_Qt.AlignVCenter # 文本居中

        id_ = QLabel(self)  # 最大显示数字100万
        id_.setObjectName("id")

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
        import random  # 测试,将列表顺序打乱
        c = ["未完成","完成","详情"]
        random.shuffle(c)
        schedule.addItems(c)

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
        s = ["刘璇", "丁梓靖", "赵银鹏"]
        random.shuffle(s)
        participator.addItems(s)

        history = QPushButton("历史", self)
        history.setObjectName("history")
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

    def info(self):
        info = dict()
        info["id"] = self.id_()
        info["task"] = self.task()
        info["number"] = self.number()
        info["count"] = self.count()
        info["schedule"] = self.schedule()
        info["scheduleAll"] = self.scheduleAll()
        info["create_time"] = self.create_time()
        info["update_time"] = self.update_time()
        info["participator"] = self.participator()
        info["participatorAll"] = self.participatorAll()
        info["jspath"] = self.jspath()
        return info

    def scheduleAll_template(self,name:str) -> list:
        temp = []
        # 获取所有的下拉列表文本
        count = self.getIDobj(name).count()
        for i in range(count):
            temp.append(self.getIDobj(name).itemText(i))
        return temp

    def __setJsPath(self,jspath:str):
        self.obj_dict["jspath"]= jspath

    def id_(self)->str:
        return self.getIDobj("id").text()

    def task(self)->str:
        return self.getIDobj("task").text()

    def number(self)->str:
        return self.getIDobj("number").text()

    def count(self)->str:
        return self.getIDobj("count").text()

    def schedule(self)->str:
        return self.getIDobj("schedule").currentText()

    def scheduleAll(self)->list:
        return self.scheduleAll_template("schedule")

    def create_time(self)->str:
        return self.getIDobj("create_time").text()

    def update_time(self)->str:
        return self.getIDobj("update_time").text()

    def participator(self)->str:
        return self.getIDobj("participator").currentText()

    def participatorAll(self)->list:
        return self.scheduleAll_template("participator")

    def jspath(self)->str:
        return self.getIDobj("jspath")

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

    # 修改当前完成进度
    def updateSchedule(self,name:str):
        self.getIDobj("schedule").setCurrentText(name)

    # 修改当前操作者
    def updateParticipator(self,name:str):
        self.getIDobj("participator").setCurrentText(name)

    def updatePath(self,jspath:str):
        self.__setJsPath(jspath)

    # 绑定事件模型
    def event_model(self,id_name:str,func,args=None):
        if args is None:
            self.getIDobj(id_name).clicked.connect(func)
        else:
            self.getIDobj(id_name).clicked.connect(lambda:func(args))

    # view事件
    def addViewEvent(self,func):
        # 回调自己的函数
        self.event_model("view",func,self)

    # 使用次数的事件
    def addCountEvent(self,func):
        self.event_model("count",func,self)

    # 历史事件
    def addHistoryEvent(self,func):
        self.event_model("history",func,self)

    # 完成情况改变时事件
    def boxchangeEvent(self, text: str):
        text = self.getIDobj("schedule").currentText()
        style =self.styleSheet()

        if text == "完成":
            p = "QFrame#body{\n\tbackground-color:<color>;".replace("<color>",
                                                                    "qlineargradient(spread:pad, x1:0, y1:0.528136, x2:1, y2:0.517, stop:0 rgba(86, 255, 109, 255), stop:1 rgba(158, 221, 185, 255))")
            style = re.sub(r"QFrame#body{\n\tbackground-color:.*;", p, style)

        if text == "未完成":
            p = "QFrame#body{\n\tbackground-color:<color>;".replace("<color>",
                                                                    "qlineargradient(spread:pad, x1:0, y1:0.528136, x2:1, y2:0.517, stop:0 rgba(187, 187, 187, 255), stop:1 rgba(255, 255, 255, 255))")
            style = re.sub(r"QFrame#body{\n\tbackground-color:.*;", p, style)
        if text == "详情":
            p = "QFrame#body{\n\tbackground-color:<color>;".replace("<color>",
                                                                    "qlineargradient(spread:reflect, x1:1, y1:0.528, x2:0.057, y2:0.54, stop:0 rgba(215, 226, 185, 255), stop:1 rgba(216, 235, 13, 255))")
            style = re.sub(r"QFrame#body{\n\tbackground-color:.*;", p, style)
        self.setStyleSheet(style)

    def myEvent(self):
        self.getIDobj("schedule").currentIndexChanged.connect(self.boxchangeEvent)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = Card(info={"number":"123","task":"dasd"})
    win.show()

    sys.exit(app.exec_())
