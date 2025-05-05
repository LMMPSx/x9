import pyautogui
import pyperclip

def salvarCPF():
    pyautogui.hotkey('ctrl', 'c')
    return pyperclip.paste().strip()