# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'viewJS.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from core.utility import sys

from core.utility import (
    QApplication,
    QWidget,
    QFileDialog,
    QMessageBox,
    QtCore,
    QtWidgets
)

from fileio.fileIO import FileIO



class ViewJS(QWidget):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.__original_path = None # 原始路径
        self.setupUi()

        self.myEvent()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(620, 650)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.label_jspath = QtWidgets.QLabel(self)
        self.label_jspath.setStyleSheet("QLabel{\n"
"    color: rgb(0, 0, 0);\n"
"    font: 10pt \"黑体\";\n"
"}")
        self.label_jspath.setObjectName("label_jspath")
        self.gridLayout.addWidget(self.label_jspath, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_jspath = QtWidgets.QLineEdit(self)
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
"font: 13pt \"黑体\";\n"
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
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 2)
        self.textEdit_code = QtWidgets.QTextEdit(self)
        self.textEdit_code.setStyleSheet("QTextEdit{\n"
"font: 12pt \"黑体\";\n"
"}")
        self.textEdit_code.setObjectName("textEdit_code")
        self.gridLayout.addWidget(self.textEdit_code, 1, 0, 1, 3)
        self.btn_reload = QtWidgets.QPushButton(self)
        self.btn_reload.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_reload.setObjectName("btn_reload")
        self.gridLayout.addWidget(self.btn_reload, 2, 0, 1, 1)
        self.btn_run = QtWidgets.QPushButton(self)
        self.btn_run.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_run.setObjectName("btn_run")
        self.gridLayout.addWidget(self.btn_run, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(247, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    # 原始路径
    def originalPath(self)->str:
        return self.__original_path

    # 从外部加载code路径
    def external_load_path(self,path:str):
        self.writeCode(path)
        self.lineEdit_jspath.setText(path)

    # 写代码到编辑器上
    def writeCode(self,path:str):
        fileio = FileIO()
        fileio.setFilePath(path)
        self.textEdit_code.setText(fileio.read())
        self.setWindowTitle(fileio.getFileNameNoExtension(path))
        self.__original_path = path

    # 打开文件
    def openFileEvent(self):
        # 使用QFileDialog打开文件
        file_name = QFileDialog.getOpenFileName(self, "打开文件", "./", "All Files (*)")
        path = file_name[0]
        if self.__original_path is None:
            self.__original_path = path
        elif self.originalPath() != path:
            decision = QMessageBox.question(self, "警告", "确定修改路径(临时)", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
            if decision == QMessageBox.Yes:
                self.__original_path = path
        # 获取文件名
        self.lineEdit_jspath.setText(self.originalPath())

        self.writeCode(self.originalPath())

    # 重新加载代码
    def reloadCodeEvent(self):
        self.writeCode(self.lineEdit_jspath.text())

    def myEvent(self):
        self.btn_open.clicked.connect(self.openFileEvent)
        # 重新加载
        self.btn_reload.clicked.connect(self.reloadCodeEvent)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "view"))
        self.label_jspath.setText(_translate("self", "脚本路径"))
        self.btn_open.setText(_translate("self", "..."))
        self.btn_reload.setText(_translate("self", "重新加载"))
        self.btn_run.setText(_translate("self", "运行脚本"))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = ViewJS()
    win.show()

    sys.exit(app.exec_())
    