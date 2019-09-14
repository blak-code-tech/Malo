import pyautogui
import time
import os
import datetime


if os.path.exists("ScreenShots") is True:
    pass
else:
    os.makedirs("ScreenShots")

DateAndTime = datetime.datetime.now().strftime("-%Y-%m-%d-%H-%M-%S")
pyautogui.grab('Screenshots/ScreenShot'+str(DateAndTime)+'.png')
time.sleep(1)
