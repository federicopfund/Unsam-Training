#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 16:29:52 2021

@author: federico pfund
"""

"""Ejercico: 3.8 Un ejemplo práctico de enumerate()"""
#%%        
def costo_camion(f):
    import csv
    try:
        a = open(f)
        rows = csv.reader(a)
        headers = next(rows)
        precio_final = 0
        for n_fila,line in enumerate(rows,start=1):
            try:       
                cajon=int(line[1])      
                precio=float(line[2])   
                precio_final = cajon*precio + precio_final 
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {line}')
        
        return precio_final
        f.close()
    except FileNotFoundError or TypeError: 
        print(f'No corresponde a una direccion válida.') 
#cost=costo_camion("../Data/missing.csv")
#print(f'Costo Total:{cost}')
#%%
"""Ejercicio: 3.9 La función zip()"""
def costo_camion1(nombre_archivo):
    import csv
    try:
        a = open(nombre_archivo)
        rows = csv.reader(a)
        headers = next(rows)
        costo_total = 0
        for n_fila, line in enumerate(rows, start=1):
            record = dict(zip(headers, line))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {line}')
        return costo_total
    except FileNotFoundError or TypeError: 
        print(f'No corresponde a una direccion válida.') 
              
        
def informe(camion):
    print(f'Costo Total:{costo_camion(camion)}')
#cost = costo_camion('../Data/fecha_camion.csv')
def main(argv):
    if len(argv)!=2:
        sys.exit(f'El número de parámetros es inadecuado. {argv[0]} recibe archivo_camion')
    else:
        camion = argv[1]
        
        informe(camion)
           
if __name__ == '__main__':
    import sys
    main(sys.argv)
