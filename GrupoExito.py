from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path= r'D:\Documents\Pruebas GrupoExito\chromedriver.exe')
driver.get("https://www.exito.com/")

#Ingresa a Mi Cuenta
# botonini = driver.find_element_by_xpath('//*[@id="header-container"]/div[2]/div[4]/div/div/div[1]/span')
# botonini.click()
# time.sleep(2)

#Crear cuenta
# ccuenta = driver.find_element_by_xpath('/html/body/div[11]/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[1]/ul/li[2]')
# ccuenta.click()

#Downlist
dwlista = driver.find_element_by_xpath('//*[@id="header-container"]/div[2]/div[3]/div/div[1]/div[1]/div[2]')
dwlista.click()
time.sleep(2)

#Seleccion Mercado
smerca = driver.find_element_by_xpath('//*[@id="mercado"]')
smerca.click()
time.sleep(2)

#Escribir Lechuga
eslechuga = driver.find_element_by_xpath('//*[@id="header-container"]/div[2]/div[3]/div/div[2]/div/div[1]/div/label')
eslechuga.send_keys('lechuga')

seleres = driver.find_element_by_xpathr('//*[@id="header-container"]/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div/section/section/a[5]')
seleres.click()
time.sleep(2)