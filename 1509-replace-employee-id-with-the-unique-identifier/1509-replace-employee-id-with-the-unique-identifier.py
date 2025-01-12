import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    newDf = employees.merge(employee_uni, on='id', how='left')
    result = newDf[['unique_id', 'name']]
    result.rename(columns={'unique_id': 'id'})
    return result