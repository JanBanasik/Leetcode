import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    filteredUsers = users[users["mail"].str.match("^[A-Za-z][A-Za-z0-9_\.-]*@leetcode\.com$")]
    return filteredUsers