# -*- coding: utf-8 -*-
'''
Сканер проверяет один порт для одного хоста за один проход
Скрипт пытается подключится через сокет к порту
В случае ошибки возникает исключение, что говорит о закрытом порте
'''

import socket

host = input("Хост => ")
port = int(input("Порт => "))

print("\nLet\'s portscan begin")

try:
    scan = socket.socket()
    scan.connect((host, port))
except socket.error:
    print("- Порт {0} закрыт".format(port))
else:
    print("+ Порт {0} открыт".format(port))
