#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# <---------------------------- Generadores ------------------------->
"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com """

#%%
# <------------------------- ticker ----------------------------------------->

from vigilante import vigilar
import csv
import informe
#%%

# <----Elegir columas especificas ------>

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]
        
# <-------- Hacer diccionarios ------->
def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, float])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

# <---- Filtrar Datos ---------------->
def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila

if __name__ == '__main__':
    camion = informe.leer_camion('../Data/camion.csv')
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    filtrar_filas = filtrar_datos(rows, camion)
    for row in filtrar_datos:
        print(row)
