import random
from debugpy import connect
import pyodbc
import pandas as pd

#create the connection string with MS-SQL server information, Here are we are going to load data to testing2 database which will be our target
connection_string_source = f"""
    Driver=ODBC Driver 17 for SQL Server;
    Server=localhost\SQLEXPRESS;
    Database=testing2;
    Trusted_Connection=yes;
"""

#create the connection
connection = pyodbc.connect(connection_string_source)
cursor = connection.cursor()

