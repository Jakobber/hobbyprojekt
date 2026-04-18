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


def create_streckbase_wrapped_df(df:pd.DataFrame) -> pd.DataFrame:
    """creates a df with all info for streckbase wrapped
    
    df: merged purchases and items df
    """
    df['alcohol_frac'] = df['alcohol']/100                          # set alcohol to fractions instead of percentage
    df['volume'] = df['volume']/100                                 # set volum to Liter instead of cl
    df['total_alc'] = (df['volume']*df['alcohol_frac']).round(2)    # pure alcohol

    df_wrapped = df.groupby('user_id')[['total_alc', 'price', 'volume']].sum().reset_index() # Sum stats for each user_id
    df_pripps = df[df["name"].str.startswith("Pripps")].groupby("user_id").size().reset_index(name="Pripps_count") # Sum pripps, multiple names
    df_wrapped = pd.merge(df_wrapped, df_pripps, on='user_id', how='inner')     # merge pripps sum col into main df
    df_wrapped['alc_to_pripps'] = (df_wrapped['total_alc']/(0.05*0.33)).round(1)# new col for pure alc transofmerd into pripps
    df_wrapped = df_wrapped[df_wrapped['price'] >= 100]                         # Remove users who have spent less then 100 kr in df

    return df_wrapped

