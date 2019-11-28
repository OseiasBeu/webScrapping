import pandas as pd
import os


def abreFile():
   
  oldAddres = 'C:/Users/beuo/Documents/Demandas/AtualizaMiddleIntegrationVtex/files/'
  
  
  

  def encontraArquivosEmPastaRecursivamente(pasta, extensao):
      arquivosTxt = []
      caminhoAbsoluto = os.path.abspath(pasta)
      for pastaAtual, subPastas, arquivos  in os.walk(caminhoAbsoluto):
          arquivosTxt.extend([os.path.join(pastaAtual,arquivo) for arquivo in arquivos if arquivo.endswith('.xls')])
      return arquivosTxt

  old_Addrres = encontraArquivosEmPastaRecursivamente(oldAddres, '.xls')
  print(old_Addrres[0])
  wb = pd.ExcelFile(oldAddres)
  df = pd.read_excel(wb)
  print(df.head())

abreFile()      