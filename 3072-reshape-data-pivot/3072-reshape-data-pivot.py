import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
   new = pd.pivot_table(weather, index = 'month',columns = 'city' , values = 'temperature')

   return new