import pandas as pd

def audit_outliers(df):
    numeric_df = df.select_dtypes(include=["int64", "float64"])
    results = {}
    for col in numeric_df.columns:
        series = numeric_df[col].dropna()
        q1, q3 = series.quantile([0.25, 0.75])
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        outliers = series[(series < lower) | (series > upper)]
        results[col] = {
            "count": int(outliers.count()),
            "percent": round((outliers.count() / len(series)) * 100, 2),
            "lower_bound": float(lower),
            "upper_bound": float(upper)
        }
    return results
