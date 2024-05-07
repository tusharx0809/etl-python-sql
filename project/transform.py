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
#customer_data = for each list in customer_data
#                    customer_data[list][0] is id 
#                    customer_data[list][1] is FirstName
#                    customer_data[list][2] is LastName
#                    customer_data[list][3] is City 
#                    customer_data[list][4] is Country
#                    customer_data[list][5] is Phone                      
#To acces the values, we just use python functionality of lists and indexes, for example customer_data[0][1] will be Maria which is the FirsName for first row in our table
#This will be same for each of the other datasets

table1_data = [] #this list will contain the transformed data which will then be pushed to target database

#we are going to create a target table with customer information with below columns when we load the data
# id int
# full_name varchar(255)
# location varchar(255) like Berlin, Italy
# customer_contact varchar(255) in the form 555419123
# total_orders int
# total_amount decimal(10,2)

table1_data = [] #this list will contain the transformed data which will then be pushed to target database
for i in range(len(customer_data)):
    ids = customer_data[i][0]
    row_info = []
    row_info.append(customer_data[i][0])
    row_info.append(customer_data[i][1] + ' ' + customer_data[i][2])
    contact_num = ''
    for digit in customer_data[i][5]:
        if digit.isdigit():
            contact_num += digit
    row_info.append(contact_num)
    row_info.append(customer_data[i][3] + ', ' + customer_data[i][4])
    count = 0
    total_amount = 0
    for j in range(len(order_data)):
        if ids == order_data[j][3]:
            count += 1
            total_amount += order_data[j][4]
    row_info.append(count)
    row_info.append(float(total_amount))
    table1_data.append(row_info)

#we have extracted the data into table1_data, so we can push it into MS-SQL database
