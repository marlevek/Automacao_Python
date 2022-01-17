import pyautogui
import pyperclip
from time import sleep

# Deixando uma pausa entre cada linha de código
pyautogui.PAUSE = 1

# 1. abrindo iniciar para digitar no campo de busca
pyautogui.press('win')

# 2. Digitando no campo de busca
pyautogui.write('whatsapp')
sleep(1)  # 1s para dar tempo de escrever e abrir o app

# 3. Abrindo o aplicativo
pyautogui.press('enter')
sleep(8)
#-------------------------- SE QUISER ENVIAR UMA MSG PARA ALGUÉM --------------------------

# Escolhendo o contato. 
#sleep(4)  # tempo de 4s para poder posicionar o mouse sobre o contato
#print(pyautogui.position())  # imprimindo a posição do contato 
pyautogui.click(x=244, y=598)

# escrevendo a msg. Note que não precisa pegar a posição do campo onde escreve a msg pois ele é selecionado automaticamente quando se clica no contato
msg = 'Bom dia minha filha, tudo bem por aí?'
pyperclip.copy(msg)  # como a msg tem caracteres especiais (acento, ?) é necessário usar o pyperclip, e depois colar com o pyautogui, senão o texto fica sem os caracteres especiais
pyautogui.hotkey('ctrl', 'v')
sleep(3)

# enviando a msg
#print(pyautogui.position())
pyautogui.click(x=1886, y=997)

