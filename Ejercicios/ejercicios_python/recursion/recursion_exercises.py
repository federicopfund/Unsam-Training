#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""

#%% 
#<---------------- Números triangulares ---------------------------------->

def suma_triangular(n):
    #<----input ---> n>=0
    #<----output ---> la sumatoria de cada numero desde 0 hasta n.
    if n==0:
        return 0
    return n + suma_triangular(n-1)

#%%
#<--------------------- Ejercicio 11.3: Dígitos -------------------------->

def digitos(n):
    # <---input ---> n>0
    # <---output --> El numero de digitos de n.
    n = str(n)    
    if len(n) == 0:
        return 0
        
    return 1 + digitos(n[1:])
    
    
#%%
# <------------------- Ejercicio 11.4: Potencias -------------------------->

def es_potencia(n,b):
    
    #<--input---> n y b son enteros positivos.
    #<---output--> True si n es potencia de b.    
    potencia=False    
    if n==1:
        potencia=True
        return potencia
    elif n<1:
        return potencia
    else:
        potencia = es_potencia(n/b,b)
        
    return es_potencia

print(es_potencia(27, 3))
#%%
#  <-------------  Ejercicio 11.5: Subcadenas ----------------------------->

def posiciones_de(cadena, subcadena):
    
    #<--input---> recibe como parámetros dos cadenas a y b,
    #<---output---> una lista con las posiciones en donde se encuentra b dentro de a.
    def pos_aux(cadena, subcadena, pos=[]):
        if len(cadena) < len(subcadena):
            return
        
        if cadena.endswith(subcadena):
            l_sub = len(subcadena)
            pos.append(len(cadena)-l_sub)    
            pos_aux(cadena[:-l_sub], subcadena, pos)
        else:
            pos_aux(cadena[:-1], subcadena, pos)
        
        return pos
    
    return pos_aux(cadena, subcadena)
    
l=posiciones_de('ru ru ru rustiqui', 'ru')
    
#%% 
#<------------------- Ejercicio 11.6: Paridad ---------------------------->

def impar(n):
    return n==1

def par(n):
    pass


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

m = maximo([1,5,89,3,6])
print(m)
