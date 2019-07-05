# -*- coding: utf-8 -*-
"""
Created on M Jul 1 15:45:43 2019

@author: Moranski
"""

import sqlite3

conn = sqlite3.connect('invoices.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE Invoices
             ([DATE] text, [generated_id] integer primary key, [COMPANY] text, [INV] real)''')
c.execute('''CREATE TABLE Products
             ([DATE] text, [generated_id] integer primary key, [BEVERAGE] real, [DRY] real, [DAIRY] real, [MEAT] real, [POULTRY] real, [PRODUCE] real, [SEAFOOD] real, [TOTAL] real)''')

# Insert a row of data


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

