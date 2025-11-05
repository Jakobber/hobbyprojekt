import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv('streckbase\.env')

def connect_remote_db():
    try:
        connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        database=os.getenv('DB_NAME')
    )

        if connection.is_connected():
            print("Successfully connected to remote database")
            cursor = connection.cursor()
            cursor.execute("SELECT NOW();")
            print("Current time from DB:", cursor.fetchone())

    except Error as e:
        print("Error:", e)

    return connection

def disconnet(connection):
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.close()
        connection.close()
        print("Connection closed")

def fetch_tables(connection):
    if connection.is_connected():
        cursor = connection.cursor()

        # Get all table names
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        
        print("Tables in database:")
        for table in tables:
            print(" -", table[0])
            print_table(connection, table[0])
        

def print_table(connection, table_name, nRows=0):
    cursor = connection.cursor()
    cursor.execute(f'SELECT * from {table_name}')
    columns = [desc[0] for desc in cursor.description]
    print("Columns:", columns)

    rows = cursor.fetchall()
    if nRows or nRows:
        print("Rows:")
        for row in rows[:nRows]:
            print(row)

