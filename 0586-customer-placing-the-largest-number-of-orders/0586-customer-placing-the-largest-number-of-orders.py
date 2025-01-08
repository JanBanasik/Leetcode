import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    newDf = orders.groupby('customer_number')['order_number'].count().reset_index()
    newDf.rename(columns={'order_number':'counter'}, inplace=True)
    return pd.DataFrame(
        {'customer_number': newDf[newDf['counter'] == newDf['counter'].max()]['customer_number'].tolist()}
    )