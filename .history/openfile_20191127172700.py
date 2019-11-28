import xlrd
 
def xlread(arq_xls):
    #  abre o arquivo para leitura
    xls = xlrd.open_workbook(arq_xls)
    # pega a primeira linha do arquivo
    plan = xls.sheets()[0]
 
  
    for i in range(plan.nrows):
        # ler cada valor da linha
        yield plan.row_values(i)
 
for line in xlread('planilha.xls'):
    print(line)