from connect import *
from compute import *

def main():
    connection = connect_remote_db()
    fetch_tables(connection)
    

if __name__ =="__main__":
    main()
