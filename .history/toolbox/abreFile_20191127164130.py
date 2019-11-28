import pandas as pd
from openpyxl import load_workbook
import os


def abreFile():
   
  oldAddres = 'C:/Users/beuo/Documents/Demandas/AtualizaMiddleIntegrationVtex/files/'
  newFile = 'C:/Users/beuo/Documents/Demandas/AtualizaMiddleIntegrationVtex/files/extract.xlsx'
  
  
  

  def encontraArquivosEmPastaRecursivamente(pasta, extensao):
      arquivosTxt = []
      caminhoAbsoluto = os.path.abspath(pasta)
      for pastaAtual, subPastas, arquivos  in os.walk(caminhoAbsoluto):
          arquivosTxt.extend([os.path.join(pastaAtual,arquivo) for arquivo in arquivos if arquivo.endswith('.xls')])
      return arquivosTxt

  # old = encontraArquivosEmPastaRecursivamente(oldAddres, '.xls')

  # print(old[0])
  # os.rename(old[0],newFile)
  
  # wb = pd.ExcelFile('20191127151150-export.xls')
  wb = load_workbook('20191127151150-export.xls')
  df = pd.read_excel(wb)
  print(df.head())

abreFile()      