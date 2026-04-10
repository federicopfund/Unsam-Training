# -*- coding: utf-8 -*-
"""
@author: federico pfund.
"""
#%%
#Ejercicio 4.6: Búsquedas de un elemento
def buscar_u_elemento(lista,e):
    
    for t, i in enumerate(lista):
        if i == e:
            return t
    else:
         return -1

primera_algo = buscar_u_elemento([1,2,3,2,3,4],1)
primera_algo1 = buscar_u_elemento([1,2,3,2,3,4],2)
primera_algo1 = buscar_u_elemento([1,2,3,2,3,4],3)
primera_algo1 = buscar_u_elemento([1,2,3,2,3,4],5)
""" busca y cuenta la cantidad de elementos que aparecen en la lista, 
 tambien guarda la posicion en la que se encuetra """
def buscar_n_elemento(lista,e):
    cuenta = 0
    lista_de_pocicion= []
    for i, elemento in enumerate(lista):
        if elemento == e:
            cuenta += 1
            lista_de_pocicion.append(i)
            
    return cuenta, lista_de_pocicion

buscar = buscar_n_elemento([1,2,3,2,3,4],1)
buscar = buscar_n_elemento([1,2,3,2,3,4],2)
buscar = buscar_n_elemento([1,2,3,2,3,4],3)
buscar = buscar_n_elemento([1,2,3,2,3,4],5)

#%%
#Ejercicio 4.7: Búsqueda de máximo y mínimo

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = 0 # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e >= m:
            m=e
      
    return m
maxi=maximo([1,2,7,2,3,4])
maxi1=maximo([1,2,3,4])
maxi2=maximo([-5,4])
maxi3=maximo([-5,-4])
#¿Por qué falla en el último caso? 
"""falla en el ultimo caso porque la variable m inicia m=0
  por lo tanto se toma como inicio el 0"""
#¿Por qué anda en el caso anterior?
"""bueno como el maximo en este caso es cuatro positivo se evalua y se lo deja como 
  el maximo,por arriva del 0"""
#¿Cómo se puede inicializar m para que la función ande también con números negativos?
"""se podria iniciar en cero y que considere la comparacion de numeros negativos"""

#%%
def maximo(lista):
    lista.sort()    
    return lista[-1]
lista=[-1,-1,-4,-1,-9]
lista2= [3,2,5,6,2,1]
maxis = maximo(lista)

def minimo(lista):
    lista.sort()
    return lista[0]
lis = [-2,-3,5,9,-9,2]
mini = minimo(lis)
#%%
#Ejercicio 6.10: Búsqueda lineal sobre listas ordenadas.
#En el peor caso, ¿cuál es nuestra nueva hipótesis sobre comportamiento del algoritmo? 
#¿Es realmente más eficiente?
#la hipotesis es que demanda menos comparaciones por lo que reduce el esfuerzo computacional,
#de se asi reduce el tiempo de respuestas..
#en secciones superiores analizaremos que tan eficiente es al evaluar la cantidad de recurso que utiliza 
#para ordenar dicha lista
def busqueda_lineal_lordenada(lista,e):
    lista.sort()
    for i, elemento in enumerate(lista):
        if elemento==e:
            return i
        elif elemento>=e:
            return -1
lista_lineal_ordenada= busqueda_lineal_lordenada([1,2,4,6,8,6,7,5,6],5)
#%%
def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    lista.sort()
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos
busqueda_bina= busqueda_binaria([1,2,4,6,8,6,7,5,6],5,verbose=(True))
#%%
busqueda_binaria([1, 3, 5], 0, verbose = True)
#%%
busqueda_binaria([1, 3, 5], 1, verbose = True)
#%%
busqueda_binaria([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],18, verbose = True)
#%%
busqueda_binaria([1, 3, 5], 6, verbose = True)
#%%
#En la línea medio = (izq + der) // 2 efectuamos la división usando el operador // en lugar de /. ¿Qué pasaría su usáramos /?
#bueno para redondear a numeros enteros es necesario usar la doble barra ya los elementos da la lista se encuentran en pocicione enteras..
