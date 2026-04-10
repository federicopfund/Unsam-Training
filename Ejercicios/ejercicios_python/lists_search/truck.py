# -*- coding: utf-8 -*-
"""
@author: federico pfund
"""
#%%
def leer_camion(direccion):
    import csv

    f= open(direccion)
    rows = csv.reader(f)
    headers = next(rows)
    select = ['nombre','cajones','precio']
    indice=[headers.index(ncolumna) for ncolumna in select]
    row=next(rows)
    record = {ncolumna: row[index] for ncolumna, index in zip(select, indice)}
    camion =[{ncolumna: row[index] for ncolumna, index in zip(select, indice)} for row in rows]
    return camion
 
camion= leer_camion('../Data/fecha_camion.csv')