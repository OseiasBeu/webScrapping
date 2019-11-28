import os, shutil, glob

old_addres = "C:\Users\beuo\Downloads\".xlsx"
try:
  os.makedirs(dst_fldr)
except:
  print("erro")

for xlsx_file in glob.glob(src_fldr+"//*.xlsx"):
    shutil.copy2(src_fldr,dst_fldr)
