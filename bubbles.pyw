from ctypes import Structure, windll, c_uint, sizeof, byref

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0

import time
import os
bubbles = "C:\Windows\System32\Bubbles.scr"
running = False
sleepTime = 2 * 60 #2 minutes

while(True):
    if get_idle_duration() < sleepTime: #we need to wait
        time.sleep(sleepTime - get_idle_duration())
        running = False
    else:
        if running == False:
            running = True
            os.startfile(bubbles)
