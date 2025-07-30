import sqlite3
import pandas as pd

df = pd.read_csv('transactions.csv')
conn = sqlite3.connect(':memory:')
df.to_sql('transactions', conn, index=False, if_exists='replace')

query = """SELECT * FROM transactions WHERE amount > 10000;"""
results = pd.read_sql_query(query, conn)
print(results)