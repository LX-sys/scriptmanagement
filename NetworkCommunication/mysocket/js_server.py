# -*- coding:utf-8 -*-
# @time:2022/8/514:04
# @author:LX
# @file:js_server.py
# @software:PyCharm
'''
    jsm服务器
'''

import socket
import threading

# 类型
SOCKET = socket.socket

# host = "192.168.50.21"
host = "0.0.0.0"

port = 8005
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((host, port))
soc.listen(5)
print("服务器开始监听...")

def client_thread(conn:SOCKET,addr):
    while True:
        data = conn.recv(1024)
        if not data:
            print("{}客户端已断开".format(addr[0]))
            break
        print("[{}]接收到数据:{}".format(addr[0], data.decode()))
        conn.send(data)
    conn.close()

while True:
    conn, addr = soc.accept()
    print("连接地址:", addr,conn.getpeername())
    threading.Thread(target=client_thread, args=(conn,addr)).start()
