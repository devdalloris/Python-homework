import sqlite3
import pandas as pd
with sqlite3.connect('lesson-18/homework/chinook.db') as connection:
    df_customers=pd.read_sql(
        'SELECT * FROM customers',
        con=connection
    )
print(df_customers.head(10))