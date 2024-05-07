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

#get the data from transform file
products_data = products_data

create_query = """
create table product_info(
  id int,
  product_name varchar(255),
  product_price decimal(10,2),
  supplier_company_name varchar(255),
  supplier_name varchar(255),
  contact_title varchar(255),
  location varchar(255),
  phone varchar(255),
  fax_info varchar(255)
)"""
create_cursor.execute(create_query)
connection.commit()

insert_cursor = connection.cursor()

insert_query = """
insert into product_info(id,product_name,product_price,supplier_company_name,supplier_name,contact_title,location,phone,fax_info)
values(?,?,?,?,?,?,?,?,?)"""

for value in products_data:
    insert_cursor.execute(insert_query, value)
connection.commit()
