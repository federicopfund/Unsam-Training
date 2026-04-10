# -*- coding: utf-8 -*-
"""
Created on Sat May 29 12:52:38 2021

@author: feder
"""

def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    
    assert (type(desde)==int and type(hasta)==int) ,"ingrese numeros enteros"
    sumas=0
    if hasta>=desde:
           
        for i in range(desde,hasta+1):
            sumas += i
        return sumas
    return 0       
   
sumar_enteros(0,0)
