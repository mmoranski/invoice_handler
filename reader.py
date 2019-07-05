# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 09:39:03 2019

@author: Moranski
"""
import tabula

# Read pdf into DataFrame
df=tabula.read_pdf("PDF/test.pdf", multiple_tables='false', guess='false', stream='true', area=('249, 239, 635, 599'), pages='all')

# convert PDF into CSV
tabula.convert_into("PDF/test.pdf", "output1.csv", output_format="csv", multiple_tables='false', guess='false', stream='true', pages='all')


