import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    res = pd.DataFrame(animals[animals['weight']>100][['name','weight']])
    res = res.sort_values(by=['weight'], ascending=False)
    return pd.DataFrame(res['name'])