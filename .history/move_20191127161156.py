import os, shutil, glob


oldAddres = 'C:/Users/beuo/Downloads/'
newAdress = 'C:/Users/beuo/Documents/Demandas/AtualizaMiddleIntegrationVtex/files/'
plan = glob.glob(oldAddres+"*.xlsx")
shutil.copy(plan, newAdress)














# try:
#   os.makedirs(dst_fldr)
# except:
#   print("erro")

# for xlsx_file in glob.glob(src_fldr+"//*.xlsx"):
#     shutil.copy2(src_fldr,dst_fldr)
