# -*- coding: utf-8 -*-
'''
Usage:
    portscan_args.py [host] [ports]
Examples:
    portscan_args.py example.com 80
    portscan_args.py example.com,test.ru 80-85
    portscan_args.py example.com 22,80,443

Без аргументов скрипт запросит эти составляющие

'''
import socket
import sys

if len(sys.argv) > 1:
    hosts = sys.argv[1]
else:
    hosts = input("Хост(ы) => ")

hosts = hosts.split(',')

if len(sys.argv) > 2:
    ports = sys.argv[2]
else:
    ports = input("Порт(ы) => ")

ports = ports.split(',')
ports_list = []
for port in ports:
    port = str(port)
    port.strip()
    if port.find('-') >= 0:
        port_start = int(port.split('-')[0])
        port_end = int(port.split('-')[1])
        for i in range(port_start, port_end):
            ports_list.append(i)
        port = port_end
    ports_list.append(int(port))

print("\nLet\'s portscan begin")

for host in hosts:
    print('Исследуем хост ' + host)
    for port in ports_list:
        try:
            scan = socket.socket()
            scan.settimeout(0.5)
            scan.connect((host, port))
        except socket.error:
            print("\t- Порт {0} закрыт".format(port))
        else:
            print("\t+ Порт {0} открыт".format(port))
