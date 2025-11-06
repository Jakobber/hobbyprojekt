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

def remove_names_from_table(df):
    end = False
    remove = []
    while not end:
        answer = input("Vilket nummer har personen? Ett nummer i taget, avsluta med \'e\'")
        if answer != 'e':
            remove.append(int(answer))
        else:
            end = True
    return df.drop(remove)

def get_personal_last_nRows(df:pd.DataFrame, user_id:str, nRows:int) -> pd.DataFrame:
    return df[df['user_id'] == user_id].tail(nRows)

def get_last_since_date(df:pd.DataFrame, user_id:str, date:str) -> pd.DataFrame:
    return df[(df['user_id'] == user_id) & (df['date'] >= pd.Timestamp(date, tz='UTC'))]
    
def merge_purchases_items(dfPurchases:pd.DataFrame, dfItems:pd.DataFrame) -> pd.Series:
    return pd.merge(dfPurchases, dfItems, on='item_id', how='inner')

def get_name_from_userID(dfUsers: pd.DataFrame, ID: str) -> str:
    user = dfUsers[dfUsers['user_id'] == ID]
    if len(user) == 1:
        return f"{user['firstname'].iloc[0]} {user['lastname'].iloc[0]}"
    else: 
        return False