# -*- coding:utf-8 -*-
# @time:2022/7/2318:23
# @author:LX
# @file:utility.py
# @software:PyCharm

# qt常用包
from PyQt5 import QtCore, QtGui, QtWidgets

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
    QScrollArea,
    QLineEdit,
    QCompleter,
    QListWidgetItem,
    QGridLayout,
    QTextEdit,
    QListWidget,
    QSpacerItem,
    QSizePolicy,
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
    Qt as core_Qt,
    QPoint
)

# python 内置库
import os
import sys
import time
from datetime import datetime as dt

# mysql数据库操作类
from databases.oper_mysql import SMJPersonalInfo

# 创建数据库
PersonalInfo = SMJPersonalInfo()

# 让数据只导入一次
def Mysql_PersonalInfo()->SMJPersonalInfo:
    return PersonalInfo


# 根路径,无论从那个文件运行,要保证文件路径是一样的
def rootPath()->str:
    z_path= os.getcwd().split("scriptmanagement")
    return os.path.join(z_path[0],"scriptmanagement")


# 组合路径
def joinPath(path:str)->str:
    return os.path.join(rootPath(),path)