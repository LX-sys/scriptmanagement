
from core.utility import sys

from core.utility import (
    QApplication,
    QWidget,
    core_Qt,
    QtCore,
    QtWidgets,
)

from fileio.fileIO import FileIO


class DownWindow(QWidget):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.setupUi()
        self.__data = ""
        # 窗口前置
        self.setWindowModality(core_Qt.ApplicationModal)
        self.myEvent()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(328, 171)
        self.setMinimumSize(328, 171)
        self.setMaximumSize(328, 171)
        self.setStyleSheet("QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"黑体\";\n"
"}")
        self.btn_down = QtWidgets.QPushButton(self)
        self.btn_down.setGeometry(110, 90, 111, 41)
        self.btn_down.setStyleSheet("QPushButton#btn_down{\n"
"border:1px solid rgb(85, 170, 0);\n"
"color: rgb(0, 170, 127);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#btn_down{\n"
"\n"
"}")
        self.btn_down.setObjectName("btn_down")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(40, 30, 258, 33)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(201, 31)
        self.lineEdit.setMaximumSize(201, 31)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    # 设置代码
    def setCode(self, data):
        self.__data = data

    def code(self)->str:
        return self.__data

    # 下载按钮点击事件
    def btn_down_Event(self):
        file_name = self.lineEdit.text()
        if not file_name or not self.code():
            # 提示用户输入文件名
            QtWidgets.QMessageBox.warning(self, "提示", "请输入文件名")
            return

        if "." not in file_name:
            file_name += ".py"
        file_io = FileIO()
        file_io.write(file_name,content=self.code())
        # 提示用户下载完成
        r=QtWidgets.QMessageBox.information(self, "提示", "下载完成",QtWidgets.QMessageBox.Yes)
        if r==QtWidgets.QMessageBox.Yes:
            self.close()
            self.destroy()

    def myEvent(self):
        print("myEvent")
        self.btn_down.clicked.connect(self.btn_down_Event)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.btn_down.setText(_translate("self", "下载"))
        self.label.setText(_translate("self", "文件名:"))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = DownWindow()
    win.show()

    sys.exit(app.exec_())
    