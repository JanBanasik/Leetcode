import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    newDf = courses.groupby('class')['student'].count().reset_index()
    newDf = newDf[newDf['student'] >= 5]
    return pd.DataFrame(newDf['class'])