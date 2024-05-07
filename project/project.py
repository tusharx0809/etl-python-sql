import random
import pyodbc
import requests
import pandas as pd

# database downloaded from "https://www.dofactory.com/sql/sample-database"

connection_string = f"""
    Driver=ODBC Driver 17 for SQL Server;
    Server=localhost\SQLEXPRESS;
    Database=testing;
    Trusted_Connection=yes;
"""

connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

query1 = """
select * from customer"""

cursor.execute(query1)

rows = cursor.fetchall()

print(rows)