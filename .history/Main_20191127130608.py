# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd


print ('Iniciando...')

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get(" https://wsmid-qa.whirlpool.com.br/manager/reports/frmQueryAnalyzer.aspx?menu=2")
dominio = driver.find_element_by_id("is-avail-field")
pesquisa.send_keys(dominio)
usuario =driver.find_element_by_id("is-avail-field")
pesquisa.send_keys(usuario)
senha = driver.find_element_by_id("is-avail-field")
pesquisa.send_keys(senha)

senha = driver.find_element_by_id("is-avail-field")
time.sleep(10)
driver.close()