import pyautogui
import time

pyautogui.hotkey('alt','tab')
time.sleep(1)
pyautogui.hotkey('ctrl','f')
time.sleep(1)

pyautogui.write('http:', interval=0.1)
pyautogui.hotkey('ctrl','h')
pyautogui.write('https:', interval=0.1)
pyautogui.hotkey('ctrl', 'alt', 'enter')
time.sleep(1)

pyautogui.hotkey('ctrl','f')
pyautogui.write('https://www.kalunga.com.br/hotsite', interval=0.1)
pyautogui.hotkey('ctrl','h')
pyautogui.write('/hotsite', interval=0.1)
pyautogui.hotkey('ctrl', 'alt', 'enter')
time.sleep(1)

pyautogui.hotkey('ctrl','f')
pyautogui.write('/hotsite/loja-oficial-hp-promocoes', interval=0.1)
pyautogui.hotkey('ctrl','h')
time.sleep(1)
pyautogui.write('/prod/impressora-multifuncional-hp-smart-tank-581-tanque-de-tinta-4a8d5a-colorida-wi-fi-conexao-usb-bivolt-4a8d5a-hp-cx-1-un/220464')
pyautogui.hotkey('ctrl', 'alt', 'enter')
time.sleep(1)

pyautogui.hotkey('ctrl','f')
pyautogui.write('https://www.kalunga.com.br/', interval=0.1)
pyautogui.hotkey('ctrl','h')
pyautogui.write('/', interval=0.1)
pyautogui.hotkey('ctrl', 'alt', 'enter')
time.sleep(1)

pyautogui.hotkey('ctrl','f')
pyautogui.write('body', interval=0.1)
pyautogui.hotkey('ctrl','h')
pyautogui.write('div', interval=0.1)    
pyautogui.hotkey('ctrl', 'alt', 'enter')
time.sleep(1)