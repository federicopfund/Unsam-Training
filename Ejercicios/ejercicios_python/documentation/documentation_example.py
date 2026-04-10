# -*- coding: utf-8 -*-
"""
@author: federico pfund
"""
#%%

#Ejercicio 7.8: Funciones y documentación
#Para cada una de las siguientes funciones:
#Pensá cuál es el contrato de la función.
#Agregale la documentación adecuada.
#Comentá el código si te parece que aporta.
#Detectá si hay invariantes de ciclo y comentalo al final de la función


#%%
def valor_absoluto(n):
    '''Precondición:Recibe un número. Poscondición: Devuelve el valor absoluto'''
    if n >= 0:
        return n
    else: #n° negativos
        return -n
    

#%%

def suma_pares(l):
    '''Precondición: Toma lista de números positivos. Poscondición: Devuelve total de sumar los pares'''
    res = 0
    for e in l:
        if e % 2 ==0: #Múltiplos de 2
            res += e
        else:
            res += 0

    return res

#Invariantes:variable res contiene la suma de todos los elementos pares ya recorridos. 

#%%
def veces(a, b):
    '''Precondición: Recibe a,b números. b número positivo. Poscondición: a*b'''
    res = 0
    nb = b
    while nb != 0:
        print(nb * a + res)
        res += a
        nb -= 1
    return res

a =veces(-2,-4)
a
#Invariantes: Res suma a por cada vez que pueda hacer b-1 antes de que b != 0
#%%

def collatz(n):
    '''Precondición: n entero,positivo. Poscondición: Partiendo de n aplica la Conjetura de Collatz y devuelve la cantidad de veces que se iteró hasta llegar a 1.'''
    res = 1 #cantidad de veces que iteró
    while n!=1:
        if n % 2 == 0: #pares
            n = n//2
        else: #impares
            n = 3 * n + 1
        res += 1

    return res
#Invariantes: Imposible de encontrar si esque los hay
collatz(10)
