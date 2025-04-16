import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    studentSubjects = pd.merge(students, subjects, how = 'cross')
    examinations['some_val'] = 1
    test = pd.merge(studentSubjects, examinations, left_on = ['student_id', 'subject_name'], right_on=['student_id', 'subject_name'], how='left')
    
    test['student_name'].fillna(value='null', inplace=True)
    test = test.groupby(by=['student_id', 'student_name', 'subject_name']).agg(
        attended_exams = ('some_val', 'sum')
    ).reset_index().sort_values(by=['student_id', 'subject_name'])

    test.replace("null", np.nan, inplace=True)
    return test