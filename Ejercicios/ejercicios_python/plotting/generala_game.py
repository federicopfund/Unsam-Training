# -*- coding: utf-8 -*-
"""
@author: federico pfund
"""
#%%
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter # Utilizado para el Poker
np.random.seed(1231412)#para poder replicar el esperimento.
#%%
def tirar():

    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6)) 

    return tirada

tirada = tirar()
#%%
def es_generala(tirada): # servida
    return max(tirada)==min(tirada)
#%%
N=1000000
sumas=[sum(tirar()) for i in range(N)]
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
#¿Por qué varían más los resultados obtenidos con N = 100000 que con N = 1000000?
"""el comportamiento de variabilidad que se regleja, Se debe al tamaño de la muestra,
    ya que para tamaños grandes segun "ley de los grandes numeros" prescriben condiciones suficientes para garantizar que dicho promedio converja 
    al promedio de las esperanzas de las variables aleatorias involucradas. Las distintas formulaciones de la ley de los grandes números 
    especifican la convergencia de formas distintas.
        Si se repite un experimento aleatorio, bajo las mismas condiciones, un número ilimitado de veces;
    y si estas repeticiones son independientes la una de la otra, entonces la frecuencia de veces que un evento A ocurra,
    convergerá con probabilidad 1 a un número que es igual a la probabilidad de que A ocurra en una sola repetición del experimento"""
plt.hist(sumas,bins=24)# distribucion a la que converje la bernoulli.
#¿Cada cuántas tiradas en promedio podrías decir que sale una generala servida? 
promedio = round(N/G)
print(f'en promedio cada {promedio},veces sale una generala servida')
#¿Cómo se puede calcular la probabilidad de forma exacta?
# bueno una forma de calcular la forma exacta es tendiendo n -> infinito.. o tambien multiplicando
#la probabilidad del segundo para que sea igual al primero (1/6) por el tercero etc.
def probabilidad_exact(probabilidad_del_evento,numeros_de_eventos):
    return probabilidad_del_evento**(numeros_de_eventos-1)
probabilidad_exacta_generala=probabilidad_exact(1/6,5)
print(f' probabilidad  exacta:{probabilidad_exacta_generala}')
#%%
#Ejercicio 5.2: Generala no necesariamente servida.
# Esta función es la tirada random de X cantidad de dados
# se la invoca para la primer tirada de 5 dados
# también puede volver a invocarse para volver a tirar los 5 dados
# o para tirar nuevamente una cantidad x de dados elegidos
def tirar():

    dados= [random.randint(1, 6) for _ in range(5)]
    return dados
dados=tirar()
#me pregunto es generala? bueno verifiquemos.
def es_generala(dados):
    return max(dados)==min(dados)
es_general = es_generala(dados)
#pero tambien puede salir otra cosa como poker..
# Para encontrar el poker se debe importar el modulo Counter
#%%
def EsPoker(dados):
   cuenta = Counter(dados) # cuenta cuantas repeticiones hay de cada valor
   cuentaRepeticiones = (cuenta.most_common(1)) # genera una lista mostrando qué valor es el mas repetido y cuántas veces se repitió
   maxRepeticion = cuentaRepeticiones[0][1] # muestra el número de veces que se repitió el valor mas repetido
   if maxRepeticion == 4:# si el valor mas repetido se repitió cuatro veces devuelve True, sino False.
       return True
   else:
       return False
dead= EsPoker(dados)
#%%
#calcularemos la probabilidad de sacar un poker.
N=1000000
u = sum([EsPoker(tirar()) for i in range(N)])
probabilida_poker = u/N
print(f'Tiré {N} veces, de las cuales {u} fueron poker.')
print(f'Podemos estimar la probabilidad de sacar poker es: {probabilida_poker:.6f}.')
#%%
#tambien es posible sacar Full..
# La i toma el primer valor de jugada hasta el ultimo,
# pregunta valor por valor la cantidad de veces que está repetido
# si el valor i esta 3 veces dentro de la jugada, me retorna True
# si hay otro valor que está 2 veces me retorna True.
# Si ambos se cumplen retorna True, de lo contrario retorna False.
def EsFull(dados):
    hay_tres=False
    hay_dos=False
    for i in range (0,len(dados)):
        if dados.count(dados[i])==3:
            hay_tres=True
        if dados.count(dados[i])==2:
           hay_dos=True
    return hay_tres and hay_dos

r = sum([EsFull(tirar()) for i in range(N)])
probabilidad_Full = r/N
print(f'Tiré {N} veces, de las cuales {r} fueron Full.')
print(f'Podemos estimar la probabilidad de sacar Full es: {probabilidad_Full:.6f}.')
#%%
# La función establece las dos posibles escaleras que existen dentro del juego.
# Luego ordena la jugada, si es igual a alguna de las dos escaleras retorna true.
def esEscalera(dados):
    esc1=[1,2,3,4,5]
    esc2=[2,3,4,5,6]
    if sorted(dados)==esc1 or sorted(dados)==esc2:
        return True
    else:
        return False
p = sum([esEscalera(tirar()) for i in range(N)])
probabilidad_Escalera = p/N
print(f'Tiré {N} veces, de las cuales {p} fueron escalera.')
print(f'Podemos estimar la probabilidad de sacar escalera es: {probabilidad_Escalera:.6f}.')
#%%
#pero tambien podemos pensar en seleccionar dados que se repitan y guardarlo y tirar los restantes..
#veremos como influye en la estrategia este metodo de jugada..
# segun los dados obtenidos y un valor de dado pedido al usuario anteriormente
# recorre la lista de dados para averiguar cuantas veces está ese dado repetido
# finalmente imprime una cadena con esa información y retorna los puntos obtenidos
# al multiplicar el valor del dado x la cantidad de veces que se ha repetido
import collections #proyecto copia y rediseño :(Maite Echeveste...) sacado de slack
def generala_no_servida(dados):
    repeticion= collections.Counter(dados)#genera diccionario con las cantidad de repeticion
    mas_repet= repeticion.most_common(1)#lista de tuplas(numero que se repite,cantidad de repeticion)
    maxRepeticion = mas_repet[0][1] # muestra el número de veces que se repitió el valor mas repetido
    dado_mas_repetido= mas_repet[0][0]#cuantas veces salio dicho dado
    for k in range(2):
        if dado_mas_repetido < 5:
            dados = [random.randint(1,6) for _ in range(5-dado_mas_repetido)]#tiro las veces necesarias 
            repeticion = collections.Counter(dados)#diccionario con las cantidad de repeticion
            mas_repet = repeticion.most_common(1)
            maxRepeticion1 = mas_repet[0][1] # muestra el número de veces que se repitió el valor mas repetido
            dado_mas_repetido1= mas_repet[0][0]#cuantas veces salio dicho dado
            if dado_mas_repetido1 > dado_mas_repetido:#compara si en la segunda tirada saca dados mas repetidos.
                dado_mas_repetido = dado_mas_repetido1# de ser true asigna dicho valor a la variable pre definida.
                maxRepeticion = maxRepeticion1 #tambien asigna la maxima repeticiondel dado en dicha jugada.
            else:# si no 
                dado_mas_repetido += dados.count(maxRepeticion)# acumula  la cantidad de veces que va saliendo el dado mas repetido.
        else:#salio generala en el primer o segundo tiro
            return [maxRepeticion]*dado_mas_repetido
            break
    for k in dados:
        if k == maxRepeticion:
            dados.remove(k)
        ultima = [maxRepeticion]*dado_mas_repetido + dados
        return ultima
#%%
"""
​def SalidaDeNumero(dados,valor):
    cantidad_de_repeticiones=0
    for i in dados:
        if i==valor:
            cantidad_de_repeticiones+=1
    multiplicacion = (valor*cantidad_de_repeticiones)
    print("El dado",valor,"salio:",cantidad_de_repeticiones,"veces. Obtuvo",multiplicacion,"puntos.")
    return multiplicacion
"""