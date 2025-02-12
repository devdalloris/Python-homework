import sqlite3
import pandas as pd
with sqlite3.connect('data/chinook.db') as connection:
    df_customers=pd.read_sql(
        'SELECT * FROM customers',
        con=connection
    )
    df_invoices=pd.read_sql(
        'SELECT * FROM invoices',
        con=connection
    )
print(df_customers.head(10))
print(df_invoices.head(10))
result = pd.merge(df_customers, df_invoices, on='CustomerId', suffixes=[None, '_other'])
print(result)
print(df_invoices['CustomerId'].value_counts())