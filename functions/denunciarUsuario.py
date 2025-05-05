import pyautogui

def denunciarUsuario(usuario):
    pyautogui.hotkey('right')
    pyautogui.write(usuario, interval=0.1)
    pyautogui.hotkey('ctrl', 'b')