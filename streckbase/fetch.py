import pandas as pd
from datetime import datetime

# dfPurchases['date'].dt.tz_localize(None).dt.floor('S')

def get_table_as_pandas(eng, table_name) -> pd.DataFrame:
    """Returns a table as a pd.DataFrame

    eng: SQLAlchemy engine

    table_name: the table to export as pandas dataframe
    
    """
    df = pd.read_sql(f'SELECT * from {table_name}', con=eng)
    if table_name == 'Users':
        df['created_at'] = df['created_at'] = pd.to_datetime(df['created_at'], utc=True, format='ISO8601')
    elif table_name == 'Purchases':
        df['date'] = df['date'] = pd.to_datetime(df['date'], utc=True, format='ISO8601')
    return df

def print_names_from_table(table: pd.DataFrame):
    for i, row in table.iterrows():
        print(f"{i:2}: {row['firstname']:9} {row['lastname']:12} är skyldig {row['debt']:4}kr, den råttan!")

def remove_names_from_table(df: pd.DataFrame) -> pd.DataFrame:
    """Shows a list of persons in table, loops over a remove function"""
    end = False
    while not end:
        answer = input("Vilka/vilket nummer har personerna/personen? Kommaseparera nummeren")
    try:
        remove = [int(x) for x in answer.split(",")]
        end = True
    except:
        print("Listan var inte kommaseparerad")
    return df.drop(remove)

def get_personal_last_nRows(df:pd.DataFrame, user_id:str, nRows:int) -> pd.DataFrame:
    return df[df['user_id'] == user_id].tail(nRows)

def get_last_since_date(df:pd.DataFrame, date:str, user_id='') -> pd.DataFrame:
    """
    slices df since a timestamp
    
    pass user Id as string to user_id to also single out one user

    Returns: pd.DataFrame since date
    """
    if user_id == '':
        return df[df['date'] >= pd.Timestamp(date, tz='UTC')].sort_values(by='date').reset_index()
    else:
        return df[(df['user_id'] == user_id) & (df['date'] >= pd.Timestamp(date, tz='UTC'))].sort_values(by='date').reset_index()
    
def merge_purchases_items(dfPurchases:pd.DataFrame, dfItems:pd.DataFrame) -> pd.DataFrame:
    # Merge dfs on item_id, sort new df by the date column, reset index since we want the df sorted by date
    df = pd.merge(dfPurchases, dfItems, on='item_id', how='inner').sort_values(by='date').reset_index()
    df[['volume', 'alcohol']] = df[['volume', 'alcohol']].fillna(0.0) # remove NaN values in volume and alcohol columns
    return df

def get_name_from_userID(dfUsers: pd.DataFrame, ID: str) -> tuple[str, str]:
    """
    get string for first and lastname of user ID

    returns: Tuple of Strings, first and lastname OR False if user is not in database
    """
    user = dfUsers[dfUsers['user_id'] == ID]
    if len(user) == 1:
        return user['firstname'].iloc[0], user['lastname'].iloc[0]
    else: 
        return False, False
    
    