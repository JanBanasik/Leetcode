import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(department, left_on = 'departmentId', right_on = 'id')
    merged.sort_values(by=['name_y', 'salary'], ascending =[True, False], inplace=True)
    print(merged)
    maxSalary = merged.groupby('departmentId')['salary'].transform('max')
    print(maxSalary)
    filtered = merged[merged['salary'] == maxSalary]
    
    res = filtered[['name_y', 'name_x', 'salary']]
    res.columns = ['Department', 'Employee', 'Salary']
    return res