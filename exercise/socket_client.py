#!/usr/bin/env python
# -*- coding:utf-8 -*-

#导入socket库
import socket

#创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#建立连接
s.connect(('www.baidu.com',80))

#终端输入netstat -ant |grep 80
#前面的IP地址 是本机的，后面的IP地址是指定网址的，如百度

#发送数据
s.send('GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection:close\r\n\r\n')
#L = 'GET /HTTP/1.1\r\nHost:www.baidu.com\r\nConnection:close\r\n\r\n'
#s.send(L)
#len(L)


#接收数据
buffer = []
while True:
    #每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)
print data
