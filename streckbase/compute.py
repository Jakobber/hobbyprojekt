import pandas as pd

def get_debt_over_limit(df: pd.DataFrame, limit: int) -> pd.DataFrame:
    """
    table: user table 

    Limit: the debt limit requested

    returns: dataframe of bad people
    """
    return df[df['debt'] > limit].reset_index()


def get_total_debt(df: pd.DataFrame)-> tuple:
    """
    Calculates total debt.

    df: users table as datafram

    returns: tuple (owed to streckbase, owed from streckbase, total)
    """
    pos_debt = df[df["debt"] > 0]["debt"].sum()
    neg_debt = df[df["debt"] < 0]["debt"].sum()

    return pos_debt, -neg_debt, pos_debt+neg_debt


