# -*- coding: utf-8 -*-
"""
@author: feder
"""
#%%
import csv
def leer_arboles(nombre_archivo):
    
    park = []
  
    try:
        with open(nombre_archivo,"rt",encoding = 'utf-8') as f:
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
        
arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
#%%
#altos de jaranda.
H=[float(arbol['altura_tot']) for i, arbol in enumerate(arboleda) if arboleda[i]['nombre_com']=="Jacarandá"]
#%%
#grafico de alto de jaranda.
import os
import matplotlib.pyplot as plt
import numpy as np
os.path.join('Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
altos = [H]
plt.hist(altos,bins=50)
#%%
import numpy as np
import matplotlib.pyplot as plt
import math
#Alto y diametro de jaranda.
Diametro_alto = [(float(arbol['diametro']),float(arbol['altura_tot'])) for i, arbol in enumerate(arboleda) if arboleda[i]['nombre_com']=="Jacarandá"]
data = np.array(Diametro_alto).T
colors=np.random.rand(3262)
plt.scatter(data[0],data[1],alpha=0.15)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")
plt.show()
#%%
#Ejercicio 5.31: Scatterplot para diferentes especies.
import os
import matplotlib.pyplot as plt

def medidas_de_especie(especies, arboleda):
    d = {especie:[(float(arbol['diametro']),float(arbol['altura_tot'])) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
    return d
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas1= medidas_de_especie(especies,arboleda)
os.path.join('Data', 'arbolado-en-espacios-verdes.csv')
medidas= medidas_de_especie(especies,arboleda)
data_eucalipto = np.array(medidas["Eucalipto"]).T
data_jacaranda = np.array(medidas["Jacarandá"]).T
data_Palo_borracho_rosado = np.array(medidas["Palo borracho rosado"]).T
#%%
plt.figure(1)
plt.scatter(data_eucalipto[0],data_eucalipto[1],alpha=0.15)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Eucalipto")
plt.show()
plt.figure(2)
plt.scatter(data_jacaranda [0],data_jacaranda[1],alpha=0.15)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para jacaranda")
plt.show()
plt.figure(3)
plt.scatter(data_Palo_borracho_rosado[0],data_Palo_borracho_rosado[1],alpha=0.15)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Palo borracho rosado")
plt.show()
 #%%