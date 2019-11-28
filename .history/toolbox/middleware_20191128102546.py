# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# import os
from datetime import datetime
# import time
import sheets as sheet
import pandas as pd

def middleware():
  driver = webdriver.Chrome(executable_path='chromedriver.exe')
  driver.get("https://wsmid-qa.whirlpool.com.br/manager/reports/frmQueryAnalyzer.aspx?menu=2")
  dominio = 'whirlpool'
  usuario = 'daniel_coelho'
  senha = '123456'

  bra = "BRA"
  data = '2019-11-01' 
  query = "SELECT pedido.clienteEstado, pedidoItem.warehouseId, count(pedidoItem.warehouseId) as [Pendentes de integração] FROM pedido LEFT JOIN pedidoItem ON pedido.codigoPedido = pedidoItem.codigoPedido WHERE pedido.datahoracriacao > '{}' AND pedido.clientepais = '{}' AND pedido.flagIntegrado = 0 GROUP BY pedidoItem.warehouseId, pedido.clienteEstado ORDER BY [Pendentes de integração] DESC".format(data,bra)
  campo_dominio = driver.find_element_by_id("ucLogin1_txtDominio")
  campo_dominio.send_keys(dominio)
  campo_usuario =driver.find_element_by_id("ucLogin1_txtUser")
  campo_usuario.send_keys(usuario)
  campo_senha = driver.find_element_by_id("ucLogin1_txtPass")
  campo_senha.send_keys(senha)
  campo_senha.send_keys(Keys.RETURN)
  records =driver.find_element_by_id("ctl00_ContentPlaceHolder1_dropRows")
  
  text_query = driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtQuery")
  text_query.send_keys(query)
  executar = driver.find_element_by_id("ctl00_ContentPlaceHolder1_imbExecutar").click()

  arr = []
  resposta = driver.find_elements_by_tag_name('tr')
 
  for item in range(len(resposta)):
    linha = resposta[item].text
    arr.append(linha.split())
   
  coluna = arr[3]
  
  coluna1 = coluna.pop(3)
  coluna1 = coluna1 +" "+ coluna.pop(3) 
  coluna1 = coluna1 +" "+ coluna.pop(3) 
  coluna.append(coluna1)
  
  
  
  df = pd.DataFrame(data=arr[4:], columns=coluna)
  
  df = df.insert(0,'timeStamp')
  df['timeStamp'] = datetime.now()
  df1 = df.drop(columns='#')
  # df1 = df[['timeStamp','clienteEstado','warehouseId','Pendentes de integração']]
  
  print(df1)


  sair = driver.find_element_by_id("ctl00_lgStatus").click()

  driver.close()