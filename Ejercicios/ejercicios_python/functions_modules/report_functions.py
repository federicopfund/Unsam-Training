# -*- coding: utf-8 -*-
"""
@author: federico pfund
"""
#%%
import csv

#%%
def leer_camion(nombre_archivo):    
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        contenido_camion = []
        for n_row, row in enumerate(rows, start = 1):
            record = dict(zip(headers, row))
            try:
                contenido_camion.append({'nombre': record['nombre'], 'cajones': int(record['cajones']), 'precio': float(record['precio'])})
            except ValueError:
                print(f'Fila {n_row}: No pude interpretar: {row}')
        return contenido_camion

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        lista_precios = {}
        for n_row, row in enumerate(rows, start = 1):
            try:
                nombre = row[0]
                try:
                    precio = float(row[1])
                except:
                    print(f'el precio de la fila {n_row} es inválido.')
            except:
                print(f'nombre vacío en la fila {n_row}')
            lista_precios[nombre] = precio
        return lista_precios
    
def hacer_informe(carga,precios):
    informe = []
    for registro in carga:
        cambio = precios[registro['nombre']]-registro['precio']
        tupla = (registro['nombre'],registro['cajones'],registro['precio'],cambio)
        informe.append(tupla)
    return informe

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in informe:
        print('%10s %10d %10.2f %10.2f' % row)
    
#%%
nombre_archivo_camion='../Data/camion.csv'
nombre_archivo_precios='../Data/precios.csv'
#%%
informe_camion(nombre_archivo_camion,nombre_archivo_precios)
#%%
def informes_camion():
    files = ['../Data/camion.csv', '../Data/camion2.csv']
    for name in files:
        print(f'{name:-^43s}')
        informe_camion(name, '../Data/precios.csv')
        print()
#%%
informes_camion()