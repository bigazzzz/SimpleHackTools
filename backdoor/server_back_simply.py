#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

host = input("Хост (localhost)=>")
if host == '':
    host = 'localhost'
port = input("Порт (4444)=>")
if port == '':
    port = '4444'
port = int(port)
request = input("Запрос (hello)=>")
if request == '':
    request = 'hello'
sock = socket.socket()
sock.connect((host, port))
sock.send(bytes(request, encoding='utf-8'))

data = sock.recv(1024)
sock.close()

print(data.decode('utf-8'))
