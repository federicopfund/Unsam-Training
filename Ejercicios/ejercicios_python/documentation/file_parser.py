#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Federico Pfund
"""

#Ejercicio 6.9
import csv

def parse_csv1(nombre_archivo, select = None, types = None, has_headers = True):
    import csv
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

#cajones_retenidos = parse_csv1('../Data/camion.csv', select =['nombre','cajones'])
#cajones_lote = parse_csv1('../Data/camion.csv', select=['nombre', 'cajones'], types=[str, int])
#precios = parse_csv1('../Data/precios.csv', types=[str,float], has_headers=False)


#%%

#Ejercicio 7.1
#import os
#os.chdir('C:/Users/feder/OneDrive/Documentos/GitHub/Programacion_en_Python_UNSAM/Notas/Ejercicios/ejercicios_python/Clase07/fileparse.py')

#Modifcá tu código para que lance una excepción en caso que ambos parámetros select y has_headers = False sean pasados juntos
#Modificá la función parse_csv() de modo que atrape todas las excepciones de tipo ValueError generadas durante el armado de los registros a devolver e imprima un mensaje de advertencia para las filas que no pudieron ser convertidas. Estas filas no deben ser procesadas (ya que no se puede hacer adecuadamente), y deben ser omitidas en el output de la función
#

def parse_csv2(nombre_archivo, select = None, types = None, has_headers = True, silence_errors = True):
    import csv
    'Parsea un archivo CSV en una lista de registros' #Esta función lee un archivo CSV y arma una lista de diccionarios a partir del contenido del archivo CSV
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        headers = next(filas)
        if select and not has_headers:
            raise RuntimeError(f'Para seleccionar, necesito encabezados.')
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
                try:
                    fila =[func(val) for func,val in zip(types, fila)]
                except ValueError as e:
                    if not silence_errors:
                        print(f'No pude convertir {fila}')
                        print(f'Motivo: {e}')
         #Armar el diccionario  
            if has_headers:
                registro =dict(zip(headers,fila))
                registros.append(registro)
                
            else:
                registros.append(tuple(fila))

    return registros

#=parse_csv2('../Data/precios.csv', select = ['nombre','precio'], has_headers = False)
#b=camion = parse_csv2('../Data/missing.csv', types = [str, int, float],silence_errors = False)

#%% "objetos cual archivos"
#Ejercicio 7.4
def parse_csv3(file, select = None, types = None, has_headers = True, silence_errors = True):
    import csv
    'Esta función lee un archivo CSV y arma una lista de diccionarios a partir del contenido del mismo'
    filas = csv.reader(file)
    headers = next(filas)
    if select and not has_headers: #levanta un error cuando se especifican columnas pero no hay encabezados en la lista
        raise RuntimeError(f'Para seleccionar, necesito encabezados.')
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
            try:
                fila =[func(val) for func,val in zip(types, fila)]
            except ValueError as e:
                if not silence_errors:
                    print(f'No pude convertir {fila}')
                    print(f'Motivo: {e}')
         #Armar el diccionario  
        if has_headers:
            registro =dict(zip(headers,fila))
            registros.append(registro)
                
        else:
            registros.append(tuple(fila))

    return registros

