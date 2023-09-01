import pyautogui
import time
import datetime

date = datetime.datetime.now()
cont = 0 
pyautogui.hotkey('alt','tab')

while (cont < 5):
    pyautogui.hotkey('ctrl', 'shit', 'v')
    pyautogui.hotkey('alt', '[')
    pyautogui.hotkey('shift', 'left', 'left')
    pyautogui.hotkey('alt', 'up')
    pyautogui.hotkey('alt', '[')
    cont += 1
    time.sleep(1)

print(date.strftime("%H"), date.strftime("%M")) 
