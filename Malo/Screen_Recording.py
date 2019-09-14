import numpy as np
import cv2
from PIL import ImageGrab
import datetime
import ctypes
import os
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

if os.path.exists("ScreenRecordings") is True:
    pass
else:
    os.makedirs("ScreenRecordings")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
DateAndTime = datetime.datetime.now().strftime("-%Y-%m-%d-%H-%M-%S")
out = cv2.VideoWriter("ScreenRecordings/Screen_Recording" + DateAndTime + ".avi", fourcc, 20.0, screensize)

while True:
    img = ImageGrab.grab()
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    out.write(frame)

    if cv2.waitKey(1) == 27:
        break

out.release()
