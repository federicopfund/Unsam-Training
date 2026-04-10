# -*- coding: utf-8 -*-
"""
@author: federico pfund
"""
#%%
#Ejercicio 4.8: Invertir una lista.

def invertir_lista(lista):
    invertida = []
    for e in lista[::-1]: # Recorro la lista
        invertida.append(e) #agrego el elemento e al principio de la lista invertida
    return invertida

lista=[1, 2, 3, 4, 5]
lista1=['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
invirtiendo = invertir_lista(lista1)
#%%