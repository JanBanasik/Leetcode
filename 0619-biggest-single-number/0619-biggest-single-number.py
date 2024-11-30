import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    grouped = my_numbers.groupby(['num']).size().reset_index()
    grouped.rename(columns = {0: "counter"}, inplace = True)
    grouped.sort_values(by = "counter",inplace = True)
    max_single = -1
    for i in grouped.iterrows():
        num = i[1]['num']
        counter = i[1]['counter']
        if counter > 1:
            break
        max_single = max(max_single, num)
    if max_single == -1:
        max_single = None
    return pd.DataFrame({"num":[max_single]})
    