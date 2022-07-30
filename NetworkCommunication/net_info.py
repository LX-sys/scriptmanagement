# -*- coding:utf-8 -*-
# @time:2022/7/3011:24
# @author:LX
# @file:net_info.py
# @software:PyCharm
'''
    获取网络信息
'''
from core.utility import SOCKET,socket

class NetInfo(object):
    def __init__(self):
        pass

    def get_ip_address(self):
        '''
            获取本机ip地址
        :return:
        '''
        s = socket(SOCKET.AF_INET, SOCKET.SOCK_DGRAM)
        s.connect(('www.baidu.com', 80))
        ip = s.getsockname()
        s.close()
        return ip


if __name__ == '__main__':
    net_info = NetInfo()
    print(net_info.get_ip_address())
    # reset_machine(number="462", hostname="