import pandas as pd

def calculate_special_bonus(df: pd.DataFrame) -> pd.DataFrame:
    f = lambda df : df["salary"] if ((not df["name"].startswith('M')) & (df["employee_id"] % 2 == 1)) else 0
    df["bonus"] = df.apply(f, axis = 1)
    df.sort_values(by=["employee_id"], inplace = True)
    return df[["employee_id", "bonus"]]