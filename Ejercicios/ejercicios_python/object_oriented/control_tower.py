#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""

#%%
# <----------------- Clase Torre de control -------------------------------->
# <------------------------- Clase Cola ------------------------------------>
class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es también el primero en ser desencolado.
    '''
    # <-----------  Contructor --------------------->
    def __init__(self):
        '''Crea una cola vacía.'''
        self.items = []

    # <----------- Metodos especiales -------------->
    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola está vacía, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola está vacía')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola está vacía, 
        False si no.'''
        return len(self.items) == 0

#%%
# <----------------- Clase Torre de Control -------------------------------->
class TorreDeControl():
    '''
    Simulación de Torre de control
    '''
    # <-----------  Contructor --------------------->
    def __init__(self):
        '''
        Defino arribos y partidas de tipo Cola
        '''
        self.arribos = Cola()
        self.partidas = Cola()

    # <----------- Metodos especiales -------------->
    def nuevo_arribo(self, arribo):
        '''
        Inserto en arribos el próximo vuelo.
        Necesito como argumento el nombre del vuelo.
        '''
        return self.arribos.encolar(arribo)

    def nueva_partida(self, partida):
        '''
        Inserto en partidas el próximo vuelo
        Necesito como argumento el nombre del vuelo.
        '''
        return self.partidas.encolar(partida)

    def ver_estado(self):
        '''
        Reviso el estado de los vuelos en arribos y partidas
        '''
        print('Vuelos esperando para aterrizar:', ', '.join(self.arribos.items) if self.arribos else 'No hay vuelos')
        print('Vuelos esperando para despegar:', ', '.join(self.partidas.items) if self.partidas else 'No hay vuelos')

    def asignar_pista(self):
        if not self.arribos.esta_vacia():
            print(f'El vuelo {self.arribos.desencolar()} aterrizó con éxito')
        elif not self.partidas.esta_vacia():
            print(f'El vuelo {self.partidas.desencolar()} despegó con éxito')
        else:
            print('No hay vuelos en espera')

#%%

torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
