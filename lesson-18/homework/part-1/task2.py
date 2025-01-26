import pandas as pd
df_employee= pd.read_json('lesson-18/homework/iris.json')
print(df_employee.shape)
print(df_employee.columns)