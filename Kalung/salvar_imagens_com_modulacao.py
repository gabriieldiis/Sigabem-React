import pyautogui
import time

cont = 0 
teste = 200

def usar_tab():
    pyautogui.hotkey('alt' , 'tab')

def usar_f6():
    pyautogui.hotkey('ctrl' , 'f6')

def usar_f7():
    pyautogui.hotkey('ctrl', 'f7')

def sleep_1sec():
    time.sleep(1)

usar_tab()
while (cont < teste):
    sleep_1sec()
    usar_f6()
    usar_f7()
    sleep_1sec()
    cont += 1
    print(f'Contador está em {cont}')

print(f'replicação concluída!')