import pandas as pd
df_csv=pd.read_csv('data/movie.csv')
df_1=df_csv[['director_name', 'color']]
df_2=df_csv[['director_name', 'num_critic_for_reviews']]
left_join=pd.merge(df_1, df_2, on='director_name', how='left')
outer_join=pd.merge(df_1, df_2, on='director_name', how='outer')
print(left_join.shape[0])
print(outer_join.shape[0])