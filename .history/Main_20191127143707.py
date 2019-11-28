# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd


print ('Iniciando...')


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://wsmid-qa.whirlpool.com.br/manager/reports/frmQueryAnalyzer.aspx?menu=2")
dominio = 'whirlpool'
usuario = 'daniel_coelho'
senha = '123456'
pendentes = 'Pendentes de integração'
bra = "BRA"
data = '2019-11-01' 
query = 'SELECT pedido.clienteEstado, pedidoItem.warehouseId, count(pedidoItem.warehouseId) as "{}" FROM pedido LEFT JOIN pedidoItem ON pedido.codigoPedido = pedidoItem.codigoPedido WHERE pedido.datahoracriacao > '{}' AND pedido.clientepais = 
{} AND pedido.flagIntegrado = 0 GROUP BY pedidoItem.warehouseId, pedido.clienteEstado ORDER BY {} DESC" .format(pendentes,bra,data,pendentes)

campo_dominio = driver.find_element_by_id("ucLogin1_txtDominio")
campo_dominio.send_keys(dominio)
campo_usuario =driver.find_element_by_id("ucLogin1_txtUser")
campo_usuario.send_keys(usuario)
campo_senha = driver.find_element_by_id("ucLogin1_txtPass")
campo_senha.send_keys(senha)
campo_senha.send_keys(Keys.RETURN)

text_query = driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtQuery")
text_query.send_keys(query)

print(query)
time.sleep(10)
driver.close()