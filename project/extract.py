import random
import pyodbc
import requests
import pandas as pd

# database downloaded from "https://www.dofactory.com/sql/sample-database"

connection_string_source = f"""
    Driver=ODBC Driver 17 for SQL Server;
    Server=localhost\SQLEXPRESS;
    Database=testing;
    Trusted_Connection=yes;
"""

connection = pyodbc.connect(connection_string_source)

#Fetching data from customers table
customer_cursor = connection.cursor()
customer_query = 'select * from customer'
customer_cursor.execute(customer_query)
customer_rows = customer_cursor.fetchall()
customer_columns = [column[0] for column in customer_cursor.description]
customer_df = pd.DataFrame.from_records(customer_rows, columns = customer_columns)
print(customer_df)