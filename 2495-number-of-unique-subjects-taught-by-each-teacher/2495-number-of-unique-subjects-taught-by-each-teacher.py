import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    newDf = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    newDf.rename(columns={'subject_id': 'cnt'}, inplace=True)
    return newDf