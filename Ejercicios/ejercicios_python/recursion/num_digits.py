#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%% <--- Ejercicio 11.3: Dígitos---->
""""Escribí una función recursiva que reciba un número positivo,
     n, y devuelva la cantidad de dígitos que tiene."""
def digitos(n):
    dig = 1
    if n < 10: # Caso base
        return 1
    else: # Caso recursivo
        n /= 10
        dig += digitos(n)
        return dig

num = 689132

print (digitos(num))