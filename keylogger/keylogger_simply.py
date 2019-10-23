#!/usr/bin/python
# -*- coding: utf-8 -*-

import pythoncom
import pyHook

def OnKeyboardEvent(event):
    print ('MessageName:',event.MessageName) # описание события
    print ('Message:',event.Message)
    print ('Time:',event.Time) #
    print ('Window:',event.Window)
    print ('WindowName:',event.WindowName) # имя приложения
    print ('Ascii:', event.Ascii, chr(event.Ascii)) # код
    print ('Key:', event.Key) # клавиша
    print ('KeyID:', event.KeyID) # Код клавиши
    print ('ScanCode:', event.ScanCode)
    print ('Extended:', event.Extended)
    print ('Injected:', event.Injected)
    print ('Alt', event.Alt)
    print ('Transition', event.Transition)
    print ('---')

    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.KeyUp = OnKeyboardEvent
    hm.HookKeyboard()
try:
    pythoncom.PumpMessages()
except KeyboardInterrupt:
    pass