import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers["contains"] = customers["id"].isin(orders["customerId"])
    res = pd.DataFrame(customers[customers["contains"] == False]["name"])
    res.columns = ["Customers"]
    return res