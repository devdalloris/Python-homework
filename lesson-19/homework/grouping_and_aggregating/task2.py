import pandas as pd
movies_data=pd.read_csv('data/movie.csv')
grouped_data = movies_data.groupby(['color', 'director_name']).agg({'num_critic_for_reviews': 'sum', 'duration': 'mean'})
grouped_data = grouped_data.rename(columns={'num_critic_for_reviews': 'Total Critic Reviews', 'duration': 'Average Duration'})
grouped_data = grouped_data.reset_index()
print(grouped_data)