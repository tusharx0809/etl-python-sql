"""This is a small ETL project which extracts data from csv and loads into the MSSQL server"""
import os
import pandas as pd

file = 'D:\\Python\\etl-python-sql\\sample.csv'

df = pd.read_csv(file, encoding='latin1')

print(df.head())