# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import toolbox.sheets as sheet
import pandas as pd


def integracoes_h():
  driver = webdriver.Chrome(executable_path='chromedriver.exe')
  driver.get("https://wsmid-qa.whirlpool.com.br/manager/reports/frmQueryAnalyzer.aspx?menu=2")
  dominio = 'whirlpool'
  usuario = 'daniel_coelho'
  senha = '123456'
  bra = "BRA"
  data = '2019-11-01' 
  query = "SELECT Cast(Day(datahoraprocessamento) AS VARCHAR(2)) +'/'+ Cast(Month(datahoraprocessamento) AS VARCHAR(2)) + '/' + Cast(Year(datahoraprocessamento) AS VARCHAR(4)) AS Data, Datepart(hour, datahoraprocessamento)AS Hora, Count(0) AS QtdPedidosVtexMdw FROM pedido WHERE ( datahoraprocessamento >= '2019-11-27 14:00:00' ) GROUP  BY Cast(Day(datahoraprocessamento) AS VARCHAR(2))  + '/' + Cast(Month(datahoraprocessamento) AS VARCHAR(2)) + '/'+ Cast(Year(datahoraprocessamento) AS VARCHAR(4)), Datepart(hour, datahoraprocessamento) ORDER  BY Cast(Day(datahoraprocessamento) AS VARCHAR(2)) + '/' + Cast(Month(datahoraprocessamento) AS VARCHAR(2)) + '/' + Cast(Year(datahoraprocessamento) AS VARCHAR(4)) DESC, Datepart(hour, datahoraprocessamento) DESC " #.format(data)
  campo_dominio = driver.find_element_by_id("ucLogin1_txtDominio")
  campo_dominio.send_keys(dominio)
  campo_usuario =driver.find_element_by_id("ucLogin1_txtUser")
  campo_usuario.send_keys(usuario)
  campo_senha = driver.find_element_by_id("ucLogin1_txtPass")
  campo_senha.send_keys(senha)
  campo_senha.send_keys(Keys.RETURN)
  records = driver.find_element_by_id("ctl00_ContentPlaceHolder1_dropRows")
  records.send_keys('sem limites')
  
  text_query = driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtQuery")
  text_query.send_keys(query)
  executar = driver.find_element_by_id("ctl00_ContentPlaceHolder1_imbExecutar").click()

  arr = []
  resposta = driver.find_elements_by_tag_name('tr')
 
  for item in range(len(resposta)):
    linha = resposta[item].text
    arr.append(linha.split())
   
  coluna = arr[3]
  print(coluna)
  df = pd.DataFrame(data=arr[4:], columns=coluna)
  sheet.insertPlanIntegracoes_h(df)
  sair = driver.find_element_by_id("ctl00_lgStatus").click()
  print(df)
  # driver.close()

# integracoes_h()