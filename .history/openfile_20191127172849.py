import xlrd
 
def xlread('20191127151150-export.xls'):
    #  abre o arquivo para leitura
    xls = xlrd.open_workbook(arq_xls)
    # pega a primeira linha do arquivo
    plan = xls.sheets()[0]
 
  
    for i in range(plan.nrows):
        # ler cada valor da linha
        yield plan.row_values(i)
 



