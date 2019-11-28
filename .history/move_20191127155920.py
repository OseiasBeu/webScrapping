import os, shutil, glob

src_fldr = r"/Users/beuo/Downloads/"
dst_fldr = 'C:\Users\beuo\Documents\Demandas\AtualizaMiddleIntegrationVtex\'

try:
  os.makedirs(dst_fldr)
except:
  print("erro")

for txt_file in glob.glob(src_fldr+"\\*.xlsx"):
    shutil.copy2(src_fldr,dst_fldr)
# shutil.move(src_fldr,dst_fldr)