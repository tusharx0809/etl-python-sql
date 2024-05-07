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

#In the above lists created for each dataframe below are the indexes for each column for us to keep track while we transform the data

customer_orders_data = [] #this list will contain the transformed data which will then be pushed to target database
for row in range(len(customer_data)):
    ids = customer_data[row][0]
    row_info = []
    row_info.append(customer_data[row][0])
    row_info.append(customer_data[row][1] + ' ' + customer_data[row][2])
    contact_num = ''
    for digit in customer_data[row][5]:
        if digit.isdigit():
            contact_num += digit
    row_info.append(contact_num)
    row_info.append(customer_data[row][3] + ', ' + customer_data[row][4])
    count = 0
    total_amount = 0
    for j in range(len(order_data)):
        if ids == order_data[j][3]:
            count += 1
            total_amount += order_data[j][4]
    row_info.append(count)
    row_info.append(float(total_amount))
    customer_orders_data.append(row_info)



products_data = []
for row in range(len(product_data)):
    row_info = []
    row_info.append(product_data[row][0])
    row_info.append(product_data[row][1])
    row_info.append(float(product_data[row][3]))

    for i in range(len(supplier_data)):
        if supplier_data[i][0] == product_data[row][2]:
            row_info.append(supplier_data[i][1])
            row_info.append(supplier_data[i][2])
            if supplier_data[i][3] is None:
                row_info.append('Missing Info!')
            else:
                row_info.append(supplier_data[i][3])
            row_info.append(supplier_data[i][4] + ', ' +supplier_data[i][5])
            contact_num = ''
            for digit in supplier_data[i][6]:
                if digit.isdigit():
                    contact_num += digit
            row_info.append(contact_num)
            if supplier_data[i][7] is None:
                row_info.append('Missing Info!')
            else:
                row_info.append(supplier_data[i][7])
    products_data.append(row_info)



