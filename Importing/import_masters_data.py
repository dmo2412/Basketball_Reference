import pandas as pd
from sqlalchemy import create_engine
import sqlite3

# connection = sqlite3.connect("firsty.db")
# cursor = connection.cursor()

xl_file = pd.ExcelFile('/Users/dannymorgan/Desktop/Masters_stats/masters_stats_2010_to_2019.xlsx')
# print(xl_file.sheet_names)

stats = xl_file.parse('Sheet1')

db_uri = 'sqlite:///testing2.db'
engine = create_engine(db_uri, echo=False)

sample_db = stats.to_sql('testingdb2', con=engine)
# sample_sql
sample_sql = engine.execute("SELECT * FROM testing2.db").fetchall()
print(sample_sql)
