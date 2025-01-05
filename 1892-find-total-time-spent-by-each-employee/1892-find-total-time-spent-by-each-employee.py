import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['time'] = employees['out_time'] - employees['in_time']
    newDf = employees.groupby(['emp_id', 'event_day'])['time'].sum('time').reset_index()
    newDf.columns = ['emp_id', 'day', 'total_time']
    return newDf[['day', 'emp_id', 'total_time']]