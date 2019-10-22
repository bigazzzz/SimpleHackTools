#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.bind(('', 4444))
sock.listen(1)
# accept возвращает кортеж с двумя элементами: новый сокет и адрес клиента
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()