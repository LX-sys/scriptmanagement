'''

    新建脚本
'''
from core.utility import (
    QApplication,
    QWidget,
    QMessageBox,
    QFileDialog,
    pyqtSignal,
    QtCore,
    QtGui,
    QtWidgets
)


from core.utility import datetime,sys

class NewJS(QWidget):
    # 新建脚本完成信号
    newjsed = pyqtSignal(dict)

    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.setupUi()
        self.Init()
        # 窗口前置
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.myEvent()
    
    def setupUi(self):
        self.setObjectName("self")
        self.resize(749, 607)
        self.setStyleSheet("QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.484, y1:1, x2:0.488, y2:0, stop:0 rgba(43, 192, 228, 253), stop:1 rgba(234, 236, 198, 255));\n"
"}")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(350, 50, 391, 501))
        self.groupBox.setMinimumSize(QtCore.QSize(391, 501))
        self.groupBox.setMaximumSize(QtCore.QSize(391, 501))
        self.groupBox.setStyleSheet("QWidget{\n"
"    background-color: none;\n"
"    font: 12pt \"黑体\";\n"
"    border:none;\n"
"}\n"
"QLabel,QPushButton{\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"黑体\";\n"
"}\n"
"QGroupBox:title{\n"
"    color:rgb(0, 0, 0);\n"
"\n"
"}")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.label_id = QtWidgets.QLabel(self.groupBox)
        self.label_id.setGeometry(QtCore.QRect(20, 50, 71, 31))
        self.label_id.setObjectName("label_id")
        self.lineEdit_id = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_id.setGeometry(QtCore.QRect(110, 40, 251, 41))
        self.lineEdit_id.setStyleSheet("QLineEdit{\n"
"border:1px solid rgb(65, 65, 65);\n"
"border-radius:5px;\n"
"font: 75 10pt \"微软雅黑\";\n"
"}\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(0, 170, 255);\n"
"}")
        self.lineEdit_id.setText("")
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.label_task = QtWidgets.QLabel(self.groupBox)
        self.label_task.setGeometry(QtCore.QRect(20, 120, 71, 31))
        self.label_task.setObjectName("label_task")
        self.lineEdit_task = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_task.setGeometry(QtCore.QRect(110, 110, 251, 41))
        self.lineEdit_task.setStyleSheet("QLineEdit{\n"
"border:1px solid rgb(65, 65, 65);\n"
"border-radius:5px;\n"
"font: 75 10pt \"微软雅黑\";\n"
"}\n"
"QLineEdit:focus{\n"
"border:1px solid rgb(0, 170, 255);\n"
"}")
        self.lineEdit_task.setText("")
        self.lineEdit_task.setObjectName("lineEdit_task")
        self.label_jspath = QtWidgets.QLabel(self.groupBox)
        self.label_jspath.setGeometry(QtCore.QRect(20, 180, 71, 31))
        self.label_jspath.setObjectName("label_jspath")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 180, 251, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_jspath = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_jspath.setReadOnly(True)
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
        self.btn_sbumit = QtWidgets.QPushButton(self.groupBox)
        self.btn_sbumit.setGeometry(QtCore.QRect(140, 280, 111, 61))
        self.btn_sbumit.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"border-radius:10px;\n"
"border:1px solid rgb(0, 255, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(0, 0, 255);\n"
"}")
        self.btn_sbumit.setObjectName("btn_sbumit")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(20, -110, 331, 571))
        self.label_2.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(20, -10, 331, 571))
        self.widget.setStyleSheet("QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(200, 200, 200, 255));\n"
"border-radius:10px;\n"
"}\n"
"QLabel,QPushButton{\n"
"background-color:none;\n"
"color: rgb(0, 0, 0);\n"
"font: 15pt \"黑体\";\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 255);\n"
"}")
        self.widget.setObjectName("widget")
        self.id_title = QtWidgets.QLabel(self.widget)
        self.id_title.setGeometry(QtCore.QRect(40, 60, 81, 31))
        self.id_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.id_title.setObjectName("id_title")
        self.id = QtWidgets.QLabel(self.widget)
        self.id.setGeometry(QtCore.QRect(124, 60, 71, 31))
        self.id.setStyleSheet("font: 13pt \"黑体\";\n"
"color: rgb(0, 0, 0);")
        self.id.setObjectName("id")
        self.number_title = QtWidgets.QLabel(self.widget)
        self.number_title.setGeometry(QtCore.QRect(20, 108, 101, 31))
        self.number_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.number_title.setObjectName("number_title")
        self.number = QtWidgets.QLabel(self.widget)
        self.number.setGeometry(QtCore.QRect(130, 108, 141, 31))
        self.number.setStyleSheet("font: 13pt \"黑体\";\n"
"color: rgb(0, 0, 0);")
        self.number.setObjectName("number")
        self.task_title = QtWidgets.QLabel(self.widget)
        self.task_title.setGeometry(QtCore.QRect(20, 150, 101, 31))
        self.task_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.task_title.setObjectName("task_title")
        self.task = QtWidgets.QLabel(self.widget)
        self.task.setGeometry(QtCore.QRect(130, 150, 141, 31))
        self.task.setStyleSheet("font: 13pt \"黑体\";\n"
"color: rgb(0, 0, 0);")
        self.task.setObjectName("task")
        self.view_title = QtWidgets.QLabel(self.widget)
        self.view_title.setGeometry(QtCore.QRect(20, 196, 101, 31))
        self.view_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.view_title.setObjectName("view_title")
        self.view = QtWidgets.QPushButton(self.widget)
        self.view.setGeometry(QtCore.QRect(129, 200, 75, 23))
        self.view.setStyleSheet("font: 13pt \"黑体\";\n"
"color: rgb(0, 0, 0);")
        self.view.setObjectName("view")
        self.count_title = QtWidgets.QLabel(self.widget)
        self.count_title.setGeometry(QtCore.QRect(20, 240, 101, 31))
        self.count_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.count_title.setObjectName("count_title")
        self.count = QtWidgets.QLabel(self.widget)
        self.count.setGeometry(QtCore.QRect(130, 240, 141, 31))
        self.count.setStyleSheet("font: 13pt \"黑体\";\n"
"color: rgb(0, 0, 0);")
        self.count.setObjectName("count")
        self.schedule_title = QtWidgets.QLabel(self.widget)
        self.schedule_title.setGeometry(QtCore.QRect(20, 280, 101, 31))
        self.schedule_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.schedule_title.setObjectName("schedule_title")
        self.schedule = QtWidgets.QLabel(self.widget)
        self.schedule.setGeometry(QtCore.QRect(130, 280, 141, 31))
        self.schedule.setStyleSheet("font: 13pt \"黑体\";\n"
"color: rgb(0, 0, 0);")
        self.schedule.setObjectName("schedule")
        self.create_time_title = QtWidgets.QLabel(self.widget)
        self.create_time_title.setGeometry(QtCore.QRect(20, 320, 101, 31))
        self.create_time_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.create_time_title.setObjectName("create_time_title")
        self.create_time = QtWidgets.QLabel(self.widget)
        self.create_time.setGeometry(QtCore.QRect(130, 320, 161, 31))
        self.create_time.setStyleSheet("font: 13pt \"黑体\";\n"
"color: rgb(0, 0, 0);")
        self.create_time.setObjectName("create_time")
        self.participator_title = QtWidgets.QLabel(self.widget)
        self.participator_title.setGeometry(QtCore.QRect(20, 360, 101, 31))
        self.participator_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.participator_title.setObjectName("participator_title")
        self.participator = QtWidgets.QLabel(self.widget)
        self.participator.setGeometry(QtCore.QRect(130, 360, 141, 31))
        self.participator.setStyleSheet("font: 13pt \"黑体\";\n"
"color: rgb(0, 0, 0);")
        self.participator.setObjectName("participator")
        self.label_2.raise_()
        self.groupBox.raise_()
        self.widget.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def Init(self):
        self.hide_label()

    def hide_label(self):
        # 隐藏所有标签
        self.widget.hide()

    def show_label(self):
        # 显示所有标签
        self.widget.show()

    # 提交事件
    def submitEvent(self):
        text_number = self.lineEdit_id.text()
        # 判断是否为数字
        if not text_number.isdigit():
            QMessageBox.warning(self, "警告", "编号必须是数字", QMessageBox.Yes)
            return

        text_task = self.lineEdit_task.text()
        if text_number == "" or text_task == "":
            QMessageBox.warning(self, "警告", "请输入任务名称！", QMessageBox.Yes)
            return

        jspath = self.lineEdit_jspath.text()
        # 判断是否为空
        if jspath == "":
            QMessageBox.warning(self, "警告", "请选择脚本！", QMessageBox.Yes)
            return

        # 构建信息
        info = {
            "number": text_number,
            "task": text_task,
            "jspath": jspath
        }
        self.number.setText(text_number)
        self.task.setText(text_task)
        self.create_time.setText(datetime.now().strftime("%Y-%m-%d %H:%M"))
        self.show_label()
        self.btn_sbumit.setText("创建完成")

        self.newjsed.emit(info)
        self.setEnabled(False)

    # 打开文件
    def openFileEvent(self):
        # 使用QFileDialog打开文件
        file_name = QFileDialog.getOpenFileName(self, "打开文件", "./", "All Files (*)")
        # 获取文件名
        self.lineEdit_jspath.setText(file_name[0])

    def myEvent(self):
        self.btn_sbumit.clicked.connect(self.submitEvent)
        self.btn_open.clicked.connect(self.openFileEvent)

    # 从外部接收 创建者 姓名
    def external_set_name(self, title):
        self.participator.setText(title)

    def closeEvent(self, e: QtGui.QCloseEvent) -> None:
        self.setEnabled(True)
        super(NewJS, self).closeEvent(e)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "新建脚本"))
        self.groupBox.setTitle(_translate("self", "新建脚本"))
        self.label_id.setText(_translate("self", "脚本编号*"))
        self.lineEdit_id.setPlaceholderText(_translate("self", "必填"))
        self.label_task.setText(_translate("self", "任务名称*"))
        self.lineEdit_task.setPlaceholderText(_translate("self", "必填"))
        self.label_jspath.setText(_translate("self", "脚本路径*"))
        self.lineEdit_jspath.setPlaceholderText(_translate("self", "可选"))
        self.btn_open.setText(_translate("self", "..."))
        self.btn_sbumit.setText(_translate("self", "创建新脚本"))
        self.id_title.setText(_translate("self", "id:"))
        self.id.setText(_translate("self", "1"))
        self.number_title.setText(_translate("self", "脚本编号:"))
        self.number.setText(_translate("self", "40092"))
        self.task_title.setText(_translate("self", "任务名称:"))
        self.task.setText(_translate("self", "hello wrold ...."))
        self.view_title.setText(_translate("self", "预览脚本:"))
        self.view.setText(_translate("self", "View"))
        self.count_title.setText(_translate("self", "使用次数:"))
        self.count.setText(_translate("self", "1"))
        self.schedule_title.setText(_translate("self", "进度:"))
        self.schedule.setText(_translate("self", "未完成"))
        self.create_time_title.setText(_translate("self", "创建时间:"))
        self.create_time.setText(_translate("self", "dasdasd"))
        self.participator_title.setText(_translate("self", "创建者:"))
        self.participator.setText(_translate("self", "刘璇"))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = NewJS()
    win.show()

    sys.exit(app.exec_())
    