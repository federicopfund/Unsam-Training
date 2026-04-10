#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%%
#<-------------------------hoja_ISO Recurcion -------------------------------->
def hoja_A(N):
    '''
    Dado un valor N >= 0, obtengo ancho y largo de la hoja
    '''
    ancho = 841
    largo = 1189

    if N > 10: # Caso base: N mayor a norma establecida
        return f'Tamaño mínimo: A10'
    elif N == 0: # Caso base: N == 0
        return (ancho, largo)
    else:
        (ancho, largo) = hoja_A(N-1)
        if ancho > largo:
            ancho //= 2
        else:
            largo //= 2
        return (ancho, largo)
#%%

for j in range(11):
    (ancho, largo) = hoja_A(j)
    print(f'Hoja A{j} => Ancho: {ancho} y Largo: {largo}')
    
#%%
