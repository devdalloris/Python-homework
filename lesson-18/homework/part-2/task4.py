import pandas as pd
df_csv=pd.read_csv('lesson-18/homework/movie.csv')
df_filtered=df_csv[df_csv['duration']>120]
print(df_filtered.sort_values(by='director_facebook_likes', ascending=False))