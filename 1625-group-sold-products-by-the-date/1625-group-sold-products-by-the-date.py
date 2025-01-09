import pandas as pd

def my_function(group):
    p = [x for x in group['product']]
    group['num_sold'] = len(p)
    group['products'] = ",".join(sorted(p))
    del group['product']
    return group
def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities.drop_duplicates(inplace=True)
    newDf = activities.groupby('sell_date').apply(my_function)
    newDf.drop_duplicates(inplace=True)
    return newDf