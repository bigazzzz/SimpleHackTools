#!/usr/bin/python
# -*- coding: utf-8 -*-

import inspect
import sys

class RemoteCommands:
    '''
    Модуль с командами для клиентского backdoor
    '''

    def help():
        '''
        Вывод строки со всеми функиями этого модуля с описаниями
        '''

        result = "Вы можете использовать следующие команды:\n"
        functions = inspect.getmembers(RemoteCommands, inspect.isfunction);
        for f in functions:
            result += f[0] + '\n\t' + f[1].__doc__.strip() + '\n'
        return result

    def sysinfo():
        '''
        Вывод строчки с информацией об ОС
        '''
        return 'Информация о системе'

    def pythoninfo():
        '''
        Вывод строчки с информацией об установленной версии python
        '''
        return(sys.version)


if __name__ == "__main__":
    print(RemoteCommands.help())