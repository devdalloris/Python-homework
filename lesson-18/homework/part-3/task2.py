import pandas as pd
df_titanic=pd.read_excel('lesson-18/homework/titanic.xlsx')
min_age=df_titanic[['Age']].min()
max_age=df_titanic[['Age']].max()
sum_age=df_titanic[['Age']].sum()
print(f'minimum {min_age}')
print(f'maxmum {max_age}')
print(f'sum {sum_age}')