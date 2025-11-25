import pandas as pd
import numpy as np

def run_audit(df):
    report={}
    report['missing']=df.isna().sum().to_dict()
    numeric=df.select_dtypes(include='number')
    z=(numeric-numeric.mean())/numeric.std()
    outliers=(abs(z)>3)
    report['outliers']=outliers.any(axis=1).sum()
    report['duplicates']=df.duplicated().sum()
    report['profiling']=numeric.describe().to_dict()
    return report