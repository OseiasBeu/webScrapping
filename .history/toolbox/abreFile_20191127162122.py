import pandas as pd


def abreFile():
  wb = pd.ExcelFile('../files/*.xls')
  df = pd.read_excel(wb)
  print(df.head())
abreFile()