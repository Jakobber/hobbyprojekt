# import mysql.connector
# import os
# from dotenv import load_dotenv
# from mysql.connector import Error

# load_dotenv('streckbase\.env')

import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

def connect_remote_db():
    """Create and return an SQLAlchemy engine connection.
    
    returns tuple (connection engine)
    """
    load_dotenv()
    DB_URL = (
    f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

    try:
        engine = create_engine(DB_URL)
        connection = engine.connect()
        # print("Successfully connected to remote database")

        # Test query
        result = connection.execute(text("SELECT NOW();"))
        # print("Current time from DB:", result.scalar())

        return connection, engine
    except SQLAlchemyError as e:
        print("Error:", e)
        return None


def disconnect(connection):
    """Close the database connection."""
    if connection:
        connection.close()
        print("Connection closed")


def fetch_tables(connection):
    """Fetch and print all tables in the database."""
    try:
        result = connection.execute(text("SHOW TABLES;"))
        tables = [row[0] for row in result]

        print("Tables in database:")
        for table in tables:
            print_table(connection, table)

    except SQLAlchemyError as e:
        print("Error fetching tables:", e)


def print_table(connection, table_name, nRows=0):
    """Print rows and columns from a given table."""
    try:
        result = connection.execute(text(f"SELECT * FROM {table_name};"))
        columns = result.keys()
        rows = result.fetchall()

        print(f"\nTable: {table_name}")
        print("Columns:", columns)

        # If nRows is 0, print all rows
        nRows = len(rows) if nRows == -1 else nRows
        if nRows > 0:
            print(f"Rows (showing {nRows}):")
            for row in rows[:nRows]:
                print(row)

    except SQLAlchemyError as e:
        print(f"Error printing table '{table_name}':", e)
