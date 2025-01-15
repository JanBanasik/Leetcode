import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managersCounted = employee.groupby('managerId').size().reset_index(name='reportsCount')
    managersCounted = managersCounted[managersCounted['reportsCount'] >= 5]
    return pd.DataFrame(employee[employee['id'].isin(managersCounted['managerId'].tolist())]['name'])