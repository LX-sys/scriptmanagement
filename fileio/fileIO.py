# -*- coding:utf-8 -*-
# @time:2022/7/279:58
# @author:LX
# @file:fileIO.py
# @software:PyCharm

import os
import shutil


# 标准文件操作
from configparser import ConfigParser


class FileIO:
    # 文件操作
    def __init__(self, *args, **kwargs) -> None:
        self.__file_path = kwargs.get("file_path", None)

    # 设置文件路径
    def setFilePath(self, file_path:str) -> None:
        self.__file_path = file_path

    def filePath(self)->str:
        return self.__file_path

    def read(self, file_name:str=None,mode:str="r",encoding:str="utf8") -> str:
        '''
        读取文件
        :param file_name:
        :return:
        '''
        if file_name is None:
            file_name = self.filePath()
        temp_file = []
        with open(file_name, mode,encoding=encoding) as f:
            while True:
                data = f.read(2048)
                if data:
                    temp_file.append(data)
                else:
                    break
            return "".join(temp_file)

    # 读取一行
    def readLine(self,file_name:str=None,mode:str="r",encoding:str="utf8"):
        '''
        读取一行
        :return:
        '''
        if file_name is None:
            file_name = self.filePath()
        with open(file_name, mode,encoding=encoding) as f:
            return f.readline()

    def write(self, file_name:str=None, content:str=None,mode:str="w",encoding:str="utf8") -> None:
        '''
        写入文件
        :param file_name:
        :param content:
        :return:
        '''
        if file_name is None:
            file_name = self.__file_path

        with open(file_name, mode,encoding=encoding) as f:
            f.write(content)

    def append(self, file_name:str=None, content:str=None,mode:str="a",encoding:str="utf8") -> None:
        '''
        追加文件
        :param file_name:
        :param content:
        :return:
        '''
        if file_name is None:
            file_name = self.__file_path
        with open(file_name, mode,encoding=encoding) as f:
            f.write(content)

    @staticmethod
    def remove(file_name:str) -> None:
        '''
        删除文件
        :param file_name:
        :return:
        '''
        os.remove(file_name)

    def rename(self,old_name:str, new_name:str) -> None:
        '''
        重命名文件
        :param old_name:
        :param new_name:
        :return:
        '''
        os.rename(old_name, new_name)
        self.__file_path = new_name

    @staticmethod
    def copy(old_name:str, new_name:str) -> None:
        '''
        复制文件
        :param old_name:
        :param new_name:
        :return:
        '''
        shutil.copy(old_name, new_name)

    def move(self, old_name:str, new_name:str) -> None:
        '''
        移动文件
        :param old_name:
        :param new_name:
       '''
        # 移动文件位置
        self.rename(old_name, new_name)
        self.__file_path = new_name

    # 检测文件是否存在
    def isExist(self, file_name:str=None) -> bool:
        '''
        检测文件是否存在
        :param file_name:
        :return:
        '''
        if file_name is None:
            file_name = self.__file_path
        return os.path.exists(file_name)

    # 检测文件是否为空
    def isEmpty(self, file_name:str=None) -> bool:
        '''
        检测文件是否为空
        :param file_name:
        :return:
        '''
        if file_name is None:
            file_name = self.__file_path
        return os.path.getsize(file_name) == 0

    # 检测文件是否为文件夹
    def isDir(self, file_name:str=None) -> bool:
        '''
        检测文件是否为文件夹
        :param file_name:
        :return:
        '''
        if file_name is None:
            file_name = self.__file_path
        return os.path.isdir(file_name)

    # 获取文件大小
    def getSize(self, file_name:str=None) -> int:
        '''
        获取文件大小
        :param file_name:
        :return:
        '''
        if file_name is None:
            file_name = self.__file_path
        return os.path.getsize(file_name)

    # 获取文件权限
    def getPermission(self, file_name:str=None) -> int:
        '''
        获取文件权限
        :param file_name:
        :return:
        '''
        if file_name is None:
            file_name = self.__file_path
        return os.stat(file_name).st_mode

    # 获取目录下文件的数量
    def getFileCount(self, file_name:str=None) -> int:
        '''
        获取目录下文件的数量
        :param file_name:
        :return:
        '''
        if file_name is None:
            file_name = self.filePath()
        return len(os.listdir(file_name))

    # 获取目录下文件的名称
    def getFileName(self, file_name:str=None) -> list:
        '''
        获取目录下文件的名称
        :param file_name:
        :return:
        '''
        if file_name is None:
            file_name = self.filePath()
        return os.listdir(file_name)

    # 获取文件名称
    def getFileNameNoExtension(self, file_name:str=None) -> str:
        '''
        获取文件名称
        :param file_name:
        :return:
        '''
        if file_name is None:
            file_name = self.filePath()
        return os.path.basename(file_name)

# 配置文件操作
class FileConfig(FileIO):
    '''
        操作 .conf配置文件
    '''
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__config = ConfigParser()

    def read(self, file_name:str=None,mode:str="",encoding="utf8") -> None:
        '''
        读取配置文件
        :param file_name:
        :return:
        '''
        if file_name is None:
            file_name = self.filePath()
        self.__config.read(file_name,encoding=encoding)

    # 获取所有header
    def headers(self,file_name:str=None,encoding="utf8")->list:
        '''
        获取配置文件中的所有header
        :param file_name:
        :return:
        '''
        if file_name is None:
            file_name = self.filePath()
        self.read(file_name,encoding=encoding)
        return self.__config.sections()

    # 获取指定header下的所有配置项
    def get_value(self, header:str, key:str, file_name:str=None,encoding="utf8") -> str:
        '''
        获取配置文件中的值
        :param header:
        :param key:
        :param file_name:
        :return:
        '''
        if file_name is None:
            file_name = self.filePath()
        self.read(file_name,encoding=encoding)
        return self.__config.get(header, key)

    # 写配置文件
    def write(self, file_name:str=None,header:str=None,config:dict=None,mode:str="w",encoding="utf8") -> None:
        '''
        写入配置文件
        :param file_name:
        :return:
        '''
        if config is None or header is None:
            return None

        if file_name is None:
            file_name = self.filePath()
        with open(file_name,mode,encoding=encoding) as f:
            temp = []
            temp.append("[{}]".format(header))
            for key, value in config.items():
                temp.append("{}={}".format(key, value))
            f.write("\n".join(temp))



if __name__ == '__main__':
    file_io = FileConfig()
    file_io.setFilePath(r"D:\code\scriptmanagement\fileio\test\testl.conf")
    print(file_io.getFileNameNoExtension())