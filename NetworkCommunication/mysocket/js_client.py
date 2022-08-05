# -*- coding:utf-8 -*-
# @time:2022/8/514:06
# @author:LX
# @file:js_client.py
# @software:PyCharm
'''
    jsm客户端
'''
import socket

host = "192.168.50.21"
port = 8004

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((host, port))
print("连接成功")
while True:
    data = input("请输入要发送的数据:")
    soc.send(data.encode())
    if data == "exit":
        break
    data = soc.recv(1024)
    print("接收到数据:", data.decode())