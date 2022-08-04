# -*- coding: utf-8 -*-



from core.utility import sys,re

from core.utility import (
    QApplication,
    QWidget,
    QMessageBox,
    QtCore,
    QtWidgets,
    pyqtSignal,

)


from GuiLib import Table


class DeleteJS(QWidget):
    # 查询脚本信号
    findJSed = pyqtSignal(dict)
    # 卡片删除信号
    cardDeled = pyqtSignal(str)

    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)

        self.setupUi()
        # 窗口前置
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.myEvent()

        self.Init()
    
    def setupUi(self):
        self.setObjectName("self")
        self.setStyleSheet('''
QWidget{
	font: 12pt "黑体";
}
        ''')
        self.resize(771, 421)
        self.setMinimumSize(QtCore.QSize(771, 421))
        self.setMaximumSize(QtCore.QSize(771, 421))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setMinimumSize(QtCore.QSize(291, 421))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 421))
        self.widget.setStyleSheet("background-color: rgb(173, 178, 255);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 30, 351, 51))
        self.label.setStyleSheet("QLabel{\n"
"    font: 40pt \"Heiti SC\";\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 100, 201, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.btn_find = QtWidgets.QPushButton(self.widget)
        self.btn_find.setGeometry(QtCore.QRect(150, 180, 113, 32))
        self.btn_find.setObjectName("btn_find")
        self.btn_find.setStyleSheet('''
QPushButton{
	background-color: rgb(71, 99, 255);
	color: rgb(255, 255, 255);
	border:1px solid rgb(0, 61, 182);
}
QPushButton:pressed{
	background-color: rgb(0, 53, 159);
}
        ''')
        self.btn_del = QtWidgets.QPushButton(self.widget)
        self.btn_del.setGeometry(QtCore.QRect(90, 350, 231, 61))
        self.btn_del.setObjectName("btn_del")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self)
        self.widget_2.setMinimumSize(QtCore.QSize(371, 421))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 421))
        self.widget_2.setStyleSheet("background-color: rgb(113, 247, 255);")
        self.widget_2.setObjectName("widget_2")
        self.tableWidget = Table(self.widget_2)
        self.tableWidget.setHeaders(["1","2"])
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 361, 401))
        self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(2)
        # self.tableWidget.setRowCount(5)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(4, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(2, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(2, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(3, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(3, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(4, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(4, 1, item)
        # self.tableWidget.horizontalHeader().setVisible(False)
        # self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        # self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        # self.tableWidget.horizontalHeader().setHighlightSections(True)
        # self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        # self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        # self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # self.tableWidget.verticalHeader().setVisible(False)
        # self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        # self.tableWidget.verticalHeader().setHighlightSections(True)
        # self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        # self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    # 设置删除按钮状态
    def setBtnEnable(self, enable:bool):
        if enable:
            self.btn_del.setEnabled(True)
            self.btn_del.setStyleSheet('''
QPushButton{
	background-color: red;
	border:1px solid rgb(179, 0, 0);
	border-radius:10px;
	color: rgb(255, 255, 255);
	font: 24pt "Baoli SC";
}
QPushButton:pressed{
	background-color: rgb(139, 0, 0);
}
            ''')
        else:
            self.btn_del.setEnabled(False)
            self.btn_del.setStyleSheet('''
                        QPushButton{
                        	background-color: gray;
                        	border-radius:10px;
                        	color: rgb(255, 255, 255);
                        	font: 24pt "Baoli SC";
                        }''')

    def Init(self):
        self.setBtnEnable(False)


    # 创建表格
    def createTable(self,info:list):
        hearders = ["ID", "编号","完成情况", "任务名", "创建者", "创建时间", "删除权限"]
        self.tableWidget.tableUrlClear()
        for i in range(len(info)):
            self.tableWidget.addTable([hearders[i],info[i]])

        # 激活删除按钮
        self.setBtnEnable(True)

    # 查找事情
    def find_Event(self):
       text = self.lineEdit.text()
       # 判断是否为全数字
       if not text.isdigit():
           QtWidgets.QMessageBox.warning(self, '提示', '请输入数字!')
           return

       self.label.setText(text+"脚本")
       self.lineEdit.setText("")
       # 构建信息,
       info ={
           "fun":self.createTable, # 回调函数,创建表格
           "number":text
       }
       self.findJSed.emit(info)

       if __name__ == '__main__':
           self.setBtnEnable(True)

    # 删除事件
    def del_Event(self):
        self.cardDeled.emit(self.getNumber())

    def myEvent(self):
        # 查找事件
        self.lineEdit.returnPressed.connect(self.find_Event)
        self.btn_find.clicked.connect(self.find_Event)
        # 删除事件
        self.btn_del.clicked.connect(self.del_Event)

    # 从标题上获取编号
    def getNumber(self):
        text = self.label.text()
        return re.findall("\d+", text)[0]

    # 删除完成后重置界面
    def resetUI(self):
        self.label.setText("脚本")
        self.lineEdit.setText("")
        self.setBtnEnable(False)
        self.tableWidget.tableUrlClear()


    def close(self) -> bool:
        self.resetUI()
        return super().close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "删除脚本"))
        self.label.setText(_translate("self", "脚本"))
        self.btn_find.setText(_translate("self", "查询"))
        self.btn_del.setText(_translate("self", "删除"))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = DeleteJS()
    win.show()

    sys.exit(app.exec_())
    