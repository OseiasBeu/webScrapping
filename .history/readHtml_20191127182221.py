from bs4 import BeautifulSoup
import pandas as pd

table = BeautifulSoup(open('C:/age0.html','r').read()).find('table')
df = pd.read_html(table)