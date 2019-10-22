#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import remotecommands as command

sock = socket.socket()
sock.bind(('', 4444))
sock.listen(1)
# accept возвращает кортеж с двумя элементами: новый сокет и адрес клиента
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    data = conn.recv(1024)
    print(data.decode('utf-8'))
    if data == b'exit':
        break

 #   try:
    func = getattr(command,data)
    data = func()
    #except:
    #    data = 'Такой команды нет. Наберите help для справки'
    conn.send(bytes(data, encoding='utf-8'))

conn.send(bytes("Работа завершена", encoding='utf-8'))
conn.close()
