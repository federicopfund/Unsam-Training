# -*- coding: utf-8 -*-
"""
@author: federico pfund
"""

#%%
# Ejercicio 3.7: Lectura de los árboles de un parque
import csv
def leer_parque(nuevo_archivo,parque):
    
    park = []
  
    try:
        with open(nuevo_archivo,"rt",encoding = 'utf-8') as f:
            rows = csv.reader(f)
            headers = next(rows)  
            i=0
            for i, line in enumerate(rows,start=1):
                try:#levantamos indexerror
                    registro = dict(zip(headers,line))
                    if registro['espacio_ve'] == parque:
                        park.append(registro)
                                                
                except IndexError:
                    pass       
        return park
        
    except FileNotFoundError or TypeError: 
          print(f'No corresponde a una direccion válida.') 
        
lista_arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv',"GENERAL PAZ")
lista1_arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv',"ANDES, LOS")
lista2_arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv',"CENTENARIO")
#%%
# 3.8: Determinar las especies en un parque

def especies(lista_arboles):
    conjunto_especie = []
    for i, art in enumerate(lista_arboles,start=1):
        Art = art['nombre_com']
       
        conjunto_especie.append(Art)
        
    return  conjunto_especie
artenset = especies(lista_arboles)
artenset1 = especies(lista1_arboles)
artenset2 = especies(lista2_arboles)
#%%
#Ejercicio 3.9: Contar ejemplares por especie
from collections import Counter
# funcion que ingresa con 2 parametro dos lista y la cantidad de especies mas 
#mas frecuente en los parques
def contar_ejemplares(lista_archivo,n):
    tenencias= Counter(lista_archivo)
    return tenencias.most_common(n)
menge_arten= contar_ejemplares(artenset,5)
menge1_arten= contar_ejemplares(artenset1,5)
menge2_arten= contar_ejemplares(artenset2,5)

#%%
def line():
    print("-"*20)
def mostrar_arboleda():
    line()
    print(f'| General Paz      |')
    line()
    e = 0
    for e in range(5):
        print(f'{menge_arten[e][0]}:{menge_arten[e][1]}')
        e += 1
    line()
    print(f'|  los Andes     |')
    line()
    r=0
    for r in range(5):
        print(f'{menge1_arten[r][0]}:{menge1_arten[r][1]}')
        r += 1
    line()
    print(f'|  Centenario    |')
    line()
    t=0
    for r in range(5):
        print(f'{menge2_arten[t][0]}:{menge2_arten[t][1]}')
        t += 1
    line()
mostrar_arboleda()
#%%
#Ejercicio 3.10: Alturas de una especie en una lista.
def obtener_alturas(lista_arboles,especie):
    
    ausffuhren = []
    
    for e, clave in enumerate(lista_arboles,start=0):
        if especie == lista_arboles[e]['nombre_com']:
            especies = float(lista_arboles[e]['altura_tot'])
            
            ausffuhren.append(especies)
    alt_max= max(ausffuhren)
    suma = sum(ausffuhren)
    promedio = round(suma/len(ausffuhren),2)
    
    return alt_max, promedio
alt = obtener_alturas(lista_arboles,'Jacarandá')
alt1 = obtener_alturas(lista1_arboles,'Jacarandá')
alt2 = obtener_alturas(lista2_arboles,'Jacarandá')

#%%
def line1():
    print('-'*43)
def mostrar():
    line1()
    print(f'|medidas |General Paz|los Andes|Centenario|')
    line1()
    print(f'|maximo  |   {alt[0]}    |   {alt1[0]}  |   {alt2[0]}   |')
    line1()
    print(f'|promedio|   {alt[1]}    |  {alt1[1]}  |   {alt2[1]}   |')
    line1()
mostrar()

#%%
#Ejercicio 3.11: Inclinación promedio por especie de una lista.
def obtener_inclinacion(lista_arboles,especie):
    asff = []
    for r, clave in enumerate(lista_arboles,start = 0):
        if especie == lista_arboles[r]['nombre_com']:
            inclinacion = float(lista_arboles[r]['inclinacio'])
            asff.append(inclinacion)
    return asff
Nei = obtener_inclinacion(lista2_arboles,'Falso Guayabo (Guayaba del Brasil)' )
#%%
#Ejercicio 3.12: Especie con el ejemplar más inclinado
def especimen_mas_inclinado(lista_arboles):
    lis ={}
   
    for especie in especies(lista_arboles): 
        max_inc= max(obtener_inclinacion(lista_arboles,especie))
        lis[especie] = max_inc
        d_inv = [(val,key) for key, val in lis.items()]
    return max(d_inv)

especimen_mas_inclinado_park_Los_Andes = especimen_mas_inclinado(lista1_arboles)
especimen_mas_inclinado_park_General_Paz = especimen_mas_inclinado(lista_arboles)
especimen_mas_inclinado_park_Centenario = especimen_mas_inclinado(lista2_arboles)
print(f'Especie mas inclinada del Parque Los Andes:{especimen_mas_inclinado_park_Los_Andes}')
print(f'Especie mas inclinada del Parque General Paz:{especimen_mas_inclinado_park_General_Paz}')
print(f'Especie mas inclinada del Parque Centenario:{especimen_mas_inclinado_park_Centenario}')
#%%
#Ejercicio 3.12: Especie con el ejemplar más inclinado.
import numpy as np
def especimen_promedio_mas_inclinado(lista_arboles):
    d ={}
   
    for especie in especies(lista_arboles): 
        prom = np.mean(obtener_inclinacion(lista_arboles,especie))
        d[especie] = prom
        d_inv = [(val,key) for key, val in d.items()]
    return max(d_inv)
especimen_promedio_mas_inclinado_park_Los_Andes = especimen_promedio_mas_inclinado(lista1_arboles)
especimen_promedio_mas_inclinado_park_General_Paz = especimen_promedio_mas_inclinado(lista_arboles)
especimen_promedio_mas_inclinado_park_Centenario = especimen_promedio_mas_inclinado(lista2_arboles)
print(f'Promedio de inclinacion del especimen en el Parque Los Andes:{especimen_promedio_mas_inclinado_park_Los_Andes}')
print(f'Promedio de inclinacion del especimen en el Parque Centenario:{especimen_promedio_mas_inclinado_park_Centenario}')
print(f'Promedio de inclinacion del especimen en el Parque General Paz:{especimen_promedio_mas_inclinado_park_General_Paz}')
