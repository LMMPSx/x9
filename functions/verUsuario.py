import pyautogui
import pyperclip

def verUsuario():
    pyautogui.click(x=359, y=788, duration=0.5)
    pyautogui.click(x=1428, y=606, duration=0.5)
    pyautogui.click(x=1194, y=273, duration=0.5)
    
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shiftright')
    pyautogui.keyDown('shiftleft')
    for i in range(2):
        pyautogui.hotkey('right')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shiftright')
    pyautogui.keyUp('shiftleft')

    pyautogui.hotkey('ctrl', 'c')

    pyautogui.click(x=400, y=521, duration=0.5)
    pyautogui.click(x=396, y=790, duration=0.5)
    pyautogui.click(x=1040, y=595, duration=0.5)
    pyautogui.click(x=583, y=788, duration=0.5)

    return pyperclip.paste()