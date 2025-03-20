import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['diff'] = employees['out_time'] - employees['in_time']
    grouped = employees.groupby(by=['emp_id', 'event_day']).sum('diff').reset_index()
    colNames = {'event_day': 'day', 'diff': 'total_time'}
    return grouped.rename(columns=colNames)[['day', 'emp_id', 'total_time']]