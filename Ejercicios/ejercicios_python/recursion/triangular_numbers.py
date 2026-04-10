#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%%
# <------------------------ Numeros Triangulares ---------------------------->
def triangular(n):
    suma = 0
    if n == 1: # Caso base
        return 1
    else: # Caso recursivo
        suma += triangular(n-1) + n
        return suma

num = 3

print(triangular(num))
#%%