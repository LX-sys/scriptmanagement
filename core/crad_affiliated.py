

from core.utility import (
    QApplication,
    QWidget,
    QtCore,
    QtWidgets
)
from core.utility import sys

class CradAffiliated(QWidget):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.setupUi()
    
    def setupUi(self):
        self.setObjectName("self")
        self.resize(1032, 259)
        self.setStyleSheet("QWidget{\n"
"    background-color: rgb(222, 222, 222);\n"
"}")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 24, 24))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:12px;\n"
"border:1px solid rgb(168, 168, 168);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(226, 226, 226);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:7px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 10, 24, 24))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(86, 255, 109);\n"
"border-radius:12px;\n"
"border:1px solid rgb(72, 216, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(72, 216, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:7px;\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 10, 24, 24))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(216, 235, 13);\n"
"border-radius:12px;\n"
"border:1px solid rgb(199, 199, 99);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(199, 199, 99);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:7px;\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("self", "√"))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = CradAffiliated()
    win.show()

    sys.exit(app.exec_())
    