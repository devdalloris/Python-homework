import pandas as pd
import lxml
df_titanic=pd.read_excel('lesson-18/homework/titanic.xlsx')
df_filtered=df_titanic[df_titanic['Age']>30]
k=df_filtered['Sex'].value_counts()
print(df_filtered)
print(k['male'])
print(k['female'])