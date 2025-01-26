import pandas as pd
df_movie=pd.read_csv('lesson-18/homework/movie.csv')
print(df_movie.sample(10))