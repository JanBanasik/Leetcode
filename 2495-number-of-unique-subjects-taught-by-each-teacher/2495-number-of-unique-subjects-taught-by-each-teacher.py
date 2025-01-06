import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    newDf = teacher[['teacher_id', 'subject_id']].groupby('teacher_id').nunique('subject_id').reset_index()
    newDf.columns = ['teacher_id', 'cnt']
    return newDf