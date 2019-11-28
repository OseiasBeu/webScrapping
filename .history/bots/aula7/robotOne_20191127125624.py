# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd

print("INICIANDO NOSSO ROBÔ....")
arq = open("resultado.txt","w")

# LENDO EXCEL
dominios = []
workbook = xlrd.open_workbook('dominio.xlsx')
sheet = workbook.sheet_by_index(0)


for linha in range(0, 6):
    dominios.append(sheet.cell_value(linha, 0))
# print(sheet.cell_value(linha,0))

driver = webdriver.Chrome(
    '/home/oseiasbeu/Documentos/robots/aula7/chromedriver')
driver.get("https://registro.br/")

# dominios = ['roboscompython.com.br', 'uol.com.br','pythoncurso.com', 'udemy.com.br']
for dominio in dominios:
    pesquisa = driver.find_element_by_id("is-avail-field")
    pesquisa.clear()  # Limpando a barra de pesquisa
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(3)
    resultados = driver.find_elements_by_tag_name("strong")
    # import pdb; pdb.set_trace()
    # print(resultados[4].text)
    #print("Dominio %s %s" % (dominio, resultados[4].text))
    texto = "Dominio %s %s \n" % (dominio, resultados[4].text)
    arq.write(texto)

# time.sleep(2) #Dormindo
arq.close()
driver.close()
