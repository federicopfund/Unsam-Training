# -*- coding: utf-8 -*-
"""
@author: Federico Pfund
"""
#%%
import csv
#%%
#Ejercicio n°6.3
def parse_csv1(nombre_archivo):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Lee los encabezados
        headers = next(rows)
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            registro = dict(zip(headers, row))
            registros.append(registro)

    return registros

#camion = parse_csv('../Data/camion.csv')

#Lee solamente la columnas que deseamos pasarle al argumento.
def parse_csv2(nombre_archivo, select = None):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros
#%%
#cajones_retenidos = parse_csv('../Data/camion.csv', select=['nombre','cajones'])
#%%
# Conversión de tipo 6.5
def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    'Parsea un archivo CSV en una lista de registros' #Esta función lee un archivo CSV y arma una lista de diccionarios a partir del contenido del archivo CSV
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        headers = next(filas)
        if select:
            indices = [headers.index(nombre_columna) for nombre_columna in select]
            headers = select 
        else:
            indices = []
            
        registros = []
        for fila in filas:
            if not fila: #Saltea filas sin datos
                continue
            #Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
            if types:
                fila =[func(val) for func,val in zip(types, fila)]
         #Armar el diccionario  
            if has_headers:
                registro =dict(zip(headers,fila))
                registros.append(registro)
                
            else:
                registros.append(tuple(fila))

    return registros

#cajones_retenidos = parse_csv('../Data/camion.csv', select =['nombre','cajones'])
#cajones_lote = parse_csv('../Data/camion.csv', select=['nombre', 'cajones'], types=[str, int])
#precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)
