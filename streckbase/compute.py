def get_debt_over_limit(connection, limit: int) -> list:
    """
    connection: SQL connection from connecte_remote_db()

    Limit: the debt limit requested

    returns: list [tuples(email, firstname, lastname, debt)]
    """
    table_name='Users'
    column_name='debt'

    cursor = connection.cursor()
    query = f"SELECT * FROM {table_name} WHERE {column_name} > %s;"
    cursor.execute(query, (limit,))
    rows = cursor.fetchall()
    ret = rows[:][1:4]
    return ret

def get_total_debt(connection)-> tuple:
    """
    Calculates total debt.

    returns: tuple (owed to streckbase, owed from streckbase, total)
    """
    cursor = connection.cursor()
    query = f"SELECT * FROM Users WHERE debt > %s;"
    cursor.execute(query, (0,))
    rows = cursor.fetchall()
    pos_debt = sum(list(zip(*rows))[4])
    query = f"SELECT * FROM Users WHERE debt < %s;"
    cursor.execute(query, (0,))
    rows = cursor.fetchall()
    neg_debt = sum(list(zip(*rows))[4])

    return pos_debt, -neg_debt, pos_debt+neg_debt

