import pandas as pd

def find_nans(df: pd.DataFrame):
    """
    I want this function to search for nan values in every column
    of a dataset and return:
        - The total count nans in every column in the form of dict
        where the keys are the names of the column
        - the indices of the rows where there exist at least 1 nan.
    """
    cols = df.columns

    nan_count = {col: df[col].isna().sum() for col in cols}
    indices = df[df.isna().any(axis=1)].index

    return nan_count, indices