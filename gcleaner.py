import pandas as pd

def get_valid_invalid(df: pd.DataFrame):
    """
    Returns a dictionary of boolean masks for valid (non-null) and invalid (null) values for each column.
    """
    cols = df.columns

    book = {}
    for col in cols:
        col_key = col.strip().replace(" ", "_").lower()
        valid_key = f"valid_{col_key}"
        invalid_key = f"invalid_{col_key}"

        book[valid_key] = df[col].notna()
        book[invalid_key] = df[col].isna()

    return book