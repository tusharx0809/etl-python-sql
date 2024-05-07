# Explanation

# customer_data = for each list in customer_data
#                    customer_data[list][0] is id 
#                    customer_data[list][1] is FirstName
#                    customer_data[list][2] is LastName
#                    customer_data[list][3] is City 
#                    customer_data[list][4] is Country
#                    customer_data[list][5] is Phone                      
# To acces the values, we just use python functionality of lists and indexes, for example customer_data[0][1] will be Maria which is the FirsName for first row in our table
# This will be same for each of the other datasets

# we are going to create a target table with customer_orders information with below columns when we load the data
# id int
# full_name varchar(255)
# location varchar(255) like Berlin, Italy
# customer_contact varchar(255) in the form 555419123
# total_orders int
# total_amount decimal(10,2)


#we have extracted the data into table1_data, so we can push it into MS-SQL database


#                    product_data[list][0] is id 
#                    product_data[list][0] is ProductName
#                    product_data[list][2] is SupplierId
#                    product_data[list][3] is UnitPrice
#                    product_data[list][4] is Package
#                    product_data[list][5] is isDicontinued

# we are going to create a target table with product information with below columns and we will only add products which are not discontinued
# product_data = for each list in product_data
# id int,
# product_name varchar(255)
# product_price deciman(10,2)
# supplier_company_name varchar(255)
# supplier_name varchar(255)
# contact_title varchar(255)
# location varchar(255)
# phone varchar(255)
# fax_info varchar(255)