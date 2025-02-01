import pandas as pd
df_parquet = pd.read_parquet('lesson-18/homework/flights/')
print(df_parquet[['Origin', 'Dest']])