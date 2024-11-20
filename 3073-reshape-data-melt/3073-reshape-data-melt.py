import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    report =  report.melt(id_vars=['product'], value_vars=['quarter_'+str(i) for i in range(1,5)])
    report.columns = ['product', 'quarter', 'sales']
    return report