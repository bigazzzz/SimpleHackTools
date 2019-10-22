#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
from remotecommands import RemoteCommands

sock = socket.socket()
sock.bind(('', 4444))
sock.listen(1)
# accept возвращает кортеж с двумя элементами: новый сокет и адрес клиента
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    data = conn.recv(1024).decode('utf-8')

    if data == 'exit':
        break

    if hasattr(RemoteCommands, data) and not data.startswith('__'):
        data = getattr(RemoteCommands, data)()
    else:
        data = 'Такой команды нет. Наберите help для справки'
    conn.send(bytes(data, encoding='utf-8'))

conn.send(bytes("Работа завершена", encoding='utf-8'))
conn.close()
