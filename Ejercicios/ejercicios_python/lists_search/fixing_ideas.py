# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:41:39 2021

@author: feder
"""
#%%
#Ejercicio 4.17: Fijando ideas.
import csv
f = open ('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
map(int, row[2].split('/'))
types = [str, float, tuple, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))
record
    
