import pyodbc
import random
import pandas as pd
from extract import *

#customer_df dataframe generated in extract file
#columns in customer_df are [Id,FirstName,LastName,City,Country,Phone]
customers_data = []
for index,row in customer_df.iterrows():
    temp = []
    temp.append(row['Id'])
    temp.append(row['FirstName'])
    temp.append(row['LastName'])
    temp.append(row['City'])
    temp.append(row['Country'])
    temp.append(row['Phone'])
    customers_data.append(temp)
print(customers_data)