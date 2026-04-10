#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""

#%%
# <------------------- Ejercicio 11.7: Máximo ----------------------------->
def maximo(lista):
    
    def max_aux(lista, n=0, maximo=0):
        
        if n==len(lista):
            return
        if maximo<lista[n]:
            maximo = lista[n]
        
        max_aux(lista, n+1, maximo)
        
        return maximo
    maximo = max_aux(lista)

    return maximo
#%%
m = maximo([1,5,89,3,6])
print(m)
