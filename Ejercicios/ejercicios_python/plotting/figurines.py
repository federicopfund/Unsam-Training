# -*- coding: utf-8 -*-
"""@author: feder
"""
#%%
from matplotlib import pyplot as plt
import numpy as np
import random
figus_total=670
#%%
#Ejercicio 5.9: Crear
def crear_album(figus_total):
	'crea un album vacio de figuritas'
	album = np.zeros(figus_total) #armo vector de 670 ceros.
	return album
A = crear_album(figus_total)
#%%
#Ejercicio 5.10: Incompleto

def album_incompleto(A):
	'recibe un vector y devuelve True si el vector contiene el elemento 0, y False en otro caso.'
	var = True
	if np.prod(A!= 0): # np.prod hace el producto de los elementos de A, si algun elemento es cero, da cero.
		var = False
	return var
contiene_elemento_cero = album_incompleto(A)
#%%

def albumQ_incompleto(A):
   
    estado = 0 in A
    return estado
contiene_elemento_cero1=albumQ_incompleto(A)
#%%

def	comprar_figu(figus_total):
	'recibe número total de figuritas que tiene el álbum y devuelve un número entero aleatorio'
	num_de_figu = random.randint(0,figus_total-1)
	return num_de_figu
Numero_entero_aleatorio = comprar_figu(figus_total)
#%%
def cuantas_figus(figus_total):
	'genera un album nuevo, simula su llenado y devuelve la cantidad de figuritas que se debieron comprar para completarlo'

	album = crear_album(figus_total) 	#genero album nuevo
	contador = 0 #inicializo contador
	while album_incompleto(album): 
		num_de_figu = comprar_figu(figus_total)  #calculo num de figu random
		if album[num_de_figu-1] >= 1:
			album[num_de_figu-1] += 1
		else:
			album[num_de_figu-1] = 1
		contador+=1
	return contador#, album
Album_nuevo_llenado = cuantas_figus(figus_total)
#%%
print(f'La cantidad de figuritas que tuve que comprar para llenar el album es de {Album_nuevo_llenado }')

#%%
n_repeticiones  = 100
resultados = [cuantas_figus(figus_total) for _ in range(n_repeticiones)]
promedio = np.mean(resultados)
print(f"El promedio de veces que debemos comprar figuritas para completar el album es {promedio:.2f}")
#%%
#Ahora con paquetes
def comprar_paquete(figus_total, figus_paquete):
    
    album_nuevo = crear_album(figus_total)
    
    a_list = list(range(figus_total)) # me armo una lista de las figus_total
    paquete = random.choices(a_list, k= figus_paquete) # acá armo paquetes con reposicion de a figus_paquete para asegurarme de que se pueden repetir.
        
    return paquete
comprar_por_paquete= comprar_paquete(670,5)
#%%

def cuantos_paquetes_figus_sinrepetir(figus_total, figus_paquete):
    'en base al tamaño del album, y la cantidad de figus por paquete,crea un album nuevo, simula su llenado  y devuelve la cantidad de paquetes de figuritas que se deberían comprar para completarlo'
    album_nuevo = crear_album(figus_total)
    contador_n = 0
    while album_incompleto(album_nuevo):
        a_list = list(range(figus_total)) # me armo una lista de las figus_total
        paquete = random.sample(a_list,k=figus_paquete) # acá armo paquetes sin reposicion de a figus_paquete para asegurarme que en el paquete no haya repetidas
        for figurita in paquete:
            album_nuevo[figurita-1] = 1
        contador_n+= 1
    return contador_n
Cuantos_paquetes_figus_sinrepetir=cuantos_paquetes_figus_sinrepetir(670, 5)
#%%
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas
figus_total = 670
figus_paquete = 5
plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()
#%%