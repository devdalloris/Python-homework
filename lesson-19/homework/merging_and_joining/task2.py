import pandas as pd
employee_data = pd.read_csv('data/employee.csv')
def normalize_salary(group):
    group['Normalized_Salary'] = (group['Salary'] - group['Salary'].min()) / (group['Salary'].max() - group['Salary'].min())
    return group
employee_data = employee_data.groupby('Department').apply(normalize_salary)
print(employee_data.head()) 