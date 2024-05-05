"""This is a small ETL project which extracts data from csv and loads into the MSSQL server"""
#The csv contains random data with 5000 rows, out of which we are going to extract only top 100 rows with valiues Name, Province and Profession. Then we will load these values in our MS-SQL server in testing database and Analysis table which is initially empty.

import pyodbc
import pandas as pd

file = 'D:\\Python\\etl-python-sql\\sample.csv'
columns = ['column' + str(i) if i != 0 else '' for i in range(1, 11)]
df = pd.read_csv(file, encoding='latin1', names=columns)

to_sql = [] # we will use this array to load data into our SQL server

i = 0 # we will increment this to 100 so we can get a total of 100 values
for idx,row in df.iterrows():
    temp = []
    temp.append(row['column3']) # append Name in temp array
    temp.append(row['column8']) # append Province in temp array
    temp.append(row['column9']) # append Profession in temp array
    to_sql.append(temp) # append temp array to to_sql in each loop
    i += 1
    if i == 100:
        break
# create a connection string to connect to database using pyodbc
connection_string = f"""
    Driver=ODBC Driver 17 for SQL Server;
    Server=localhost\SQLEXPRESS;
    Database=testing;
    Trusted_Connection=yes;
"""

connection = pyodbc.connect(connection_string)

cursor = connection.cursor()

insert_query = """
insert into Analysis(name,province,profession)
values(?,?,?)
"""

for values in to_sql:
    cursor.execute(insert_query, values) # usign execute function we run insert query for each value in to_sql array
connection.commit()