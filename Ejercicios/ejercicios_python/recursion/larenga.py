#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%%
# <----------------------- Triangulo de pascal ------------------------------>

def pascal(n, k):
    '''
    A partir de n, k >= 0, hallo el valor solicitado
    en el triangulo de Pascal
    n: fila, k: columna
    '''
    if (k == 0) or (n == k): # Caso base (fila 0 es 1 y tambien los lados)
        return 1
    else:
        return pascal(n-1, k-1) + pascal(n-1, k)

print(pascal(5, 2))

#%%
