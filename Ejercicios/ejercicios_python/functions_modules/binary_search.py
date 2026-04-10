# -*- coding: utf-8 -*-
"""
@author: federico pfund
"""
#%%
#Ejercicio 6.11: Búsqueda binaria.
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
def donde_insertar(lista, x, verbose = False):
    
    if verbose:
        print(f'[DEBUG] izq |der |medio| Insertar |')
     # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        pos = medio
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}  |   {medio:3d}    |')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos
donde_insertar([1,2,4,6,7],5,verbose=(True))
#%%
#generamos una lista grande y preguntamos donde se podra insertar sin desordenar la lista.
import random
def generar_lista(n, m):
    '''
    devuelve una lista ordenada de n elementos diferentes entre 0 y m-1
    '''
    l = random.sample(range(m), k = n)
    l.sort()
    return l
#%%
m = 10000
n = 100
lista = generar_lista(n, m)
n= 6910# numero 3221
print(donde_insertar(lista, n))#donde insertar el numero que sale del random
#%%
#Insertar un elemento en una lista.

#%%
def insertar(lista, x, verbose = False):
    
    if verbose:
        print(f'[DEBUG] izq |der |medio| Insertar |')
     # Inicializo respuesta, el valor no fue encontrado
    pos = -1
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
       
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}  |   {medio:3d}    |')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if pos == -1:
        pos = medio
        lista.insert(pos,x)
        print(f'lista con una inserccion:{lista} en la pocicion {pos} el numero {x}')
    return pos
insertar([1,2,4,6,7],5,verbose=(True))
#%%
def incrementar(s):
    carry = 1
    l = len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s

incrementar([0, 1, 0, 0, 1])#9
incrementar([0, 0, 1, 1, 0])

incrementar([0, 0, 1, 1, 1])
incrementar([1, 1, 1, 1, 1])
incrementar([0, 0, 0, 0, 0])
#¿Te parece que incrementar() es una función lineal, cuadrática, logarítmica o exponencial?
#En terminos de complejida parece responder a una calculadora binaria.por lo que podemos decir que se categoriza como ? ?Por qué?
#

#%%
#Complejidad de incrementar()
def incrementar(s):
    carry = 1
    l = len(s)
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s
def listar_secuencias(n):# n toma la longuitud  de la lista!!
 
    s=[0]*n
    lista=[]
    lista.append(s)
    contador=0
    cantidad=(2**n)-1
    while contador<cantidad:
        s=incrementar(s)
        print(s)
        contador=contador+1
        copia = s.copy()
        lista.append(copia)
    return lista
b=listar_secuencias(11)
ejemplo=listar_secuencias(4)
#¿Cuántas listas hay de longitud n?
#proporcional a s*n
#¿Te parece que listar_secuencias(n) es una función lineal, cuadrática, logarítmica o exponencial en n? ¿Por qué?
#Lista_secuencia(n) es exponencial ya que el tamaña de n aumenta exponencialmente 
#%%
def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primer aparición, 
    de lo contrario devuelve -1.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps
busqueda_secuencial_([1,2,3,4,2,12,3,21,24,23], 5)[1]
#%%
def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    comps=0# sumo las comparacion que esta por haccer
    der = len(lista) - 1
    while izq <= der:
        comps += 1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
           
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos, comps
busqueda_binaria([1,2,3,4,6,12,31,32,34,36], 5,verbose=(True))[1]# Calcula las comparaciones que hace la busqueda binaria!
#%%


def generar_lista(n, m):
    import random
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)
#%%
m = 10000
n = 100
lista = generar_lista(n, m)

# acá comienza el experimento
x = generar_elemento(m)
comps = busqueda_secuencial_(lista, x)[1]
#%%
m = 10000
n = 100
k = 1000
lista = generar_lista(n, m)

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom
#%%
import matplotlib.pyplot as plt
import numpy as np

m = 10000
k = 1000

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos,comps_promedio,label = 'Búsqueda Secuencial')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaiciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()
#%%