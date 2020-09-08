import pandas as pd
data_xls = pd.read_excel('usopen.xlsx', 'Sheet1', index_col=None)
data_xls.to_csv('usopentest.csv', encoding='utf-8')
