#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%%
# <--------------- Ejercicio 11.5 subcadenas --------------------------------->

def posiciones(a, b):
    #<--input---> recibe como parámetros dos cadenas a y b,
    #<---output---> una lista con las posiciones en donde se encuentra b dentro de a.
    index_found = []
    if len(a) < len(b): # Caso base
        return index_found

    if a[-len(b):] == b: # Caso recursivo
        index_found.append(a.index(b, -len(b)))
        index_found += posiciones(a[:-1], b) 
        return index_found

    else:
        return posiciones(a[:-1], b)
#%%
print(posiciones('Un tete a tete con Tete', 'te')[::-1])