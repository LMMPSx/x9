# Importando bibliotecas
import pyautogui
import ctypes

# ------------------------------------------------------------------------------------------
# Importando funções

from functions.abrirExcel import abrirExcel
from functions.selecionarCelula import selecionarCelula
from functions.salvarCPF import salvarCPF
from functions.validarCPF import validarCPF
from functions.abrirSigest import abrirSigest
from functions.pesquisarCadastro import pesquisarCadastro
from functions.esperarSigest import esperarSigest
from functions.verUsuario import verUsuario
from functions.denunciarUsuario import denunciarUsuario
from functions.proximoCadastro import proximoCadastro

# ------------------------------------------------------------------------------------------
# Configurações do PyAutoGUI
pyautogui.PAUSE = 0.75

cpf = ''
usuario = ''

# ------------------------------------------------------------------------------------------
# Início do programa

abrirExcel()

selecionarCelula()

while cpf != '-':
    cpf = salvarCPF()

    cpf = validarCPF(cpf)

    if cpf == '-':
        ctypes.windll.user32.MessageBoxW(0, "Demanda Finalizada", "Informação", 0x00001000 | 0x00000001)
        break

    abrirSigest()

    pesquisarCadastro(cpf)

    esperarSigest()

    usuario = verUsuario()

    abrirExcel()

    denunciarUsuario(usuario)

    proximoCadastro()