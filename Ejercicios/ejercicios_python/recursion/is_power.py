#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%%
# <------------------- Ejercicio 11.4: Potencias -------------------------->
    #<--input---> n y b son enteros positivos.
    #<---output--> True si n es potencia de b.   
def es_potencia(n, b): # b^x = n ?
    if n == b: # Caso base x = 1
        return True
    if n == 1: # Caso base x = 0
        return True
    if n > b: # Caso recursivo con n mayor a b (potencia: b^x = n?)
        resto = n % b
        if resto == 0:
            return es_potencia(n // b, b)
        else:
            return False
    if n < b: # Caso recursivo con n menor a b (raiz: n^x = b?)
        resto = b % n
        if resto == 0:
            return es_potencia(n, b // n)
        else:
            return False
#%%
print(es_potencia(8, 2))
print(es_potencia(64, 4))
print(es_potencia(70, 10))
print(es_potencia(1, 2))
#es_potencia(8, 2) -> True
#es_potencia(64, 4) -> True
#es_potencia(70, 10) -> False
#es_potencia(1, 2) -> True
