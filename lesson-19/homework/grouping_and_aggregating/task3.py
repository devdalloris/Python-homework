import pandas as pd
flights_data=pd.read_parquet('data/flights')
grouped_data = flights_data.groupby(['Year', 'Month']).agg({
    'Year': 'count',
    'ArrDelay': 'mean',
    'DepDelay': 'max'
})
grouped_data = grouped_data.rename(columns={'Year': 'Total Flights', 'ArrDelay': 'Average Arrival Delay', 'DepDelay': 'Max Departure Delay'})

grouped_data = grouped_data.reset_index()
print(grouped_data)