from bs4 import BeautifulSoup
import pandas as pd

table = BeautifulSoup(open('20191127151150-export.html','r').read()).find('table')
df = pd.read_html(table)

print(df)