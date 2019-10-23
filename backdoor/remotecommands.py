#!/usr/bin/python
# -*- coding: utf-8 -*-

import inspect
import sys
import os
import platform

class RemoteCommands:
    '''
    Модуль с командами для клиентского backdoor
    '''

    def help():
        '''
        Вывод строки со всеми функиями этого модуля с описаниями
        '''

        result = "Вы можете использовать следующие команды:\n"
        functions = inspect.getmembers(RemoteCommands, inspect.isfunction)
        for f in functions:
            result += f[0] + ' - ' + f[1].__doc__.strip() + '\n'
        return result

    def sysinfo():
        '''
        Вывод строчки с информацией об ОС
        '''
        result = 'Информация о системе\n'
        result += 'platform - ' + sys.platform + '\n'
        result += 'ОС - ' + platform.platform() + ' ' + platform.architecture()[0] + '\n'
        if sys.platform == 'win32':
            result += 'Windows -' + str(sys.getwindowsversion()) + '\n'
        result += 'Хост - ' + platform.node() + '\n'
        result += 'CPU - ' + platform.processor() + '\n'

        return result

    def shortinfo():
        '''
        Краткая информация о хосте
        '''
        return str(platform.uname())

    def pythoninfo():
        '''
        Вывод строчки с информацией об установленной версии python
        '''
        return sys.version

    def path():
        '''
        Вывод текущего пути
        '''
        return os.getcwd()

    def exit():
        '''
        Выход
        '''
        return "Работа завершена"

if __name__ == "__main__":
    print(RemoteCommands.help())