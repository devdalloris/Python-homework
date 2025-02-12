import pandas as pd
df_titanic = pd.read_excel('data/titanic.xlsx')
def classify_age_group(age):
    if age < 18:
        return 'Child'
    else:
        return 'Adult'
df_titanic['Age_Group'] = df_titanic['Age'].apply(classify_age_group)
print(df_titanic.head()) 