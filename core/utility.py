# -*- coding:utf-8 -*-
# @time:2022/7/2318:23
# @author:LX
# @file:utility.py
# @software:PyCharm

'''
    实用工具

'''

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
    QTextBrowser,
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
    QPoint,
    QSize,
    QRect
)
from PyQt5.QtNetwork import (
    QTcpSocket,
    QHostAddress
)

# python 内置库
import re
import os
import sys
import jwt
import time
import copy
import json
import typing
from datetime import datetime

import socket as SOCKET
from socket import socket

# mysql数据库操作类
from databases.oper_mysql import SMJPersonalInfo,CardInfo

# 创建数据库 smj_personal_info
PersonalInfo = SMJPersonalInfo()
# 创建数据库 card_info
cardInfo = CardInfo()


# 让数据库对象只导入一次
def Mysql_PersonalInfo()->SMJPersonalInfo:
    return PersonalInfo

def Mysql_cardInfo()->CardInfo:
    return cardInfo


# 根路径,无论从那个文件运行,要保证文件路径是一样的
def rootPath()->str:
    z_path= os.getcwd().split("scriptmanagement")
    return os.path.join(z_path[0],"scriptmanagement")


# win
def is_windows()->bool:
    return sys.platform == "win32" or sys.platform == "win64"


# linux
def is_linux()->bool:
    return sys.platform == "linux" or sys.platform == "linux2"


# mac
def is_mac()->bool:
    return sys.platform == "darwin"


# 比较路径是否相同
def compare_path(path1:str,path2:str)->bool:
    return os.path.normpath(path1) == os.path.normpath(path2)


# 组合路径
def joinPath(path:str,before_path:str=None)->str:
    if is_windows() and "/" in path:
        path = path.replace("/","\\")

    if is_mac():
       if "\\\\" in path:
            print("---")
            path = path.replace("\\\\","/")
       elif "\\" in path:
            print("===")
            path = path.replace("\\","/")
    if before_path:
        return os.path.join(before_path, path)
    else:
        return os.path.join(rootPath(),path)


# 运行python文件
def runPython(path:str,version:int=2)->None:
    if version==2:
        os.system("python2 {}".format(path))
    else:
        os.system("python3 {}".format(path))


# 将python2的print转换为python3的print
def py2_print_To_py3(py_file_path:str,encoding:str="utf8",file_cover=False)->str:
    '''
            将python2的print转换为python3的print
    :param py_file_path:
    :param encoding:
    :param file_cover: 不需要返回值,执行完毕后覆盖原文件
    :return:
    '''
    from fileio.fileIO import FileIO

    f = FileIO()
    pyfile = f.read(py_file_path,encoding=encoding) # 原文件代码
    temp = []
    no_bracket_print = re.findall("print.*",pyfile) # 没有括号的print
    bracket_data = re.findall("print(.*)",pyfile) # print 后面的数据
    for c in bracket_data:
        temp.append("print({})".format(c.strip()))
    # 替换
    for i in range(len(no_bracket_print)):
        upfile = pyfile.replace(no_bracket_print[i],temp[i])
        pyfile = upfile
    if file_cover:
        f.write(py_file_path,content=upfile,encoding=encoding)
    return  upfile if no_bracket_print else ""


# 获取当前时间
def cu_time()->str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


# TCP发送数据包装
def tcp_send(data,encoding="utf8")->bytes:
    return json.dumps(data).encode(encoding=encoding)

# Tcp接收数据包装
def tcp_recv(data:bytes,encoding="utf8")->dict:
    return json.loads(data.decode(encoding=encoding))