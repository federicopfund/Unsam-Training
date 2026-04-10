#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# <----------------------- Generadores e iteradores ------------------------->
"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com """
 #%%
# <------------------------------- Imports ---------------------------------->

from fileparse import parse_csv
import sys
import lote
import formato_tabla
from camion import Camion
#%%

# <-------------------------- Funcion leer_camion --------------------------->
def leer_camion(file_name):
    with open(file_name, 'rt') as file:
        camion_dicts = parse_csv(file, 
                                 select=['nombre','cajones','precio'],
                                 types=[str,int,float])
        
        camion = [ lote.Lote(d['nombre'],
                             d['cajones'],
                             d['precio']) for d in camion_dicts]
        # Retorno con resultado
        return Camion(camion)

# <------------------------ Funcion leer_precios ---------------------------->
def leer_precios(file_name):
    with open(file_name, 'rt') as file:
        venta = parse_csv(file ,types=[str,float], has_headers=False)
        header = ['producto', 'billetin'] # Asigno header
        precios = [dict(zip(header,tupa)) for tupa in venta]
        # Retorno con resultado
        return (precios) 

# <---------------------- Funcion hacer_informe ----------------------------->
def hacer_informe(camion, precios):
    # Variables
    informe = []
    for itemA in camion:
        for itemB in precios:
            try:
                if itemA.nombre == itemB['producto']:
                    producto = itemA.nombre
                    cantidad = int(itemA.cajones)
                    precio = round(float(itemA.precio),2)
                    cambio = round(float(itemB['billetin']) - precio, 2)
                    info = (producto, cantidad, precio, cambio)
                    informe.append(info)
            except KeyError:
                continue
    # Retorno con resultado
    return informe 

# <------------------ Funcion imprimir_informe ------------------------------>
def imprimir_informe(informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia)
    '''
    # Cabecera de informe
    formateador.encabezado(["Producto", "Cajones", "Precio", "Cambio"]) 
    
    for nombre, cajones, precio, cambio in informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)
    # Retorno a main
    return 

# <------------------ Funcion informe_camion -------------------------------->
def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt = 'txt'):
     # Leo datos del camion
    carga = leer_camion(nombre_archivo_camion)
    # Leo los precios de venta
    chanta = leer_precios(nombre_archivo_precios)
    # Genero un informe
    informe = hacer_informe(carga, chanta) 

    formateador = formato_tabla.crear_formateador(fmt)
    # Imprimo informe en pantalla
    imprimir_informe(informe, formateador)

# <--------------------------- Main ----------------------------------------->
def main(argv):
    if len(sys.argv) != 4:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]}'
                         ' archivo_camion archivo_precios formato')
    else:
        camion = sys.argv[1]
        precios = sys.argv[2]  
        formato = sys.argv[3]  

    informe_camion(camion, precios, formato)

# <--------------------------- Sys ------------------------------------------>
if __name__ == '__main__':
    main(sys.argv)