def audit_integrity(df):
    issues = {}
    issues["column_types"] = {col: str(df[col].dtype) for col in df.columns}

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    type_errors = {}
    for col in numeric_cols:
        invalid = df[col].apply(lambda x: isinstance(x, str)).sum()
        if invalid > 0:
            type_errors[col] = invalid
    issues["invalid_numeric_types"] = type_errors

    issues["duplicate_rows"] = int(df.duplicated().sum())

    if "id" in df.columns:
        issues["empty_id_rows"] = int(df["id"].isna().sum())

    return issues
