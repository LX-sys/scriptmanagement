# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'js_ranking_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets



class JSRanking(QWidget):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.setupUi()
    
    def setupUi(self):
        self.setObjectName("self")
        self.resize(992, 689)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setMinimumSize(QtCore.QSize(0, 51))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 51))
        self.label_2.setStyleSheet("font: 18pt \"黑体\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 1, 2, 2)
        self.widget_3 = QtWidgets.QWidget(self)
        self.widget_3.setMinimumSize(QtCore.QSize(381, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(381, 16777215))
        self.widget_3.setStyleSheet("background-color: rgb(255, 49, 49);")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout.addWidget(self.widget_3, 1, 0, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(527, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton.setMaximumSize(QtCore.QSize(75, 23))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label_2.setText(_translate("self", "脚本排名"))
        self.textBrowser.setHtml(_translate("self", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'黑体\'; font-size:11pt;\">具体代码</span></p></body></html>"))
        self.pushButton.setText(_translate("self", "复制"))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = JSRanking()
    win.show()

    sys.exit(app.exec_())
    