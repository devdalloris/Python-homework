import pandas as pd
df_iris=pd.read_json('lesson-18/homework/iris.json')
new_columns=[column.lower() for column in df_iris.columns]
df_iris.columns=new_columns
sepal_length_and_sepal_width=df_iris[['sepallength','sepalwidth']]
print(sepal_length_and_sepal_width)