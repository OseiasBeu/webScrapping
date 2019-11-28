# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import tempfile
import time
import shutil
import glob
import pandas as pd

def baixaArquivo():
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
  records.send_keys("Sem limite") #ctl00_ContentPlaceHolder1_imbExecutar
  text_query = driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtQuery")
  text_query.send_keys(query)
  executar = driver.find_element_by_id("ctl00_ContentPlaceHolder1_imbExecutar").click()
  time.sleep(5)
  


  # chrome_options = Options()
  # download_dir = tempfile.mkdtemp()
  # try:
  #   chrome_options.add_experimental_option('prefs', {
  #       "plugins.plugins_list": [{"enabled":False,"name":"Chrome PDF Viewer"}],
  #       "download": {
  #       "prompt_for_download": False,
  #       "default_directory"  : download_dir
  #       }
  #   })
  #   #...
  # 

  
  # while glob.iglob(os.path.join(download_dir, '*.crdownload')): 
  #   time.sleep(1)  # espera o download terminar
  #   # pega o 1o pdf que tiver, só terá 1 pois a pasta estava vazia antes:
  #   arquivo = glob.iglob(os.path.join(download_dir, '*.xlsx'))[0] 
  #   shutil.move(arquivo, r'C:\Users\beuo\Documents\Demandas\AtualizaMiddleIntegrationVtex\files\*.xlsx')
  # # finally:
  #   # shutil.rmtree(download_dir) # remove todos os arquivos temporários
  
  # exportar = driver.find_element_by_id("ctl00_ContentPlaceHolder1_imbExportExcel").click()
  arr = []
  resposta = driver.find_elements_by_tag_name('tr')
  # print(resposta.text)
  for item in range(len(resposta)):
    linha = resposta[item].text
    arr.append(linha.split())
    # print(linha.split())

  coluna = arr[3]
  print('Coluna inicial:'.format(coluna))
  coluna1 = coluna.pop(3)
  coluna1 = coluna1 +" "+ coluna.pop(3) 
  coluna1 = coluna1 +" "+ coluna.pop(3) 
# coluna1 = coluna.pop(5)
  coluna.append(coluna1)
  print('coluna: '.format(coluna))
  
  # print(arr[3][3])
  print(arr)

  # pd.DataFrame(data=data[1:,1:],columns=data[0,1:]))
  time.sleep(10)
  sair = driver.find_element_by_id("ctl00_lgStatus").click()
  

  
  time.sleep(10)

  driver.close()
