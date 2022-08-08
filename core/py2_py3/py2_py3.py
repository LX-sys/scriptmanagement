from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox

from core.utility import sys

from core.utility import (
    QApplication,
    QWidget,
    QFileDialog,
    QLineEdit,
    QtCore,
    QtWidgets
)

from fileio.fileIO import FileIO
from GuiLib import Typewriter
from core.utility import py2_print_To_py3
from core.py2_py3.down_window import DownWindow


class Py2Py3(QWidget):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.setupUi()

        self.myEvent()
        self.Init()

    def Init(self):
        self.textEdit_front.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_front.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    def setupUi(self):
        self.setObjectName("self")
        self.resize(658, 565)
        self.setStyleSheet('''
QWidget{
background-color: rgb(255, 255, 255);
font: 10pt "黑体";
}
QLabel,QPushButton{
	color: rgb(0, 0, 0);
	font: 10pt "黑体";
}
QPushButton#btn_img{
color: rgb(255, 255, 255);
border-radius:50px;
background-color: qlineargradient(spread:pad, x1:0.0280455, y1:0, x2:1, y2:0.9545, stop:0 rgba(107, 96, 255, 150), stop:1 rgba(187, 39, 39, 150));
font: 10pt "黑体";
}
QPushButton#btn_img:hover{
border:1px solid rgb(85, 170, 127);
}
QPushButton#btn_img:pressed{
background-color: qlineargradient(spread:pad, x1:0.0280455, y1:0, x2:1, y2:0.9545, stop:0 rgba(9, 12, 255, 255), stop:1 rgba(187, 29, 29, 255));
}
QWidget#textEdit_front{
border:none;
}
QPushButton#btn_down{
border:1px solid rgb(85, 170, 0);
	color: rgb(0, 170, 127);
}
        ''')
        self.gridLayout_3 = QtWidgets.QGridLayout(self)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_jspath = QLineEdit(self)
        self.lineEdit_jspath.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_jspath.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_jspath.setStyleSheet("QLineEdit{\n"
"color: rgb(252, 252, 252);\n"
"font-size:13pt;\n"
"background-color: rgb(143, 143, 143);\n"
"border:1px solid rgb(238, 238, 238);\n"
"border-right:none;\n"
"border-top-left-radius:4px;\n"
"border-bottom-left-radius:4px;\n"
"font: 11pt \"黑体\";\n"
"}")
        self.lineEdit_jspath.setObjectName("lineEdit_jspath")
        self.horizontalLayout.addWidget(self.lineEdit_jspath)
        self.btn_open = QtWidgets.QPushButton(self)
        self.btn_open.setMinimumSize(QtCore.QSize(51, 30))
        self.btn_open.setMaximumSize(QtCore.QSize(51, 30))
        self.btn_open.setStyleSheet("QPushButton{\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-left:none;\n"
"border-top-right-radius:4px;\n"
"border-bottom-right-radius:4px;\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(9, 9, 9);\n"
"font: 13pt \"华文琥珀\";\n"
"}\n"
"QPushButton:pressed{\n"
"font-size:10px;\n"
"background-color:rgb(95, 48, 0);\n"
"}")
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout.addWidget(self.btn_open)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(252, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.textEdit_front = Typewriter(self.page)
        self.textEdit_front.setReadOnly(True)
        self.textEdit_front.setObjectName("textEdit_front")
        self.gridLayout_2.addWidget(self.textEdit_front, 0, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(252, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        self.btn_img = QtWidgets.QPushButton(self.page)
        self.btn_img.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_img.setMaximumSize(QtCore.QSize(100, 100))
        self.btn_img.setObjectName("btn_img")
        self.gridLayout_2.addWidget(self.btn_img, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout.setContentsMargins(0, 0, 0, -1)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.page_2)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 2)
        self.btn_down = QtWidgets.QPushButton(self.page_2)
        self.btn_down.setMinimumSize(QtCore.QSize(80, 23))
        self.btn_down.setMaximumSize(QtCore.QSize(80, 23))
        self.btn_down.setObjectName("btn_down")
        self.gridLayout.addWidget(self.btn_down, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(552, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_3.addWidget(self.stackedWidget, 1, 0, 1, 2)

        self.retranslateUi()
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    # 打开文件
    def openFileEvent(self):
        # 使用QFileDialog打开文件
        file_name = QFileDialog.getOpenFileName(self, "打开文件", "./", "All Files (*)")
        # 获取文件名
        self.lineEdit_jspath.setText(file_name[0])

    # 代码转换
    def codeEvent(self):
        file = FileIO()
        # 获取文件名
        file_name = self.lineEdit_jspath.text()
        if file_name:
            # 获取文件内容
            file_content = file.read(file_name)
            self.textEdit_front.setText(file_content,True)
            self.btn_img.setText("扫描文件中...")
        else:
            QMessageBox.warning(self, "警告", "请选择文件", QMessageBox.Yes)
            return

    # 下载代码
    def downLoadEvent(self):
        code = self.textEdit.toPlainText()
        if not hasattr(self,"downloader"):
            self.down_win = DownWindow()
        self.down_win.show()
        self.down_win.setCode(code)


    # 打字完成触发信号
    def codeEndEvent(self):
        self.stackedWidget.setCurrentIndex(1)
        code = py2_print_To_py3(self.lineEdit_jspath.text())
        if code:
            self.textEdit.setText(code)
        else:
            QMessageBox.warning(self, "警告", "代码中没有py2的print,不需要转换", QMessageBox.Yes)
            return

    def myEvent(self):
        self.btn_open.clicked.connect(self.openFileEvent)
        self.btn_img.clicked.connect(self.codeEvent)
        self.textEdit_front.tyObj().typewrite_end.connect(self.codeEndEvent)
        # 下载文件
        self.btn_down.clicked.connect(self.downLoadEvent)

    def closeEvent(self, e: QtGui.QCloseEvent) -> None:
        self.stackedWidget.setCurrentIndex(0)
        self.lineEdit_jspath.setText("")
        self.textEdit_front.clear()
        self.textEdit.clear()
        self.btn_img.setText("Py2转换")
        super().closeEvent(e)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "转换"))
        self.label.setText(_translate("self", "py2脚本路径:"))
        self.btn_open.setText(_translate("self", "..."))
        self.btn_img.setText(_translate("self", "Py2转换"))
        self.btn_down.setText(_translate("self", "下载"))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = Py2Py3()
    win.show()

    sys.exit(app.exec_())
    