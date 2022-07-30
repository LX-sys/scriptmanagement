
from core.utility import sys

from core.utility import (
    QApplication,
    QWidget,
    QMessageBox,
    QtCore,
    QtWidgets,
    pyqtSignal,
    QFileDialog
)

from core.login_info import LoginInfo
from fileio.fileIO import FileIO
from core.card import Card


class UpdateJS(QWidget):
    TextID = str

    updateEnded = pyqtSignal(dict)
    # 信号接收卡片对象
    externaled = pyqtSignal(TextID)

    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.setupUi()

        # 窗口前置
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.lineEdit_ip_number.setFocus() # 设置焦点
        self.myEvent()
    
    def setupUi(self):
        self.setObjectName("self")
        self.resize(740, 544)
        self.setMinimumSize(QtCore.QSize(740, 544))
        self.setMaximumSize(QtCore.QSize(740, 544))
        self.setStyleSheet("QWidget#self{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 12pt \"黑体\";\n"
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setMinimumSize(QtCore.QSize(311, 521))
        self.widget.setMaximumSize(QtCore.QSize(400, 600))
        self.widget.setStyleSheet("QWidget{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 12pt \"黑体\";\n"
"    background-color: rgb(91, 0, 136);\n"
"}")
        self.widget.setObjectName("widget")
        self.label_o_title = QtWidgets.QLabel(self.widget)
        self.label_o_title.setGeometry(QtCore.QRect(20, 30, 291, 81))
        self.label_o_title.setStyleSheet("QLabel{\n"
"    font: 24pt \"黑体\";\n"
"}")
        self.label_o_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_o_title.setObjectName("label_o_title")
        self.label_o_id = QtWidgets.QLabel(self.widget)
        self.label_o_id.setGeometry(QtCore.QRect(20, 130, 71, 31))
        self.label_o_id.setObjectName("label_o_id")
        self.label_o_task = QtWidgets.QLabel(self.widget)
        self.label_o_task.setGeometry(QtCore.QRect(20, 190, 71, 31))
        self.label_o_task.setObjectName("label_o_task")
        self.label_o_jspath = QtWidgets.QLabel(self.widget)
        self.label_o_jspath.setGeometry(QtCore.QRect(20, 250, 71, 31))
        self.label_o_jspath.setObjectName("label_o_jspath")
        self.btn_copy = QtWidgets.QPushButton(self.widget)
        self.btn_copy.setGeometry(QtCore.QRect(85, 255, 75, 23))
        self.btn_copy.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color:rgba(255, 255, 255, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(214, 214, 107);\n"
"}\n"
"QPushButton:pressed{\n"
"    color:rgb(240, 240, 240);\n"
"}")
        self.btn_copy.setObjectName("btn_copy")
        self.label_input_id = QtWidgets.QLabel(self.widget)
        self.label_input_id.setGeometry(QtCore.QRect(110, 130, 141, 31))
        self.label_input_id.setObjectName("label_input_id")
        self.label_input_task = QtWidgets.QLabel(self.widget)
        self.label_input_task.setGeometry(QtCore.QRect(110, 190, 181, 31))
        self.label_input_task.setObjectName("label_input_task")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(20, 300, 281, 221))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.btn_find = QtWidgets.QPushButton(self.groupBox)
        self.btn_find.setGeometry(QtCore.QRect(80, 130, 101, 51))
        self.btn_find.setStyleSheet("QPushButton{\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-radius:4px;\n"
"color: rgb(226, 226, 226);\n"
"background-color: rgb(170, 85, 255);\n"
"font: 13pt \"华文琥珀\";\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100, 50, 150);\n"
"}")
        self.btn_find.setObjectName("btn_find")
        self.lineEdit_ip_number = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ip_number.setGeometry(QtCore.QRect(40, 40, 201, 61))
        self.lineEdit_ip_number.setStyleSheet("QLineEdit{\n"
"background-color: rgb(121, 121, 181);\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-radius:8px;\n"
"}\n"
"")
        self.lineEdit_ip_number.setObjectName("lineEdit_ip_number")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self)
        self.widget_2.setMinimumSize(QtCore.QSize(411, 521))
        self.widget_2.setMaximumSize(QtCore.QSize(411, 600))
        self.widget_2.setStyleSheet("QWidget{\n"
"    color: rgb(255, 255, 255);\n"
"    font: 12pt \"黑体\";\n"
"    background-color: rgb(85, 0, 0);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.layoutWidget = QtWidgets.QWidget(self.widget_2)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 290, 251, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_jspath = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_jspath.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_jspath.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_jspath.setStyleSheet("QLineEdit{\n"
"color: rgb(252, 252, 252);\n"
"font-size:13pt;\n"
"border:1px solid rgb(238, 238, 238);\n"
"border-right:none;\n"
"border-top-left-radius:4px;\n"
"border-bottom-left-radius:4px;\n"
"font: 11pt \"黑体\";\n"
"}")
        self.lineEdit_jspath.setText("")
        self.lineEdit_jspath.setObjectName("lineEdit_jspath")
        self.horizontalLayout.addWidget(self.lineEdit_jspath)
        self.btn_open = QtWidgets.QPushButton(self.layoutWidget)
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
        self.lineEdit_id = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_id.setGeometry(QtCore.QRect(130, 140, 251, 41))
        self.lineEdit_id.setStyleSheet("QLineEdit{\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-radius:4px;\n"
"}\n"
"")
        self.lineEdit_id.setText("")
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.label_jspath = QtWidgets.QLabel(self.widget_2)
        self.label_jspath.setGeometry(QtCore.QRect(30, 290, 71, 31))
        self.label_jspath.setObjectName("label_jspath")
        self.label_task = QtWidgets.QLabel(self.widget_2)
        self.label_task.setGeometry(QtCore.QRect(30, 210, 71, 31))
        self.label_task.setObjectName("label_task")
        self.label_id = QtWidgets.QLabel(self.widget_2)
        self.label_id.setGeometry(QtCore.QRect(30, 140, 71, 31))
        self.label_id.setObjectName("label_id")
        self.lineEdit_task = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_task.setGeometry(QtCore.QRect(130, 220, 251, 41))
        self.lineEdit_task.setStyleSheet("QLineEdit{\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-radius:4px;\n"
"}\n"
"")
        self.lineEdit_task.setText("")
        self.lineEdit_task.setObjectName("lineEdit_task")
        self.btn_sbumit = QtWidgets.QPushButton(self.widget_2)
        self.btn_sbumit.setGeometry(QtCore.QRect(160, 370, 111, 41))
        self.btn_sbumit.setStyleSheet("QPushButton{\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-radius:4px;\n"
"color: rgb(43, 43, 43);\n"
"background-color:rgb(0, 255, 127);\n"
"font: 13pt \"华文琥珀\";\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(0, 220, 106);\n"
"}")
        self.btn_sbumit.setObjectName("btn_sbumit")
        self.label_title = QtWidgets.QLabel(self.widget_2)
        self.label_title.setGeometry(QtCore.QRect(140, 30, 161, 81))
        self.label_title.setStyleSheet("QLabel{\n"
"    font: 24pt \"黑体\";\n"
"}")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    '''由于本身是无法获取到卡片信息,所以需要从外部传入卡片信息'''
    def setCard(self, card: Card,loginInfo:LoginInfo):
        if card:
            # 构建真实信息
            info = {
                "name":card.participator(),
                "up_name":loginInfo.name(),
                "id": card.id_(),
                "task": card.task(),
                "jspath": card.jspath(),
            }
        else:  # 这个部分是用于测试
            # 伪造构建信息
            info = {
                "name":"LX",
                "up_name":"LX",
                "id": "1",
                "task": "hello",
                "jspath": "test/test.js",
            }
        self.setOriginInfo(*info.values())

    # 设置源信息
    def setOriginInfo(self,name:str,up_name:str,id: int, task: str, jspath: str):
        # 设置标题
        self.label_o_title.setText("原脚本({})".format(name))
        # 设置修改者
        self.label_title.setText("修改({})".format(up_name))


        self.label_input_id.setText(str(id))
        self.label_input_task.setText(task)
        self.btn_copy.setToolTip("<html><head/><body><p>{}</p></body></html>".format(jspath))


        fileio = FileIO()
        self.setTitle(fileio.getFileNameNoExtension(jspath))

    def setTitle(self, title: str):
        self.setWindowTitle(title)

    # 打开文件
    def openFileEvent(self):
        # 使用QFileDialog打开文件
        file_name = QFileDialog.getOpenFileName(self, "打开文件", "./", "All Files (*)")
        # 获取文件名
        self.lineEdit_jspath.setText(file_name[0])

    # 提交信息
    def submitEvent(self):
        id = self.lineEdit_id.text()
        task = self.lineEdit_task.text()
        jspath = self.lineEdit_jspath.text()


        if not self.label_input_id.text():
            QMessageBox.warning(self, "提示", "请先查询的脚本编号或ID")
            return

        if (not id) and (not task) and (not jspath):
            QMessageBox.warning(self, "提示", "没有做任何修改")
            return

        if not id.isdigit():
            QMessageBox.warning(self, "警告", "编号必须是数字", QMessageBox.Yes)
            return

        if jspath:
            fileio = FileIO()
            self.setTitle(fileio.getFileNameNoExtension(jspath))

        # 构建信息
        info = {
            "id": id if id else None,
            "task": task if task else None,
            "jspath": jspath if jspath else None
        }
        self.btn_sbumit.setText("修改完成")
        # 修改完成提示
        QMessageBox.information(self, "提示", "修改完成")
        # 修改完成,发送信号
        self.updateEnded.emit(info)

    # 查询脚本
    def findEvent(self):
        text_id = self.lineEdit_ip_number.text()
        if not text_id:
            QMessageBox.warning(self, "提示", "请输入要查询的脚本编号或ID")
            return
        if not text_id.isdigit():
            QMessageBox.warning(self, "警告", "编号必须是数字", QMessageBox.Yes)
            return

        # 测试
        if __name__ == '__main__':
            self.setCard(None)
        else:
            # 发送信息
            self.externaled.emit(text_id)

    def myEvent(self):
        self.btn_sbumit.clicked.connect(self.submitEvent)
        self.btn_open.clicked.connect(self.openFileEvent)
        self.btn_find.clicked.connect(self.findEvent)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_o_title.setText(_translate("self", "原脚本()"))
        self.label_o_id.setText(_translate("self", "脚本编号:"))
        self.label_o_task.setText(_translate("self", "任务名称:"))
        self.label_o_jspath.setText(_translate("self", "脚本路径:"))
        self.btn_copy.setToolTip(_translate("self", "<html><head/><body><p>脚本路径</p></body></html>"))
        self.btn_copy.setText(_translate("self", "复制"))
        self.label_input_id.setText(_translate("self", ""))
        self.label_input_task.setText(_translate("self", ""))
        self.groupBox.setTitle(_translate("self", "脚本ID或者编号"))
        self.btn_find.setText(_translate("self", "查询"))
        self.lineEdit_jspath.setPlaceholderText(_translate("self", "可选"))
        self.btn_open.setText(_translate("self", "..."))
        self.lineEdit_id.setPlaceholderText(_translate("self", "可选"))
        self.label_jspath.setText(_translate("self", "脚本路径:"))
        self.label_task.setText(_translate("self", "任务名称:"))
        self.label_id.setText(_translate("self", "脚本编号:"))
        self.lineEdit_task.setPlaceholderText(_translate("self", "可选"))
        self.btn_sbumit.setText(_translate("self", "提交修改"))
        self.label_title.setText(_translate("self", "修改()"))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = UpdateJS()
    win.show()

    sys.exit(app.exec_())
    