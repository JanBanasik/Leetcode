import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by = 'event_date', inplace=True)
    activity.drop_duplicates(subset=['player_id'], keep='first', inplace=True)
    result_df = activity[['player_id', 'event_date']]
    result_df.columns = ['player_id', 'first_login']
    return result_df