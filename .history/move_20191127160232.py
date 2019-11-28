import os, shutil, glob

src_fldr = r"C:/Users/beuo/Downloads/"
dst_fldr = 'C:/Users/beuo/Documents/Demandas/AtualizaMiddleIntegrationVtex/files'

try:
  os.makedirs(dst_fldr)
except:
  print("erro")

for xlsx_file in glob.glob(src_fldr+"//*.xlsx"):
    shutil.copy2(src_fldr,dst_fldr)
