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
campo_dominio = driver.find_element_by_id("is-avail-field")
campo_dominio.send_keys(dominio)
campo_usuario =driver.find_element_by_id("is-avail-field")
campo_usuario.send_keys(usuario)
campo_senha = driver.find_element_by_id("is-avail-field")
campo_senha.send_keys(senha)

pesquisa.send_keys(Keys.RETURN)
senha = driver.find_element_by_id("is-avail-field")
time.sleep(10)
driver.close()