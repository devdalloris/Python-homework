import pandas as pd
df_titanic = pd.read_excel('data/titanic.xlsx')
grouped_data = df_titanic.groupby('Pclass').agg({'Age': 'mean', 'Fare': 'sum', 'PassengerId': 'count'})
grouped_data = grouped_data.rename(columns={'Age': 'Average Age', 'Fare': 'Total Fare', 'PassengerId': 'Passenger Count'})
new_df = grouped_data.reset_index()
print(new_df)