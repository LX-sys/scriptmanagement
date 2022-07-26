# -*- coding: utf-8 -*-
'''
    脚本模板
'''
import sys
import copy
import random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets



class JSTemplate(QWidget):

    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        # 模板位置,一排最多放多少个模板
        self.__template_pos = [0,-1]
        self.__v_max = 3

        # 模板编号和具体内容
        self.__template_dict = {
            "id":0,
        }
        self.setupUi()

        self.Init()

    def Init(self):
        self.setTitle("代码片段")
        self.setTemplateMaxNumber(4)
        self.addTemplate("清空谷歌进程代码",code='''
import os
os.system('taskkill /im chromedriver.exe /F')
        ''')
        self.addTemplate("获取当前年龄",code='''
def getAge():
    from datetime import datetime as dt
    Birth = Year_Of_Birth + "-" + Month_Of_Birth.zfill(2) + "-" + Day_Of_Birth.zfill(2)
    return (dt.now()-dt.strptime(Birth,"%Y-%m-%d")).days//365
        ''')
        self.addTemplate("美国时间",code='''Birth = Month_Of_Birth.zfill(2) + "-" + Day_Of_Birth.zfill(2) + "-" + Year_Of_Birth''')
        self.addTemplate("LP模板",code='''
try:
   a_1 = am.see("xpath",'xxx')[0]
   a_2 = am.see("xpath",'xxx')[0]
   e=random.choice([a_1])
   driver.execute_script("arguments[0].scrollIntoView(false);", e)
   am.click(e)

   if e == a_1:
       win_handles = driver.window_handles
       driver.switch_to.window(win_handles[-1])
except:
    pass
time.sleep(random.randint(10,15))
        ''')
        self.addTemplate("移除空白",code='''
def reblank(text):
    import re
    import copy

    s="移除空白函数类似下面这种"
    s= "Adasd ASD       1kld Uca     "
    s= r"Adasd ASD\n       1kld Uca     "
    s= "Adasd ASD" + r"\n" + "       1kld Uca     "
    s = "这是注释说明"

    if "\n" in text:
        return re.sub(r"\n.*?\S"," ",text,re.M)
    else:
        text = text.strip().split(" ")
        copy_text = copy.deepcopy(text)
        for t in copy_text:
            if not t:
                text.remove(t)
        return " ".join(text)
        ''')
        self.addTemplate("元素居中",code='''driver.execute_script("arguments[0].scrollIntoView();", e)''')

    def getID(self) -> int:
        return self.__template_dict["id"]

    # 给对应ID的模板设置内容
    def addCode(self,id:int,code:str):
        if self.__template_dict.get(str(id),None) is None:
            self.__template_dict[str(id)] = code

    def getCode(self,id:int)->str:
        return self.__template_dict.get(str(id),None)

    # 设置模板最大数量
    def setTemplateMaxNumber(self,count:int):
        self.__v_max = count

    # 返回下一个模板的位置
    def next_pos(self) -> list:
        if self.__template_pos[1] < self.__v_max-1:
            self.__template_pos[1]+=1
        else:
            self.__template_pos[0] += 1
            self.__template_pos[1] = 0
        return self.__template_pos

    def setupUi(self):
        self.setObjectName("self")
        self.resize(972, 758)
        self.setStyleSheet('''
QLabel{
	color: rgb(0, 0, 0);
	font: 12pt "黑体";
}
        ''')
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0,0,0,0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 953, 756))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(5,5,5,5)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # ---
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def addTemplate(self,title:str="标准自动化脚本模板",code:str=""):
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(241, 211))
        self.frame.setMaximumSize(QtCore.QSize(241, 250))
        self.frame.setStyleSheet("QWidget{\n"
                                 "    background-color: qlineargradient(spread:pad, x1:0.023, y1:0.023, x2:1, y2:1, stop:0 rgba(130, 247, 255, 164), stop:1 rgba(181, 218, 221, 255));\n"
                                 "}\n"
                                 "QPushButton{\n"
                                 "border:none;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "    background-color: rgb(255, 170, 0);\n"
                                 "}\n"
                                 "QLabel{\n"
                                 "    /*color: rgb(81, 81, 81);*/\n"
                                 "    color: rgb(69, 0, 104);\n"
                                 "    background-color: rgba(160,179, 241, 255);\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        pushButton = QtWidgets.QPushButton(self.frame)
        pushButton.setMinimumSize(QtCore.QSize(240, 222))
        self.verticalLayout.addWidget(pushButton)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setText(title)
        self.label.setMinimumSize(QtCore.QSize(240, 21))
        self.label.setMaximumSize(QtCore.QSize(240, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_2.addWidget(self.frame,*self.next_pos())
        self.__template_dict["id"] += 1
        n = copy.deepcopy(self.getID()) # 这里需要深拷贝一次
        self.addCode(n,code) # 添加代码
        pushButton.clicked.connect(lambda :self.template_Event(n))


    # 模板事件
    def template_Event(self,id):
        print("id:",id)
        print("code:",self.getCode(id))

    def setTitle(self,title:str):
        self.setWindowTitle(title)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "脚本模板"))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = JSTemplate()
    win.show()

    sys.exit(app.exec_())
    