import pandas as pd


def abreFile():
  wb = pd.ExcelFile('*.xls')
  df = pd.read_excel(wb)
  print(df.head())
abreFile()