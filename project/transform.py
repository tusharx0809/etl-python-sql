import pyodbc
import random
import pandas as pd
from extract import *

#we have already created dataframes for all the tables, now we are going to convert the data into python lists so that we can manipulate and push our findings and clena data into target system, we are going to achieve this by creating a below function
def get_data(dataframe):
    data = [] #final list to be returned
    columns = list(dataframe.columns) #list of columns in the dataframe
    for idx,row in dataframe.iterrows():
        temp = []
        for i in columns: #traverse thorough columns to append the value in temporary list
            temp.append(row[i]) #append each value in list
        data.append(temp) #append each row in list(this will create a 2d list)
    return data

# passing each dataframe through above function
customer_data = get_data(customer_df)
order_data = get_data(order_df)
orderitem_data = get_data(orderitem_df)
product_data = get_data(product_df)
supplier_data = get_data(supplier_df)

print(supplier_data)