# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'JStemplate_tree.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import re
from core.utility import QApplication,QWidget,QListWidgetItem,QGridLayout,QPushButton,QTextEdit,QListWidget,QSpacerItem,QSizePolicy,core_Qt,QtCore
from core.utility import joinPath


from GuiLib import LineEditComplement
from fileio.fileIO import FileIO


class JSTemplate(QWidget):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        # 模板编号和具体内容
        self.__template_dict = {
            "id": -1,
        }

        self.setupUi()
        self.myEvent()
        self.Init()

    def Init(self):
        self.setTitle("代码片段")
        self.loadCode()


    def setTitle(self,title:str):
        self.setWindowTitle(title)

    def setupUi(self):
        self.setObjectName("self")
        self.resize(1064, 673)
        self.setStyleSheet("QWidget{\n"
"    font: 11pt \"黑体\";\n"
"    border:1px solid gray;\n"
"}\n"
"QPushButton#btn_ok{\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"}\n"
"QPushButton#btn_ok:hover{\n"
"    background-color: rgb(0, 123, 255);\n"
"}\n"
"QPushButton#btn_ok:pressed{\n"
"    background-color: rgb(0, 52, 157);\n"
"}\n"
"QPushButton#btn_c{\n"
"    color: rgb(241, 241, 241);\n"
"    background-color: rgb(135, 135, 135);\n"
"}\n"
"QPushButton#btn_c:pressed{\n"
"    background-color: rgb(58, 58, 58);\n"
"}")
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setContentsMargins(5, 3, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_search = LineEditComplement(self)
        self.lineEdit_search.setMinimumSize(197, 40)
        self.lineEdit_search.setMaximumSize(197, 40)
        self.lineEdit_search.setStyleSheet("border-top:none;\n"
"border-right:none;\n"
"border-left:none;")
        self.lineEdit_search.setObjectName("lineEdit_search")

        self.gridLayout.addWidget(self.lineEdit_search, 0, 0, 1, 1)
        self.btn_ok = QPushButton(self)
        self.btn_ok.setMinimumSize(58, 40)
        self.btn_ok.setMaximumSize(58, 40)
        self.btn_ok.setObjectName("btn_ok")
        self.gridLayout.addWidget(self.btn_ok, 0, 1, 1, 1)
        self.textEdit_code = QTextEdit(self)
        self.textEdit_code.setStyleSheet("border:none;")
        self.textEdit_code.setObjectName("textEdit_code")
        self.gridLayout.addWidget(self.textEdit_code, 0, 2, 2, 2)
        self.listWidget_title = QListWidget(self)
        self.listWidget_title.setMaximumSize(256, 16777215)
        self.listWidget_title.setStyleSheet("border-top:none;\n"
"border-left:none;\n"
"border-bottom:none;")
        self.listWidget_title.setObjectName("listWidget_title")
        self.gridLayout.addWidget(self.listWidget_title, 1, 0, 2, 2)
        spacerItem = QSpacerItem(760, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.btn_c = QPushButton(self)
        self.btn_c.setMinimumSize(41, 30)
        self.btn_c.setMaximumSize(41, 30)
        self.btn_c.setObjectName("btn_c")
        self.gridLayout.addWidget(self.btn_c, 2, 3, 1, 1)

        self.retranslateUi()

    def getID(self) -> int:
        return self.__template_dict["id"]

    # 给对应ID的模板设置内容
    def addCode(self,id:int,code:str):
        if self.__template_dict.get(str(id),None) is None:
            self.__template_dict[str(id)] = code

    # ID自增
    def id_add(self):
        self.__template_dict["id"] += 1

    def getCode(self,id:int):
        return self.__template_dict.get(str(id),None)

    # 加载所有代码片段
    def loadCode(self):
        fileio = FileIO()
        path = joinPath(r"template\tree_py")
        fileio.setFilePath(path)
        file_names = fileio.getFileName()

        if "__init__.py" in file_names: # 去除__init__.py
            file_names.remove("__init__.py")

        for i in file_names:
            self.addTemplatePath(path+"\{}".format(i))

    def addTemplate(self, title:str,code:str=""):
        self.lineEdit_search.addCompleterList([title])

        item = QListWidgetItem()
        item.setText(title)
        self.listWidget_title.addItem(item)

        self.id_add()
        self.addCode(self.__template_dict["id"],code)

    # 添加代码片段路径
    def addTemplatePath(self,path:str):
        fileio = FileIO()
        fileio.setFilePath(path)
        # 读取标题
        title = re.findall(r"# title:(.*)",fileio.readLine())
        if title:
            # 读取代码
            code = fileio.read()
            self.addTemplate(title[0],code)

    # 从数据库中获取代码片段
    def getCodeFromDB(self):
        pass

    # 写代码到文本框
    def writeCode(self,code:str):
        self.textEdit_code.clear()
        self.textEdit_code.setText(code)

    # 树子项点击事件
    def code_Event(self,item:QListWidgetItem):
        # 获得索引
        index = self.listWidget_title.indexFromItem(item).row()
        # 获得代码
        code = self.getCode(index)
        # print(code)
        self.writeCode(code)

    # 搜索子项点击事件
    def search_Event(self,text:str):
        # 获得索引
        item = self.listWidget_title.findItems(text,core_Qt.MatchContains)
        index=self.listWidget_title.indexFromItem(item[0]).row()
        # 获得代码
        code = self.getCode(index)
        self.writeCode(code)

    # 内容复制到鼠标上
    def copyTomouse_Event(self):
        import copy
        code = self.textEdit_code.toPlainText()
        code_ = code.split("\n")
        del code_[0]  # 移除标题

        # 移除空白
        code_copy = copy.deepcopy(code_)
        for c in code_copy:
            if not c:
                del code_[code_copy.index(c)]
            else: # 遇到第一段有效代码就立刻结束
                break
        # 写入剪贴板
        QApplication.clipboard().setText("\n".join(code_))

    def myEvent(self):
        #listWidget_title的点击事件
        self.listWidget_title.itemClicked.connect(self.code_Event)
        # 搜索子项点击事件
        self.btn_ok.clicked.connect(lambda:self.search_Event(self.lineEdit_search.text()))
        self.lineEdit_search.returnPressed.connect(lambda:self.search_Event(self.lineEdit_search.text()))
        # 复制
        self.btn_c.clicked.connect(lambda:self.copyTomouse_Event())

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.lineEdit_search.setPlaceholderText(_translate("self", "搜索"))
        self.btn_ok.setText(_translate("self", "确定"))
        self.btn_c.setText(_translate("self", "复制"))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = JSTemplate()
    win.show()

    sys.exit(app.exec_())
    