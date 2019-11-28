import shutil, glob

for txt_file in glob.glob(src_fldr+"\\.xlsx"):
    shutil.copy2(txt_file, dst_fldr);
shutil.move('/Users/beuo/Downloads/{*}.xlsx','/Users/beuo/Documents/Demandas/AtualizaMiddleIntegrationVtex/')