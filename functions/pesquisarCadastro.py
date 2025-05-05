import pyautogui

def pesquisarCadastro(cpf):
    pyautogui.click(x=98, y=251, duration=0.5)
    pyautogui.click(x=541, y=318, duration=0.5)
    pyautogui.write(cpf, interval=0.1)
    pyautogui.click(x=1114, y=374, duration=0.5)