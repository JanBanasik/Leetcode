import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    res = pd.DataFrame(views[views["author_id"] == views["viewer_id"]]["author_id"])
    res = pd.DataFrame(res["author_id"].unique())
    res.columns = ["id"]
    res = res.sort_values(by=["id"])
    return res