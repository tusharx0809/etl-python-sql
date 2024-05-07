import random
import pyodbc
import pandas as pd

# database downloaded from "https://www.dofactory.com/sql/sample-database"

connection_string_source = f"""
    Driver=ODBC Driver 17 for SQL Server;
    Server=localhost\SQLEXPRESS;
    Database=testing;
    Trusted_Connection=yes;
"""
connection = pyodbc.connect(connection_string_source)

#Function to fetch data from all tables
def get_table(connection_string, sql_query):
    cursor = connection.cursor()
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    df = pd.DataFrame.from_records(rows, columns = columns)
    return df

#creating data frames for each table for us to work on
customer_df = get_table(connection_string_source,'select * from customer')
order_df = get_table(connection_string_source, 'select * from [order]')
orderitem_df = get_table(connection_string_source,'select * from orderitem')
product_df = get_table(connection_string_source,'select * from product')
supplier_df = get_table(connection_string_source,'select * from supplier')

print(order_df)