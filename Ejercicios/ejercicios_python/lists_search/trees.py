# -*- coding: utf-8 -*-
"""
@author: federico pfund
"""
#%%
#Ejercicio 4.18: Lectura de todos los árboles.
import csv
def leer_parque(nuevo_archivo):
    
    park = []
  
    try:
        with open(nuevo_archivo,"rt",encoding = 'utf-8') as f:
            row = csv.reader(f)
            headers = next(row)  
            i=0
            for i, line in enumerate(row,start=1):
                try:#levantamos indexerror
                    registro = dict(zip(headers,line))
                    
                    park.append(registro)
                                                
                except IndexError:
                    pass       
        return park
        
    except FileNotFoundError or TypeError: 
          print(f'No corresponde a una direccion válida.') 
        
arboleda = leer_parque('../Data/arbolado-en-espacios-verdes.csv')
#%%
#Ejercicio 4.19: Lista de altos de Jacarandá.
H=[float(arbol['altura_tot']) for i, arbol in enumerate(arboleda) if arboleda[i]['nombre_com']=="Jacarandá"]
#%%
#Ejercicio 4.20: Lista de altos y diámetros de Jacarandá.
Diametro_alto =[(float(arbol['altura_tot']),float(arbol['diametro'])) for i, arbol in enumerate(arboleda) if arboleda[i]['nombre_com']=="Jacarandá"]
#%%
#Ejercicio 4.21: Diccionario con medidas.
def medidas_de_especies(especies,arboleda):
   d={}
   for especie in especies:
       d[especie] = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]
   return d
   
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies,arboleda)
#%%
#comprecion de lista:
def medidas_de_especie(especies, arboleda):
    d = {especie: [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
    return d
medidas1= medidas_de_especie(especies,arboleda)
#%%

