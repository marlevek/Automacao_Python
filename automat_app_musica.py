from time import sleep
import pyautogui as pya

pya.PAUSE = 1

pya.press('win')
sleep(0.5)
pya.write('tunein')
pya.press('enter')
