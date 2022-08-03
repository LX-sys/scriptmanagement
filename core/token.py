# -*- coding:utf-8 -*-
# @time:2022/7/2513:38
# @author:LX
# @file:token.py
# @software:PyCharm
'''

    生成token
'''

from core.utility import time

from core.utility import (
    QThread,
    QMainWindow
)

from core.utility import jwt

class JWT:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.secret = "secret"
        self.__payload = dict()
        self.__token = ""

    # 设置数据库
    def setData(self, data:dict) -> None:
        self.__payload = data

    def token(self) -> str:
        return self.__token

    def encode(self, data:dict=None) -> str:
        if data is None:
            data = self.__payload
        self.__token = jwt.encode(data, self.secret, algorithm='HS256')
        return self.__token

    def decode(self, token:str=None) -> dict:
        '''
        解析token
        :param token:
        :return:
        '''
        if token is None:
            token = self.__token
        return jwt.decode(token, self.secret, algorithms=['HS256'])

    def verify(self, token:str) -> bool:
        '''
        验证token
        :param token:
        :return:
        '''
        try:
            jwt.decode(token, self.secret, algorithms=['HS256'])
            return True
        except:
            return False

# 生成一个字典，包含我们的具体信息
d = {
    # 公共声明
    'exp': time.time() + 60*60*2,  # (Expiration Time) 此token的过期时间的时间戳
    'iat': time.time(),  # (Issued At) 指明此创建时间的时间戳
    'iss': 'LX',  # token的签发者

    # 私有声明
    'data': {
        'username': 'lx',
        "pwd": "123456",
        'timestamp': time.time()
    }
}


# 监视token的线程 stackedWidget
class QtJWT(QThread):
    def __init__(self,win:QMainWindow,jwt:JWT, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__win = win
        self.__jwt = jwt


    def run(self):
        while True:
            if not self.__jwt.verify(self.__jwt.token()):
                print("token失效")
                # 弹窗提示(这句话会导致界面卡死)
                # QMessageBox.warning(self.__win, "警告", "登录已过期,请重新登录!", QMessageBox.Yes, QMessageBox.Yes)
                self.__win.stackedWidget.setCurrentIndex(1)
                break
            self.sleep(2)



# myjwt = JWT()
# myjwt.setData(d)
# myjwt.encode()
# print(myjwt.decode())
# print(myjwt.verify(myjwt.token()))
# 打印token串
# print(__jwt.decode(jwt_encode, '123456', issuer='LX',  algorithms=['HS256']))


# import requests
# import json
# from requests.auth import HTTPBasicAuth
# header={
# "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
# "Accept":"application/json, text/plain, */*",
# "Accept-Encoding":"gzip, deflate, sdch",
# "Accept-Language":"zh-CN,zh;q=0.8",
# "Connection":"keep-alive",
# "Host":"panda.vqmjc.cc",
# "Referer":"http://panda.vqmjc.cc/",
# "Upgrade-Insecure-Requests":"1",
# "Cookie":"_fbp=fb.1.1649571363075.1222574223; _ga_GS0KJP7XQZ=GS1.1.1650590917.1.0.1650590921.0; _ga_CMNH37RCF4=GS1.1.1651042895.1.0.1651042905.0; _ga_3F27FB26WK=GS1.1.1651740875.1.1.1651741558.0; _tt_enable_cookie=1; _ttp=3e4e09eb-292e-41e7-975a-37776f8085f6; initialTrafficSource=utmccn=(not set); _ga_TEQK9M04ED=GS1.1.1652152149.1.0.1652152172.0; _ga_N4KKZKC6TZ=GS1.1.1652781741.4.0.1652781750.0; _ivu=0BB195C3-1CE2-4D63-B3FA-D02533693499; _vwo_uuid=D0B0C1A2AD474D47EB8284C52289F0A16; _vwo_ds=3:a_1,t_1:0$1652926949:51.71538321:::3_1,2_1:1; _cq_duid=1.1652942740.63g5DDlLcPMpi3jO; _atcid=EeKMSXH8SiZR3N; _atcid-pt=1652950851763; _ga_TZBT6VFDLS=GS1.1.1653017418.4.0.1653017418.0; _vis_opt_s=2|; _ce.s=v~3db06d01c154e0a7d1a6f01cd1f4b80f88d62da4~vpv~1; _ga_3RSTQ8PEQ2=GS1.1.1655687357.3.0.1655687357.60; _lc2_fpi=37dabcc9a3d0--01g65bk5s81wrc51424bqfjc41; _vwo=ts~o6a_gg7(MR0)k~*(MR0; _clck=jwt1nm|1|f2m|0; _ga_PC6DJ10JX3=GS1.1.1657590484.2.0.1657590498.0; _gcl_au=1.1.1580680699.1657612159; _ga=GA1.2.770677172.1649571362; _uetvid=a92ed3c0d68b11ecb4e66b74f3e50544"
# }
# # po=requests.session().post("http://panda.vqmjc.cc/panda_web/users/users/login",headers=header,data={"user_name":"haian_lx","user_pwd":"123456"})
# data = json.dumps({"username":"haian_lx","password":"123456"})
# po = requests.post("http://panda.vqmjc.cc/panda_web/users/users/login",headers=header,data=data,verify=False)
# print(po)
# print(po.text)