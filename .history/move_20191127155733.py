import os, shutil, glob

src_fldr = r"/Users/beuo/Downloads/"
dst_fldr = "/Users/beuo/Documents/Demandas/AtualizaMiddleIntegrationVtex/"; ## Edit this

try:
  os.makedirs(dst_fldr); ## it creates the destination folder
except:
  print("Folder already exist or some error")

for txt_file in glob.glob(src_fldr+"\\*.xlsx"):
    shutil.copy2(txt_file, dst_fldr);
shutil.move(src_fldr,dst_fldr)