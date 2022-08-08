'''

    账号管理界面
'''

from core.utility import sys

from core.utility import (
    QApplication,
    QWidget,
    QtWidgets,
    QSize,
    QRect,
    core_Qt

)


class AccountSys(QWidget):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.__pos = [0, -1]
        self.setupUi()

        self.Init()


    def Init(self):
        pass
        # self.addUser()
        # self.addUser()
        # self.addUser()
        # self.addUser()
        # self.addUser()

    def nextPos(self)->list:
        self.__pos[1] += 1
        if self.__pos[1]>2:
            self.__pos[1] = 0
            self.__pos[0] += 1
        return self.__pos

    def setupUi(self):
        self.setObjectName("self")
        self.resize(1002, 567)
        self.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
#         self.widget = QtWidgets.QWidget(self)
#         self.widget.setMinimumSize(QSize(270, 220))
#         self.widget.setMaximumSize(QSize(270, 220))
#         self.widget.setStyleSheet("QWidget{\n"
# "background-color:rgba(130, 247, 255, 164);\n"
# "    border-radius:8px;\n"
# "    border:1px solid rgb(0, 0, 0);\n"
# "}")
#         self.widget.setObjectName("widget")
#         self.label_name = QtWidgets.QLabel(self.widget)
#         self.label_name.setGeometry(QRect(70, 10, 101, 51))
#         self.label_name.setStyleSheet("QLabel{\n"
# "    background-color:rgba(34, 178, 221, 0);\n"
# "    font: 18pt \"黑体\";\n"
# "    color:rgb(0, 0, 127);\n"
# "    border:none;\n"
# "}")
#         self.label_name.setAlignment(Qt.AlignCenter)
#         self.label_name.setObjectName("label_name")
#         self.label_user = QtWidgets.QLabel(self.widget)
#         self.label_user.setGeometry(QRect(20, 70, 221, 41))
#         self.label_user.setMinimumSize(QSize(0, 21))
#         self.label_user.setMaximumSize(QSize(16777215, 1990))
#         self.label_user.setStyleSheet("QLabel{\n"
# "    color: rgb(255, 255, 255);\n"
# "    background-color:gray;\n"
# "    font: 15pt \"黑体\";\n"
# "}")
#         self.label_user.setAlignment(Qt.AlignCenter)
#         self.label_user.setObjectName("label_user")
#         self.btn_update = QtWidgets.QPushButton(self.widget)
#         self.btn_update.setGeometry(QRect(40, 170, 30, 30))
#         self.btn_update.setStyleSheet("QPushButton{\n"
# "    background-color: rgb(0, 255, 0);\n"
# "    border-radius:15px;\n"
# "}\n"
# "QPushButton:pressed{\n"
# "    background-color: rgb(0, 189, 0);\n"
# "}\n"
# "")
#         self.btn_update.setObjectName("btn_update")
#         self.btn_del = QtWidgets.QPushButton(self.widget)
#         self.btn_del.setGeometry(QRect(170, 170, 30, 30))
#         self.btn_del.setStyleSheet("QPushButton{\n"
# "    color:rgb(255, 255, 255);\n"
# "    background-color: red;\n"
# "    border-radius:15px;\n"
# "}\n"
# "QPushButton:pressed{\n"
# "    background-color: rgb(170, 0, 0);\n"
# "}")
#         self.btn_del.setObjectName("btn_del")
#         self.label_pwd = QtWidgets.QLabel(self.widget)
#         self.label_pwd.setGeometry(QRect(20, 111, 221, 41))
#         self.label_pwd.setMinimumSize(QSize(0, 21))
#         self.label_pwd.setMaximumSize(QSize(16777215, 1990))
#         self.label_pwd.setStyleSheet("QLabel{\n"
# "    color: rgb(255, 255, 255);\n"
# "    background-color:gray;\n"
# "    font: 15pt \"黑体\";\n"
# "}")
#         self.label_pwd.setAlignment(Qt.AlignCenter)
#         self.label_pwd.setObjectName("label_pwd")
#         self.btn_details = QtWidgets.QPushButton(self.widget)
#         self.btn_details.setGeometry(QRect(90, 170, 61, 31))
#         self.btn_details.setStyleSheet("QPushButton{\n"
# "    font: 12pt \"黑体\";\n"
# "    color: rgb(255, 255, 255);\n"
# "    background-color: rgb(0, 85, 255);\n"
# "}\n"
# "QPushButton:pressed{\n"
# "    background-color: rgb(0, 0, 223);\n"
# "}")
#         self.btn_details.setObjectName("btn_details")
#         self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
#         # -------------------------------------------------------------
#         spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
#         self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
#         spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
#         self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
#         self.widget_2 = QtWidgets.QWidget(self)
#         self.widget_2.setMinimumSize(QSize(270, 220))
#         self.widget_2.setMaximumSize(QSize(270, 220))
#         self.widget_2.setStyleSheet("QWidget{\n"
# "background-color:rgba(130, 247, 255, 164);\n"
# "    border-radius:8px;\n"
# "    border:1px solid rgb(0, 0, 0);\n"
# "}")
#         self.widget_2.setObjectName("widget_2")
#         self.label_name_2 = QtWidgets.QLabel(self.widget_2)
#         self.label_name_2.setGeometry(QRect(70, 10, 101, 51))
#         self.label_name_2.setStyleSheet("QLabel{\n"
# "    background-color:rgba(34, 178, 221, 0);\n"
# "    font: 18pt \"黑体\";\n"
# "    color:rgb(0, 0, 127);\n"
# "    border:none;\n"
# "}")
#         self.label_name_2.setAlignment(Qt.AlignCenter)
#         self.label_name_2.setObjectName("label_name_2")
#         self.label_user_2 = QtWidgets.QLabel(self.widget_2)
#         self.label_user_2.setGeometry(QRect(20, 70, 221, 41))
#         self.label_user_2.setMinimumSize(QSize(0, 21))
#         self.label_user_2.setMaximumSize(QSize(16777215, 1990))
#         self.label_user_2.setStyleSheet("QLabel{\n"
# "    color: rgb(255, 255, 255);\n"
# "    background-color:gray;\n"
# "    font: 15pt \"黑体\";\n"
# "}")
#         self.label_user_2.setAlignment(Qt.AlignCenter)
#         self.label_user_2.setObjectName("label_user_2")
#         self.btn_update_2 = QtWidgets.QPushButton(self.widget_2)
#         self.btn_update_2.setGeometry(QRect(40, 170, 30, 30))
#         self.btn_update_2.setStyleSheet("QPushButton{\n"
# "    background-color: rgb(0, 255, 0);\n"
# "    border-radius:15px;\n"
# "}\n"
# "QPushButton:pressed{\n"
# "    background-color: rgb(0, 189, 0);\n"
# "}\n"
# "")
#         self.btn_update_2.setObjectName("btn_update_2")
#         self.btn_del_2 = QtWidgets.QPushButton(self.widget_2)
#         self.btn_del_2.setGeometry(QRect(170, 170, 30, 30))
#         self.btn_del_2.setStyleSheet("QPushButton{\n"
# "    color:rgb(255, 255, 255);\n"
# "    background-color: red;\n"
# "    border-radius:15px;\n"
# "}\n"
# "QPushButton:pressed{\n"
# "    background-color: rgb(170, 0, 0);\n"
# "}")
#         self.btn_del_2.setObjectName("btn_del_2")
#         self.label_pwd_2 = QtWidgets.QLabel(self.widget_2)
#         self.label_pwd_2.setGeometry(QRect(20, 111, 221, 41))
#         self.label_pwd_2.setMinimumSize(QSize(0, 21))
#         self.label_pwd_2.setMaximumSize(QSize(16777215, 1990))
#         self.label_pwd_2.setStyleSheet("QLabel{\n"
# "    color: rgb(255, 255, 255);\n"
# "    background-color:gray;\n"
# "    font: 15pt \"黑体\";\n"
# "}")
#         self.label_pwd_2.setAlignment(Qt.AlignCenter)
#         self.label_pwd_2.setObjectName("label_pwd_2")
#         self.btn_details_2 = QtWidgets.QPushButton(self.widget_2)
#         self.btn_details_2.setGeometry(QRect(90, 170, 61, 31))
#         self.btn_details_2.setStyleSheet("QPushButton{\n"
# "    font: 12pt \"黑体\";\n"
# "    color: rgb(255, 255, 255);\n"
# "    background-color: rgb(0, 85, 255);\n"
# "}\n"
# "QPushButton:pressed{\n"
# "    background-color: rgb(0, 0, 223);\n"
# "}")
#         self.btn_details_2.setObjectName("btn_details_2")
#         self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.retranslateUi()


    def addUser(self,name="lx",user="xxx",pwd="xxx"):
        info = {
            "name":name,
            "user":user,
            "pwd":pwd
        }

        self.widget = QtWidgets.QWidget(self)
        self.widget.setMinimumSize(QSize(270, 220))
        self.widget.setMaximumSize(QSize(270, 220))
        self.widget.setStyleSheet("QWidget{\n"
                                  "background-color:rgba(130, 247, 255, 164);\n"
                                  "    border-radius:8px;\n"
                                  "    border:1px solid rgb(0, 0, 0);\n"
                                  "}")
        self.widget.setObjectName("widget")
        label_name = QtWidgets.QLabel(self.widget)
        label_name.setGeometry(QRect(70, 10, 101, 51))
        label_name.setStyleSheet("QLabel{\n"
                                 "    background-color:rgba(34, 178, 221, 0);\n"
                                 "    font: 18pt \"黑体\";\n"
                                 "    color:rgb(0, 0, 127);\n"
                                 "    border:none;\n"
                                 "}")
        label_name.setAlignment(core_Qt.AlignCenter)
        label_name.setObjectName("label_name")
        label_name.setText(info.get("name",""))

        label_user = QtWidgets.QLabel(self.widget)
        label_user.setGeometry(QRect(20, 70, 221, 41))
        label_user.setMinimumSize(QSize(0, 21))
        label_user.setMaximumSize(QSize(16777215, 1990))
        label_user.setStyleSheet("QLabel{\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "    background-color:gray;\n"
                                 "    font: 15pt \"黑体\";\n"
                                 "}")
        label_user.setAlignment(core_Qt.AlignCenter)
        label_user.setObjectName("label_user")
        label_user.setText(info.get("user",""))

        btn_update = QtWidgets.QPushButton(self.widget)
        btn_update.setGeometry(QRect(40, 170, 30, 30))
        btn_update.setStyleSheet("QPushButton{\n"
                                 "    background-color: rgb(0, 255, 0);\n"
                                 "    border-radius:15px;\n"
                                 "}\n"
                                 "QPushButton:pressed{\n"
                                 "    background-color: rgb(0, 189, 0);\n"
                                 "}\n"
                                 "")
        btn_update.setObjectName("btn_update")
        btn_update.setText("U")

        btn_del = QtWidgets.QPushButton(self.widget)
        btn_del.setGeometry(QRect(170, 170, 30, 30))
        btn_del.setStyleSheet("QPushButton{\n"
                              "    color:rgb(255, 255, 255);\n"
                              "    background-color: red;\n"
                              "    border-radius:15px;\n"
                              "}\n"
                              "QPushButton:pressed{\n"
                              "    background-color: rgb(170, 0, 0);\n"
                              "}")
        btn_del.setObjectName("btn_del")
        btn_del.setText("D")

        label_pwd = QtWidgets.QLabel(self.widget)
        label_pwd.setGeometry(QRect(20, 111, 221, 41))
        label_pwd.setMinimumSize(QSize(0, 21))
        label_pwd.setMaximumSize(QSize(16777215, 1990))
        label_pwd.setStyleSheet("QLabel{\n"
                                "    color: rgb(255, 255, 255);\n"
                                "    background-color:gray;\n"
                                "    font: 15pt \"黑体\";\n"
                                "}")
        label_pwd.setAlignment(core_Qt.AlignCenter)
        label_pwd.setObjectName("label_pwd")
        label_pwd.setText(info.get("pwd",""))

        btn_details = QtWidgets.QPushButton(self.widget)
        btn_details.setGeometry(QRect(90, 170, 61, 31))
        btn_details.setStyleSheet("QPushButton{\n"
                                  "    font: 12pt \"黑体\";\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "    background-color: rgb(0, 85, 255);\n"
                                  "}\n"
                                  "QPushButton:pressed{\n"
                                  "    background-color: rgb(0, 0, 223);\n"
                                  "}")
        btn_details.setObjectName("btn_details")
        btn_details.setText("详情")

        self.gridLayout.addWidget(self.widget, *self.nextPos())

    def retranslateUi(self):
        self.setWindowTitle("用户管理")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = AccountSys()
    win.show()

    sys.exit(app.exec_())
    