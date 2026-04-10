#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Federico Pfund
"""
#%%
import os
import csv
from fileparse import parse_csv3, parse_csv2
import sys
#os.getcwd()
#os.chdir('C:\\Users\\feder\\OneDrive\\Documentos\\GitHub\\Programacion_en_Python_UNSAM\\Notas\\Ejercicios\\ejercicios_python\\Clase06')



def leer_camion(nombre_archivo1):
    'lee un archivo de lotes de un camion y lo devuelve como lista de diccionarios con claves nombre, cajones precio'
    with open(nombre_archivo1) as file:
        camion = parse_csv3(file, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    return camion

def leer_precios(nombre_archivo2, has_headers = False): #El default de has-heaers es False
    with open(nombre_archivo2) as file:    
        if has_headers: #Acá has_headers es true 
            precio_productos = parse_csv3(nombre_archivo2, has_headers = True)
        else:
            precio_productos = {tupla[0]: tupla[1] for tupla in parse_csv2(nombre_archivo2, has_headers = False)}
    return precio_productos

def hacer_informe(archivo1,archivo2, has_headers = False):
    a = leer_camion(archivo1)
    b = leer_precios(archivo2,has_headers = False) ##Acá o ´se si funciona bien cuando archivo dos tienen headers
    lista_tuplas = []
    for s in a:
        if s['nombre'] in b:
            Nombre = s['nombre']
            precio_venta = float(b[Nombre])
            Cajones = int(s['cajones'])
            Precio = float(s['precio'])
            Cambio = precio_venta - Precio
            tupla = (str(Nombre), Cajones, precio_venta, Cambio)
            lista_tuplas.append(tupla)
    return lista_tuplas

def balance_venta(nombre_archivo1, nombre_archivo2):
    a = leer_camion(nombre_archivo1)
    b = leer_precios(nombre_archivo2)
    venta = 0
    balance= 0
    costo_total = 0
    for s in a: ###Llamo a cada uno de los elementos de a, que son dicccionarios dentro de una lista
        if s['nombre'] in b:
            clave = s['nombre']
            cajones = int(s['cajones'])
            precio = float(s['precio'])
            costo_total += cajones*precio
            venta +=  b[clave]*cajones
            balance += (b[clave] - precio)*cajones
    return  print (f'Lo recaudado es de: ${venta}. El costo de la carga del camión es de: ${costo_total}. La diferencia es de: ${balance}')

def imprimir_informe(informe):
    encabezado = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(*encabezado))
    print('{:->10s} {:->10s} {:->10s} {:->10s}'.format('-', '-', '-', '-'))
    for row in informe: 
       print('%10s %10d %10.2f %10.2f' % row)
    return
        
def informe_camion (archivo1, archivo2):
    informe = hacer_informe(archivo1,archivo2)
    return imprimir_informe (informe)

def main(argv):
    if len(argv)!=3:
        sys.exit(f'El número de parámetros es inadecuado. {argv[0]} recibe archivo_camion y archivo_precio')
    else:
        camion = argv[1]
        precios = argv[2]
        informe_camion(camion,precios)
           
if __name__ == '__main__':
    import sys
    main(sys.argv)
