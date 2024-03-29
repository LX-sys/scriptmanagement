'''

    登录加载界面
'''

from core.utility import sys

from core.utility import (
    QApplication,
    QWidget,
    QMouseEvent,
    QtCore,
    QtWidgets,
    QPoint,
    core_Qt,
    QTextBrowser
)

from GuiLib.progressbar.progressBar import MyQProgressBar
from core.ScriptManagement import ScriptManagement

class OpenLoad(QWidget):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.setupUi()
        # 背景透明
        self.setAttribute(core_Qt.WA_TranslucentBackground, True)
        # 去掉窗口边框
        self.setWindowFlags(core_Qt.FramelessWindowHint)
        # 去掉边框
        self.setAttribute(core_Qt.WA_DeleteOnClose)
        self.myEvent()
    
    def setupUi(self):
        self.setObjectName("self")
        self.resize(1027, 611)
        self.setStyleSheet("QWidget{\n"
"border-radius:7px;\n"
"}")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(80, 80, 791, 481))
        self.label.setStyleSheet("QWidget{    \n"
"    border:none;\n"
"    background-color: qlineargradient(spread:pad, x1:0.023, y1:0.023, x2:1, y2:1, stop:0 rgba(130, 247, 255, 255), stop:1 rgba(190, 191, 221, 255));\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 781, 491))
        self.label_2.setStyleSheet("QWidget{\n"
"border:none;\n"
"background-color:rgb(221, 221, 221);\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 781, 491))
        self.label_3.setStyleSheet("QWidget{\n"
"border:none;\n"
"background-color:qlineargradient(spread:pad, x1:0.023, y1:0.023, x2:1, y2:1, stop:0 rgba(130, 247, 255, 164), stop:1 rgba(181, 218, 221, 255));\n"
"}")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_j1 = QtWidgets.QLabel(self)
        self.label_j1.setGeometry(QtCore.QRect(340, -30, 161, 281))
        self.label_j1.setStyleSheet("QLabel{\n"
"font:210pt \"黑体\";\n"
"background-color: none;\n"
"color:rgb(27, 27, 27);\n"
"}\n"
"")
        self.label_j1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_j1.setObjectName("label_j1")
        self.label_j2 = QtWidgets.QLabel(self)
        self.label_j2.setGeometry(QtCore.QRect(330, -30, 161, 281))
        self.label_j2.setStyleSheet("QLabel{\n"
"font:200pt \"黑体\";\n"
"background-color: none;\n"
"color:qlineargradient(spread:pad, x1:0.295955, y1:0.471, x2:0.54, y2:0.619273, stop:0.488636 rgba(125, 60, 221, 77))\n"
"}\n"
"")
        self.label_j2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_j2.setObjectName("label_j2")
        self.label_s1 = QtWidgets.QLabel(self)
        self.label_s1.setGeometry(QtCore.QRect(490, 40, 161, 281))
        self.label_s1.setStyleSheet("QLabel{\n"
"font:200pt \"黑体\";\n"
"background-color: none;\n"
"/*color: rgb(170, 255, 255);*/\n"
"    color:qlineargradient(spread:pad, x1:0.295955, y1:0.471, x2:0.54, y2:0.619273, stop:0.488636 rgba(34, 178, 221, 216));\n"
"}\n"
"")
        self.label_s1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_s1.setObjectName("label_s1")
        self.label_s2 = QtWidgets.QLabel(self)
        self.label_s2.setGeometry(QtCore.QRect(480, 40, 161, 281))
        self.label_s2.setStyleSheet("QLabel{\n"
"font:210pt \"黑体\";\n"
"background-color: none;\n"
"/*color: rgb(170, 255, 255);*/\n"
"    color:rgb(67, 67, 67);\n"
"}\n"
"")
        self.label_s2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_s2.setObjectName("label_s2")
        self.label_m2 = QtWidgets.QLabel(self)
        self.label_m2.setGeometry(QtCore.QRect(670, -30, 161, 281))
        self.label_m2.setStyleSheet("QLabel{\n"
"font:210pt \"黑体\";\n"
"background-color: none;\n"
"color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(34, 120, 255, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(0, 255, 250, 145), stop:0.45 rgba(255, 193, 0, 208), stop:0.477581 rgba(71, 213, 255, 130), stop:0.518717 rgba(71, 255, 151, 130), stop:0.55 rgba(157, 0, 255, 255), stop:0.57754 rgba(255, 0, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"}\n"
"")
        self.label_m2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_m2.setObjectName("label_m2")
        self.label_m1 = QtWidgets.QLabel(self)
        self.label_m1.setGeometry(QtCore.QRect(660, -30, 161, 281))
        self.label_m1.setStyleSheet("QLabel{\n"
"font:200pt \"黑体\";\n"
"background-color: none;\n"
"color:rgb(58, 58, 58);\n"
"}\n"
"")
        self.label_m1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_m1.setObjectName("label_m1")
        self.progressBar = MyQProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(80, 555, 789, 5))
        self.progressBar.setStyleSheet("QWidget{\n"
"    color:rgb(68, 68, 68);\n"
"    background-color:qlineargradient(spread:pad, x1:0.295955, y1:0.471, x2:0.705, y2:0.778, stop:0.488636 rgba(34, 178, 221, 5));\n"
"border-radius:2px;\n"
"}\n"
"QProgressBar::chunk{\n"
"    background-color: rgb(170, 255, 127);\n"
"}")
        self.progressBar.setProperty("value", 80)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.textEdit = QTextBrowser(self)
        self.textEdit.setGeometry(QtCore.QRect(100, 280, 311, 231))
        self.textEdit.setStyleSheet("QTextBrowser{\n"
"    font: 40pt \"微软雅黑\";\n"
"color:rgb(85, 85, 85);\n"
"border:none;\n"
"    background-color: qlineargradient(spread:pad, x1:0.295955, y1:0.471, x2:0.705, y2:0.778, stop:0.488636 rgba(34, 178, 221, 5));\n"
"}\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(100, 250, 111, 21))
        self.label_5.setStyleSheet("QWidget{\n"
"    background-color:none;\n"
"color:rgb(85, 85, 85);\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(550, 230, 441, 41))
        self.label_4.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(550, 270, 441, 41))
        self.label_6.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(550, 310, 441, 41))
        self.label_7.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.writing = QTextBrowser(self)
        self.writing.setGeometry(QtCore.QRect(390, 380, 431, 101))
        self.writing.setStyleSheet("QTextBrowser{\n"
"    font: 40pt \"微软雅黑\";\n"
"color:rgb(85, 85, 85);\n"
"border:none;\n"
"    background-color: qlineargradient(spread:pad, x1:0.295955, y1:0.471, x2:0.705, y2:0.778, stop:0.488636 rgba(34, 178, 221, 5));\n"
"}\n"
"")
        self.writing.setObjectName("writing")
        self.label_7.raise_()
        self.label_6.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_j1.raise_()
        self.label_j2.raise_()
        self.label_s1.raise_()
        self.label_s2.raise_()
        self.label_m2.raise_()
        self.label_m1.raise_()
        self.progressBar.raise_()
        self.textEdit.raise_()
        self.label_5.raise_()
        self.writing.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def mousePressEvent(self, e: QMouseEvent) -> None:
            if e.button() == core_Qt.LeftButton:
                    self._isTracking = True
                    self._startPos = QPoint(e.x(), e.y())

    def mouseMoveEvent(self, e: QMouseEvent) -> None:
            try:
                    self._endPos = e.pos() - self._startPos
                    self.move(self.pos() + self._endPos)
            except Exception as e:
                    pass

    def mouseReleaseEvent(self, e: QMouseEvent):
            if e.button() == core_Qt.LeftButton:
                    self._isTracking = False


    def myEvent(self):
        # 测试事件
        self.progressBar.add_event_start(self.fake_load_Event)
        self.progressBar.progress_bar_finish_signal.connect(self.wanc)

    def wanc(self):
        print("完成")
        self.jsm = ScriptManagement()
        self.jsm.show()
        self.close()

    # 伪造进度条加载
    def fake_load_Event(self):
        for i in range(101):
            self.progressBar.msleep(150)
            self.progressBar.setValue(i)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label_j1.setText(_translate("self", "J"))
        self.label_j2.setText(_translate("self", "J"))
        self.label_s1.setText(_translate("self", "S"))
        self.label_s2.setText(_translate("self", "S"))
        self.label_m2.setText(_translate("self", "M"))
        self.label_m1.setText(_translate("self", "M"))
        self.textEdit.setHtml(_translate("self", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:40pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">dsadsa..................加载中</span></p></body></html>"))
        self.label_5.setText(_translate("self", "@ LX"))
        self.writing.setHtml(_translate("self", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:40pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Please don\'t let go of your dream quietly, sooner or later it will shine in your hands</span></p></body></html>"))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = OpenLoad()
    win.show()

    sys.exit(app.exec_())
    