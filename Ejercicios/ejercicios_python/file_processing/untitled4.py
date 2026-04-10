# -*- coding: utf-8 -*-
# camion_commandline.py
import csv
import sys

def costo_camion(nombre_archivo):
      try:
        with open(nombre_archivo, 'rt') as f:
            costo_total = 0
            siguiete_linea = next(f)
            for line in f:
                row = line.split(',')
                cajones_x_fruta = int(row[1]) * float(row[2])
                costo_total = costo_total + cajones_x_fruta
           
            return costo_total
      except FileNotFoundError or ValueError: 
        print(f'{nombre_archivo}\nNo corresponde a una direccion válida.')     

   
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)

