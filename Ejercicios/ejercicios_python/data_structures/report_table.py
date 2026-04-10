# -*- coding: utf-8 -*-
"""@author: federico pfund
"""
from collections import Counter
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


def recuento(precio_compra):           
        tenencias= Counter()
        for s  in precio_compra:    
            tenencias[s['nombre']] += s['cajones']
        return tenencias
recuento=recuento(precio_compra)

def total_pagado(precio_compra):
    
    total = 0.0
    for s in precio_compra:
        total += s['cajones']*s['precio']
    return total
total_pagado_en_compra= total_pagado(precio_compra) 

def leer_precios(nuevo_archivo):
    
    mydict={}
    total_cajones = Counter()
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
diferencia_en_venta=round(diferencia_en_ventas)
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
    print("-"*(68))
def line1():
    print("-"*(7*8))
def line2():
    print('-'*(9*9))
def mostrar_pantalla():
    line()
    print(f'| Nombre   | N_Cajones | Precio_Compra  |  precio_venta  |  Cambio |')
    line()
    n_filas=0
    for n_filas, e in enumerate(precio_compra):
        com = precio_compra[n_filas]["precio"]
        ven = precio_venta[precio_compra[n_filas]["nombre"]]
        cambio = ven - com
        print(f'| {precio_compra[n_filas]["nombre"]:<9} | {precio_compra[n_filas]["cajones"]:^8} | ${precio_compra[n_filas]["precio"]:^13} | ${precio_venta[precio_compra[n_filas]["nombre"]]:^13} | $ {cambio:^5.2f} |' )
      
    line()  
    print("|                   BALANCE                            |")
    line1()
    print(f'|  Costo_Camion  |  Recaudacion  |   diferencia_total  |') 
    line1()
    print(f'|  $ {total_pagado_en_compra:<10}  | $  {recaudacion_de_ventas:^11}|  $ {diferencia_en_venta:^17}|')
    line1()
    print("|                 Recuento de la carga                 |")
    line2()
    print(f'|{recuento}|')
    line2()
    
mostrar_pantalla()
        
