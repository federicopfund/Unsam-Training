#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%%
#<------------------------- Orden por Seleccion ----------------------------->
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección."""
       #<--input-->: los elementos de la lista deben ser comparables.
       #<--otout-->: la lista está ordenada.
    
    # posición final del segmento a tratar
    n = len(lista) - 1
    comparaciones = 0

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        comparaciones += n

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1

    return comparaciones
#%%
#<------------------------ Buscar Maximo ------------------------------------>
def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max
#%%
#<------------------------------- Testeo ------------------------------------>
lista = [3,0,1,2]# defino lista
resu = ord_seleccion(lista)
print(resu)