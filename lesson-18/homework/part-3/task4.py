import pandas as pd
df_parquet = pd.read_parquet('lesson-18/homework/flights/')
mean_df_parquet=df_parquet.select_dtypes('number').mean()
print(df_parquet.isna())
print(df_parquet.fillna(mean_df_parquet))