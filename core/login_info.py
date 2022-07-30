
from core.utility import cu_time
from core.token import JWT


# 登录信息类
class LoginInfo:
    def __init__(self):
        self.__info = dict()
        self.__info['username'] = ''
        self.__info['password'] = ''
        self.__info['login_time'] = ''
        self.__info['login_ip'] = ''
        self.__info['login_port'] = ''
        self.__info['login_hostname'] = ''
        self.__info['login_token']:JWT=None

    def setInfo(self,username:str,password:str,login_token:JWT=None):
        self.__info['username'] = username
        self.__info['password'] = password
        self.__info['login_time'] = cu_time()
        self.__info['login_ip'] = ""
        self.__info['login_port'] = ""
        self.__info['login_hostname'] = ""
        self.__info['login_token'] = login_token

    def name(self)->str:
        return self.__info['username']

    def ip(self)->str:
        return self.__info['login_ip']

    def port(self)->str:
        return self.__info['login_port']


    def info(self)->dict:
        return self.__info