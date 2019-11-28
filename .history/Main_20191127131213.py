# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd


print ('Iniciando...')


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get(" https://wsmid-qa.whirlpool.com.br/manager/reports/frmQueryAnalyzer.aspx?menu=2")
dominio = 'whirlpool'
usuario = 'daniel_coelho'
senha = '123456'

campo_dominio = driver.find_element_by_id("ucLogin1_txtDominio")
campo_dominio.send_keys(dominio)
campo_usuario =driver.find_element_by_id("ucLogin1_txtUser")
campo_usuario.send_keys(usuario)
campo_senha = driver.find_element_by_id("ucLogin1_txtPass")
campo_senha.send_keys(senha)
campo_senha.send_keys(Keys.RETURN)

time.sleep(10)
driver.close()