import pandas as pd

def fix_names(df: pd.DataFrame) -> pd.DataFrame:
    df['name'] = df['name'].apply(lambda x: x.lower().capitalize())
    return df.sort_values(by=['user_id'])