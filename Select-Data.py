import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    x = students.loc[students["student_id"] == 101 , ["name", "age"]]
    return x
    