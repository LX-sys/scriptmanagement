# -*- coding:utf-8 -*-
# @time:2022/7/213:17
# @author:LX
# @file:tt.py
# @software:PyCharm
import sys
import typing
import time
from PyQt5.QtCore import QPoint, QThread, QObject
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar
from PyQt5 import QtCore, QtGui, QtWidgets

class ProgressBarThread(QThread):

    def __init__(self,progressbar:QProgressBar, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.progressbar = progressbar
        print(self.progressbar.maximum())

    def run(self):
        while True:
            max_num = self.progressbar.value()
            if max_num == self.progressbar.maximum():
                break
            else:
                self.progressbar.setValue(max_num+1)
            # self.sleep() # 秒
            # self.msleep(300) # 豪毫（不能低于250）
            # self.usleep(100) # 微毫


class MyQProgressBar(QProgressBar):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)

        self.setMaximum(100)
        self.setValue(0)
        # 内置qt线程
        self.built_thread = ProgressBarThread(self)

    def start(self):
        self.built_thread.start()


class Test(QWidget):
    def __init__(self, *args,**kwargs) -> None:
        super().__init__(*args,**kwargs)

        self.s = MyQProgressBar(self)
        self.s.setValue(24)
        self.s.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = Test()
    win.show()

    sys.exit(app.exec_())
