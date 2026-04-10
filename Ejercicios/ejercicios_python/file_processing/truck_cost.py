# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 15:18:21 2021

@author: feder
"""

""" Ejercicio 2.2:  Lectura de un archivo de datos"""

with open('../Data/camion.csv', 'rt') as f:
    costo_total = 0
    siguiete_linea = next(f)
    for line in f:
        row = line.split(',')
        cajones_x_fruta = int(row[1]) * float(row[2].rstrip("\n"))
        costo_total = costo_total + cajones_x_fruta
    print("costo de total: ",costo_total)
    
"""Ejercicio 2.3: Precio de la naranja"""

with open('../Data/precios.csv',mode = 'rt', encoding='utf8') as precios:
       for line in precios:
          nueva_linea = line.rstrip("\n").split(",")          
          if nueva_linea[0]== "Naranja":
              print('precio de la Naranja: $',nueva_linea[1])
             

"""Ejercicio 2.6: Transformar un script en una función"""

def costo_camion(Nombre_archivo):
    with open(Nombre_archivo, 'rt') as f:
        costo_total = 0
        siguiete_linea = next(f)
        for line in f:
            row = line.split(',')
            cajones_x_fruta = int(row[1]) * float(row[2].rstrip("\n"))
            costo_total = costo_total + cajones_x_fruta
       
        return costo_total
        
costo_camion("../Data/camion.csv")


""""Ejercicio 2.7: Buscar precios"""


def buscar_precio(fruta):
    with open('../Data/precios.csv',mode = 'rt', encoding='utf-8') as precios:
        costo=0
        try:            
            for line in precios:
                nueva_linea = line.rstrip("\n").split(",")
                opcion=nueva_linea[0]
                                
                if opcion==fruta:
                       precios = float(nueva_linea[1])
                       costo = precios
            if costo==0:
                print(f'{fruta} no figura en el listado de precios')  
        except:
            print("cvbcd")   
                  
   # return f'el precio de la {fruta} es:{costo}'           
    return costo           
buscar_precio("Cebolla")  
         

"""Ejercicio 2.8: Administración de errores"""



def costo_camion(Nombre_archivo):
    try:
        with open(Nombre_archivo, 'rt') as f:
            costo_total = 0
            siguiete_linea = next(f)
            for line in f:
                row = line.split(',')
                cajones_x_fruta = int(row[1]) * float(row[2].rstrip("\n"))
                costo_total = costo_total + cajones_x_fruta
           
            return costo_total
    except FileNotFoundError: 
        print(f'{Nombre_archivo}\nNo corresponde a una direccion válida.') 
        
costo_camion('Data/missing.csv')


"""Ejercicio 2.9: Funciones de la biblioteca"""


def costo_camion(f):
    import csv
    try:
        a = open(f)
        rows = csv.reader(a)
        headers = next(rows)
        precio_final = 0
        for line in rows:
            try:       
                cajon=int(line[1])      
                precio=float(line[2])   
                precio_final = cajon*precio + precio_final 
            except:
                print('Una fila se encuentra vacía')
                
        return precio_final
        f.close()
    except FileNotFoundError or TypeError: 
        print(f'No corresponde a una direccion válida.') 
        
        
        
precio_final = costo_camion("../Data/missing.csv")
print('Costo total=',precio_final) 


"""2.15: Lista de tuplas"""
        
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
cost=costo_camion("../Data/missing.csv")
print(f'Costo Total:{cost}')