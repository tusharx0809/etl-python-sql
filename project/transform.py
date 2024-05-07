import pyodbc
import random
import pandas as pd
from extract import *

#we have already created dataframes for all the tables, now we are going to convert the data into python lists so that we can manipulate and push our findings and clena data into target system
def get_data(dataframe):
    data = []
    columns = list(dataframe.columns)
    for idx,row in dataframe.iterrows():
        temp = []
        for i in columns:
            temp.append(row[i])
        data.append(temp)
    return data

customer_data = get_data(customer_df)
order_data = get_data(order_df)
orderitem_data = get_data(orderitem_df)
product_data = get_data(product_df)
supplier_data = get_data(supplier_df)