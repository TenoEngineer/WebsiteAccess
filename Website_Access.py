from platform import python_branch
from numpy import exp
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import os,sys
import root

root
periodo = list(root.getInput())[0]
cnpj = 'xxxxxxxxx'
senha = 'xxx'

navegador = webdriver.Firefox()
navegador.get('https://doisirmaos.atende.net/autoatendimento/servicos/acesso-ao-sistema-de-nota-fiscal-de-servico-eletronica/detalhar/1')
navegador.maximize_window()

#Propaganda
try:
    WebDriverWait(navegador, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.wpo-fechar:nth-child(1)'))).click()
except:
    time.sleep(2)
    navegador.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/button').click()

#acesso
time.sleep(1)
acesso=None
x=0
while acesso is None and x<10:
    acesso = pyautogui.locateOnScreen(f'{os.path.dirname(sys.argv[0])}/acesso.png',grayscale=True)
    if acesso!= None:
        point = pyautogui.center(acesso)
        pyautogui.click(point.x,point.y)
        break
    time.sleep(0.25)
    x+=1


time.sleep(0.5)
pyautogui.write(cnpj)
pyautogui.press('tab')
pyautogui.write(senha)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')

#Segunda_aba
time.sleep(3)
windows_2 = navegador.window_handles[-1]
time.sleep(0.5)
navegador.close()
navegador.switch_to.window(windows_2)
navegador.maximize_window()
time.sleep(1)
try: 
    location = pyautogui.locateOnScreen(f'{os.path.dirname(sys.argv[0])}/Nota fiscal.png',grayscale=True, confidence=.5)
    point = pyautogui.center(location)
    pyautogui.click(point.x,point.y)
except:
    location = pyautogui.locateOnScreen(f'{os.path.dirname(sys.argv[0])}/Nota fiscal2.png',grayscale=True, confidence=.5)
    point = pyautogui.center(location)
    pyautogui.click(point.x,point.y)
time.sleep(5)

try:
    location = pyautogui.locateOnScreen(f'{os.path.dirname(sys.argv[0])}/consulta.png',grayscale=True)
    point = pyautogui.center(location)
    pyautogui.moveTo(point.x,point.y)
    time.sleep(0.5)
    pyautogui.moveTo(point.x,point.y+30)
    pyautogui.click()
except:
    location = pyautogui.locateOnScreen(f'{os.path.dirname(sys.argv[0])}/consulta3.png',grayscale=True)
    point = pyautogui.center(location)
    pyautogui.moveTo(point.x,point.y)
    time.sleep(0.5)
    pyautogui.moveTo(point.x,point.y+20)
    pyautogui.click()

time.sleep(2)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write(periodo)

x=0
while x <10:
    pyautogui.press('tab')
    x+=1

pyautogui.write(cnpj)
try:
    location = pyautogui.locateOnScreen(f'{os.path.dirname(sys.argv[0])}/consultar.png', grayscale=True, confidence=.5)
    point = pyautogui.center(location)
    pyautogui.click(point.x,point.y)
except:
    location = pyautogui.locateOnScreen(f'{os.path.dirname(sys.argv[0])}/consultar2.png', grayscale=True, confidence=.5)
    point = pyautogui.center(location)
    pyautogui.click(point.x,point.y)
time.sleep(1)
pyautogui.scroll(-1000)