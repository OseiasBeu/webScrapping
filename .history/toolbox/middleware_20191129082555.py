# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import toolbox.sheets as sheet
import pandas as pd
import numpy as np


def middleware():
  driver = webdriver.Chrome(executable_path='chromedriver.exe')
  driver.get("https://wsmid-prd.whirlpool.com.br/manager/reports/frmQueryAnalyzer.aspx?menu=2")
  dominio = 'whirlpool'
  usuario = 'daniel_coelho'
  senha = 'Sua95xb4'
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
  
  coluna1 = coluna.pop(3)
  coluna1 = coluna1 +" "+ coluna.pop(3) 
  coluna1 = coluna1 +" "+ coluna.pop(3) 
  coluna.append(coluna1)
  
  
  
  df = pd.DataFrame(data=arr[4:], columns=coluna)
  
  # df = df.insert(0,'timeStamp')
  now = datetime.now()
  df['timeStamp'] = ''
  df1 = df.drop(columns='#')
  wb = pd.ExcelFile('base_middleware.xlsx')
  base_m = pd.read_excel(wb)
  # print(base_m.head())
  # print(df1.head())
  sheet.insertPlanMiddleware(df1)
  base_m['timeStamp'] = datetime.now().strftime('%m/%S/%Y %H:%M:%S')

  from openpyxl import load_workbook

  # new_row_data = [
  #   ['odhgos', 'e/p', 'dromologio', 'ora'],
  #   ['odigosou', 'dromou', 'dromologio', 'ora']]
  antes = np.asarray(df1)
  depois = np.asarray(base_m)

  wb = load_workbook("test/test.xlsx")
  # Select First Worksheet
  ws = wb.worksheets[0]

# Append 2 new Rows - Columns A - D
  for row_data in new_row_data:
    # Append Row Values
    ws.append(row_data)

  wb.save("test/test.xlsx")
  # print(df1)
  # antes = np.asarray(df1)
  # depois = np.asarray(base_m)
  # print(type(antes))
  # print(type(depois))

  # new_df = np.concatenate(antes,depois)

  # new_df = pd.DataFrame(antes)
  # df1.append(base_m)
  print(new_df)
  
  
 
  

  nomeArquivo = 'base_middleware.xlsx'
  new_df.to_excel(nomeArquivo, index=False)
  


  sair = driver.find_element_by_id("ctl00_lgStatus").click()

  driver.close()

  	# clienteEstado	warehouseId	Pendentes de integração	Última hora?