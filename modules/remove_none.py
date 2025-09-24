# remove_none.py
import pandas as pd

def remove_null_values(dataframe):
    """
    Function to remove rows or columns with null values.
    Returns a cleaned dataframe.
    """
    # Remove rows with any null values
    cleaned_df = dataframe.dropna()
    return cleaned_df
