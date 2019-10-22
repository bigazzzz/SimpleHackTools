#!/usr/bin/python
# -*- coding: utf-8 -*-
'''

Модуль с командами для клиентского backdoor

'''

def sysinfo():
    '''
    Вывод строчки с информацией об ОС
    '''
    return 'Информация о системе'

def help():
    '''
    Вывод строки со всеми функиями этого модуля с описаниями
    '''
    from inspect import isfunction

    functions_list = []
    for value in dir():
        func = getattr(this, value)
        print(func)
  #      if isfunction(func)
         #   functions_list.append(func)
        #


    print(functions_list)
    result = "Вы можете использовать следующие команды:\n"
    for f in functions_list:
      #  result += f[0] + '\n\t' + f[1].__doc__ + '\n'
    return result

print(help())
