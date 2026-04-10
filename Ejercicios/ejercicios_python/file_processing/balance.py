# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 23:17:36 2021

@author: federico pfund
"""


import csv
def leer_camion(nuevo_archivo):
    
    camion = []
    
    try:
        with open(nuevo_archivo,"rt") as f:
            row = csv.reader(f)
            headers = next(row)        
            for line in row:
                try:#levantamos indexerror
                    fila = [line[0], int(line[1]), float(line[2])]
                    registro = dict(zip(headers,fila))
                    camion.append(registro)
                except IndexError:
                    pass
        return camion  
        
    except FileNotFoundError or TypeError: 
          print(f'No corresponde a una direccion válida.') 
        
precio_compra = leer_camion('../Data/camion.csv')
def total_pagado(precio_compra):
    
    total = 0.0
    for s in precio_compra:
        total += s['cajones']*s['precio']
    return total
total_pagado_en_compra= total_pagado(precio_compra) 

def leer_precios(nuevo_archivo):
    
    mydict={}
    with open (nuevo_archivo,'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                mydict[row[0]] = float(row[1])
            except:
                pass
    return mydict
precio_venta= leer_precios('../Data/precios.csv')

def diferencia(precio_compra,precio_venta):
    it = 0
    diferencia=0
    for s in precio_compra:
        if s['nombre'] in precio_venta:
            venta =precio_venta[s['nombre']]*precio_compra[it]['cajones']
            compra = precio_compra[it]["cajones"]*precio_compra[it]['precio']
            diferencia += venta - compra
            it+=1
        else:
            pass
    return diferencia
diferencia_en_ventas=diferencia(precio_compra,precio_venta)

def recauda(precio_compra,precio_venta):
    it = 0
    recauda=0
    for s in precio_compra:
        if s['nombre'] in precio_venta:
            venta =precio_venta[s['nombre']]*precio_compra[it]['cajones']
            recauda += venta
            it+=1
        else:
            pass
    return recauda
recaudacion_de_ventas = recauda(precio_compra,precio_venta)
def line():
    print("-"*(14*7))
    
def mostrar_pantalla():
    line()
    print(f'| nombre   | precio_venta  | diferencia_de_venta | recaudacion_de_venta | total_pagado_en_compra |')
    line()
    for e in precio_venta:
        print(f'|{e:<9} | {precio_venta[e]:^14}| {diferencia_en_ventas}  | {recaudacion_de_ventas:^19}  | {total_pagado_en_compra:^22} |' )
    line()    
mostrar_pantalla()
