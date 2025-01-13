import pandas as pd

def decide(row):
    if row['income'] < 20000:
        return "Low Salary"
    elif row['income'] <= 50000:
        return "Average Salary"
    else:
        return "High Salary"

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts["category"] = accounts.apply(decide, axis=1)
    resultDf = accounts.groupby("category")['account_id'].count().reset_index()
    resultDf.rename(columns={"account_id":"accounts_count" }, inplace=True)

    for name in ["Low Salary", "Average Salary", "High Salary"]:
        if name not in resultDf["category"].tolist():
            newRow = pd.DataFrame({"category": [name], "accounts_count": [0]})
            resultDf = pd.concat([resultDf, newRow], ignore_index=True)
    return resultDf