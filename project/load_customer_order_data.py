import random
from debugpy import connect
import pyodbc
import pandas as pd
from transform import *

#create the connection string with MS-SQL server information, Here are we are going to load data to testing2 database which will be our target
connection_string_source = f"""
    Driver=ODBC Driver 17 for SQL Server;
    Server=localhost\SQLEXPRESS;
    Database=testing2;
    Trusted_Connection=yes;
"""

#create the connection
connection = pyodbc.connect(connection_string_source)
create_cursor = connection.cursor()

#customer_orders_data extracted in transform file, now we will load it
customer_orders_data = customer_orders_data

create_cursor = connection.cursor()
create_query = """
Create table customer_orders(
  id int,
  full_name varchar(255),
  contact_number varchar(255),
  location varchar(255),
  total_orders int,
  total_amount decimal(10,2)
)"""
create_cursor.execute(create_query)
connection.commit()

insert_query = """
insert into customer_orders(id,full_name,contact_number,location,total_orders,total_amount)
values(?,?,?,?,?,?)"""

insert_cursor = connection.cursor()
for value in customer_orders_data:
    insert_cursor.execute(insert_query, value)
connection.commit()