# -*- coding:utf-8 -*-
# @time:2022/8/814:11
# @author:LX
# @file:agreement.py
# @software:PyCharm


'''
    协议类
    用于构建客户端与服务器信息交流的协议
'''
class  Agreement:
    def __init__(self,protocolType:str,data:dict):
        self.__protocolType = protocolType
        self.__data = data

    def protocolType(self)->str:
        return self.__protocolType

    def data(self)->dict:
        return self.__data

    # 返回客服端发送给服务器的协议
    def get_send_sever(self)->dict:
        return {
            "protocolType":self.protocolType(),
            "data":self.data()
        }

    # 返回服务器发送给客服端的协议
    def get_send_client(self,result:bool=None)->dict:
        return {
            "protocolType":self.protocolType(),
            "data":self.data(),
            "result":200 if result else 400
        }

def createAgreement(protocolType:str,data:dict,result:bool=None)->dict:
    if result is None:
        return Agreement(protocolType,data).get_send_sever()
    return Agreement(protocolType,data).get_send_client(result)