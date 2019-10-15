# -*- coding:utf -8 -*-
'''
Сканер проверяет несколько портов из стандартного списка
Скрипт пытается подключится через сокет к порту
В случае ошибки возникает исключение, что говорит о закрытом порте
'''
import socket

ports = [20, 21, 22, 23, 42, 43, 53, 67, 69, 80]

host = input("Хост => ")

print("\nLet\'s portscan begin")

for port in ports:
    try:
        scan = socket.socket()
        scan.settimeout(0.5)
        scan.connect((host, port))
    except socket.error:
        print("- Порт {0} закрыт".format(port))
    else:
        print("+ Порт {0} открыт".format(port))
