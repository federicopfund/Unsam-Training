#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def costo_camion(f):
    import csv
    try:
        a = open(f)
        rows = csv.reader(a)
        headers = next(rows)
        precio_final = 0
        contador=0
        for line in rows:
            contador += 1
            try:           
                cajon=int(line[1])      
                precio=float(line[2])   
                precio_final += cajon*precio
            except:
                print(f'la fila {contador} se encuentra vacía.',line)
        return precio_final
        f.close()
    except FileNotFoundError or ValueError:
        print(f'{nombre_archivo}\nNo corresponde a una direccion válida.')
        
        
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)    
