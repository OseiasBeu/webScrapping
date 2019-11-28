import os
import errno
import glob 
import time 
import win32com.client    

def xlsx_to_xls(path):
    xlsx_files = glob.glob(path+'\\*.xlsx') 

    if len(xlsx_files) == 0: 
        raise RuntimeError('No XLSX files to convert.') 

    xlApp = win32com.client.Dispatch('Excel.Application') 

    for file in xlsx_files: 
        xlWb = xlApp.Workbooks.Open(os.path.join(os.getcwd(), file)) 
        xlWb.SaveAs(os.path.join(os.getcwd(), file.split('.xlsx')[0] + '.xls'), FileFormat=1) 
        xlWb.Close()

    xlApp.Quit() 

    time.sleep(2) # give Excel time to quit, otherwise files may be locked 
    for file in xlsx_files: 
        os.unlink(file) 

xlsx_to_xls('./')