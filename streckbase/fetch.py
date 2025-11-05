import pandas as pd

def get_table_as_pandas(connection, table_name) -> pd.DataFrame:
    """Returns a table as a pd.DataFrame

    Connection: connection to sql database
    table_name: the table to export as pandas dataframe
    
    """
    return pd.read_sql(f'SELECT * from {table_name}', con=connection)

def item_IDs_to_item_names(Ids):
    pass
