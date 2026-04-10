#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# <----------------------- Generadores e iteradores ------------------------->
"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com """

#%%

# <----------------------------- Imports ------------------------------------>
from vigilante import vigilar
import csv
import informe
import formato_tabla
import sys
#%%
# <----------------------------- ticker ------------------------------------->

def ticker(camion_file, log_file, fmt):
    '''
    Imprime por pantalla en el formato deseado
    '''
    camion = informe.leer_camion(camion_file)
    filas = parsear_datos(vigilar(log_file), types = [str, str, str])
    filas = filtrar_datos (filas, camion)
    formateador = formato_tabla.crear_formateador(fmt)
    formateador.encabezado(['nombre', 'precio', 'volumen'])
    while True:
        for fila in filas:
           formateador.fila(fila.values())

# <------------------------ filtrar_datos ----------------------------------->
def filtrar_datos(filas, nombres):
#   <------ Filtrador por nombre ------->
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila

# <------------------------ cambiar_tipo ------------------------------------>
def cambiar_tipo(rows, types):
#  <-- Cambia el tipo de cada elemento de fila ---->
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

# <------------------------- hace_dicts ------------------------------------->
def hace_dicts(rows, headers):
#   <---- Crea diccionarios ----->
    for row in rows:
        yield dict(zip(headers, row))

# <----------------------- elegir_columnas --------------------------------->
def elegir_columnas(rows, indices):
#   <----- Elije columnas de un archivo ----->
    for row in rows:
        yield [row[index] for index in indices]


# <------------------------- parsear_datos ---------------------------------->
def parsear_datos(lines, types = [str, float, float]):
    # <------Parseo de lineas --------->
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, types) # [str, float, float]
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

# <-------------------- Expreciones Generadoras ----------------------------->
"""def parsear_datos(lineas):
    
    #<------------ Lectura del archivo -------------->
    lins = csv.reader(lineas)
    
    #<--- Eleguir fila de la lectura -> "lins" ------->
    elegir_cols = ([row[index] for index in [0,1,2]] \
                               for row in lins)
        
    # <----------- Cambiar Tipo ---------------------->
    camb_type = ([func(val) for func, val in zip([str, float, float], row)] \
                            for row in elegir_cols)
        
    # <----------- Hacer diccionario ----------------->
    diccionario = (dict[zip(['nombre','precio','volumen'], elemento)] \
                            for elemento in camb_type)
        
    # <---------- Filtrar datos ---------------------->
    filtro = (fila for fila in diccionario if fila['nombre'] 
                            in ['Mandarina','Naranja'])
    
    # <-----retorna------>
    return filtro"""
#%%
# <----------------------------- Main --------------------------------------->
def main(argv):
    if len(sys.argv) != 4:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]}'
                         ' archivo_camion archivo_mercadolog formato')
    else:
        camion = sys.argv[1]
        filas = sys.argv[2]  
        formato = sys.argv[3]  

    ticker(camion, filas, formato)

# <--------------------------- Sys ------------------------------------------>
if __name__ == '__main__':
    main(sys.argv)
    
   