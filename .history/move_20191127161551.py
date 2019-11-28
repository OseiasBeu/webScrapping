import os, shutil, glob


oldAddres = 'C:/Users/beuo/Downloads/'
newAdress = 'C:/Users/beuo/Documents/Demandas/AtualizaMiddleIntegrationVtex/files/'



def encontraArquivosEmPastaRecursivamente(pasta, extensao):
    arquivosTxt = []
    caminhoAbsoluto = os.path.abspath(pasta)
    for pastaAtual, subPastas, arquivos  in os.walk(caminhoAbsoluto):
        arquivosTxt.extend([os.path.join(pastaAtual,arquivo) for arquivo in arquivos if arquivo.endswith('.xls')])
    return arquivosTxt

encontraArquivosEmPastaRecursivamente(oldAddres, '.xls')












# try:
#   os.makedirs(dst_fldr)
# except:
#   print("erro")

# for xlsx_file in glob.glob(src_fldr+"//*.xlsx"):
#     shutil.copy2(src_fldr,dst_fldr)
