def audit_missing_values(df):
    missing_count = df.isna().sum()
    missing_percent = (missing_count / len(df)) * 100

    result = {
        "missing_count": missing_count.to_dict(),
        "missing_percent": missing_percent.round(2).to_dict(),
        "rows_with_missing": int(df.isna().any(axis=1).sum()),
        "completeness_score": round(100 - missing_percent.mean(), 2)
    }
    return result
