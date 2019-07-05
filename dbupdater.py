# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 22:14:07 2019

@author: Moranski
"""

import sqlite3
import pandas as pd


conn = sqlite3.connect('invoices.db')  
c = conn.cursor()

read_invoices = pd.read_csv (r'output.csv')
read_invoices.to_sql('Invoices', conn, if_exists='append', index = False) # Insert the values from the csv file into the table 'Invoices' 

read_products = pd.read_csv (r'output1.csv')
read_products.to_sql('Products', conn, if_exists='append', index = False) # Insert the values from the csv file into the table 'Products'


