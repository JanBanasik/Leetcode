import pandas as pd

def createBonusColumn(df: pd.DataFrame) -> pd.DataFrame:
    df['bonus'] = 2 * df['salary']
    return df