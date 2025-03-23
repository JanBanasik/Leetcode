import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by = 'event_date', ascending = True, inplace=True)

    result = activity.drop_duplicates(subset = ['player_id'], keep='first')[['player_id', 'event_date']]

    columnNames = {'event_date': 'first_login'}
    return result.rename(columns=columnNames)