#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""

#%% 
# <--------------------- Busqueda binaria ------------------------------------>
def bbinaria_rec(lista, e):
    '''
    Realizo busqueda binaria de un valor 'e' dentro de una lista dada
    '''
    if len(lista) == 0: # Caso base: lista vacia
        res = False
    elif len(lista) == 1: # Caso base: lista con un elemento e igual al buscado
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if e in lista[:medio]:
            return bbinaria_rec(lista[:medio], e)
        else:
            return bbinaria_rec(lista[medio:], e)
    return res
#<-------------Tendria que dar TRUE ------------------------------------------>
print(bbinaria_rec([1, 5, 3, 2, 8, 5, 0, 63], 3))

#<-------------Tendria que dar FALSE------------------------------------------>

print(bbinaria_rec([1, 5, 3, 2, 8, 5, 0, 63], 12))