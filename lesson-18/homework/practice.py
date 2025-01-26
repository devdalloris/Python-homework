import pandas as pd
data = [
    ['John', 'Doe', 40],
    ['Jone', 'Doe', 44],
    ['Adam', 'Smith', 40]
]
columns=['Firtname', 'Lastname', 'Age']
df=pd.DataFrame(data=data, columns=columns)
print(df)