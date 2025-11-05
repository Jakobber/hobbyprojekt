import pandas as pd

def get_table_as_pandas(eng, table_name) -> pd.DataFrame:
    """Returns a table as a pd.DataFrame

    eng: SQLAlchemy engine

    table_name: the table to export as pandas dataframe
    
    """
    return pd.read_sql(f'SELECT * from {table_name}', con=eng)

def item_IDs_to_item_names(Ids):
    pass

def print_names_from_table(table: pd.DataFrame):
    for i, row in table.iterrows():
        print(f"{i:2}: {row['firstname']:9} {row['lastname']:12} är skyldig {row['debt']:4}kr, den råttan!")

def remove_names_from_table(df):
    end = False
    remove = []
    while not end:
        answer = input("Vilket nummer har personen? Ett nummer i taget, avsluta med \'e\'\n")
        if answer != 'e':
            remove.append(int(answer))
        else:
            end = True
    return df.drop(remove)

