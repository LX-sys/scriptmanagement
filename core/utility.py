# -*- coding:utf-8 -*-
# @time:2022/7/2318:23
# @author:LX
# @file:utility.py
# @software:PyCharm

# qt常用包
from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QProgressBar,
    QTabWidget,
    QDockWidget,
    QMainWindow,
    QMessageBox,
    QMenuBar,
    QMenu,
    QAction,
    QPushButton,
    QShortcut,
    QLabel,
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QVBoxLayout,
    QComboBox,
    QScrollArea
)
from PyQt5.Qt import (
    QThread,
    pyqtSignal,
    QMouseEvent,
    Qt as qt_Qt
)
from PyQt5.QtGui import (
    QKeySequence,
    QColor,
    QCursor
)
from PyQt5.QtCore import (
    Qt as coreQt,
    QPoint
)

# python 内置库
import sys
from datetime import datetime as dt

# mysql数据库操作类
from databases.oper_mysql import SMJPersonalInfo

# 创建数据库
PersonalInfo = SMJPersonalInfo()

# 让数据只导入一次
def Mysql_PersonalInfo()->SMJPersonalInfo:
    return PersonalInfo
