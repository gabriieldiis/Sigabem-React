import pyautogui
import time
import datetime

date = datetime.datetime.now()
cont = 0 
pyautogui.hotkey('alt','tab')

while (cont < 60):
    pyautogui.hotkey('f6')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'f7')
    cont += 1

print(date.strftime("%H"), date.strftime("%M")) 
