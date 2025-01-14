import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    newDf = orders.merge(company, on = 'com_id', how='inner')
    REDSalesPeople = newDf[newDf['name'] == 'RED']['sales_id'].tolist()
    result = sales_person[~sales_person['sales_id'].isin(REDSalesPeople)]
    return pd.DataFrame(result['name'])