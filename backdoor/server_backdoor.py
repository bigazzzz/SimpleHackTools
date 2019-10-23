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
    data = conn.recv(1024).decode('utf-8').strip()
    if data.find(" ") == -1:
        command = data
        args = None
    else:
        command = data[:data.find(" ")]
        args = data[data.find(" "):].strip()

    if hasattr(RemoteCommands, command) and not command.startswith('__'):
        result = getattr(RemoteCommands, command)()
    else:
        result = 'Такой команды нет. Наберите help для справки'
    conn.send(bytes(result, encoding='utf-8'))
    if command == 'exit':
        break

conn.close()
