from time import sleep
import pyautogui as pya

pya.PAUSE = 1

pya.press('win')
sleep(0.5)
pya.write('tunein')
pya.press('enter')

sleep(3)

pya.click(x=531, y=476, clicks=2)  # escolhendo a rádio LOVETIMES
sleep(1.5)

pya.click(x=1848, y=444)   # clicando para começar a tocar
sleep(2)

pya.click(x=1799, y=10)  # minimizando a janelae