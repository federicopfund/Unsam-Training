#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%%
# <---------------------- Clase Lote para el informe ------------------------>
class Lote:
    '''
    Clase lote para elaboración de informe de camion
    '''
    def __init__(self, nombre, cajones, precio):
        '''
        Defino mis atributos nombre, cajones y precio
        '''
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        '''
        Devuelvo costo = cajones * precio
        '''
        return (self.cajones * self.precio)
    
    def vender(self, caj_vender):
        '''
        Vendo cajones y resto del total
        '''
        self.cajones -= caj_vender

    def __repr__(self):
        '''
        Muestro contenido de Lote en memoria
        '''
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'
#%%
class Lote_inf(Lote):
    def costo(self):
        '''
        Devuelvo costo = cajones * precio
        '''
        return 1.25*self.cajones * self.precio
#%%
b = Lote_inf('pera',100,10)
print(b.costo())
# <----------------------------- Testeo ------------------------------------->
import lote
a = lote.Lote('Pera', 100, 490.10)
b = lote.Lote('Manzana', 50, 122.34)
c = lote.Lote('Naranja', 75, 91.75)
b.cajones * b.precio
c.cajones * c.precio
lotes = [a, b, c]
lotes
#%%
# <------------------------- Imprecion en consola --------------------------->
for c in lotes:
     print(f'{c.nombre:>10s} {c.cajones:>10d} {c.precio:>10.2f}')
#%%
s = lote.Lote('Pera', 100, 490.10)
s.costo()
s.cajones
s.vender(25)
s.cajones
s.costo()
#%%
# <----------------------- Lista de Instancias ------------------------------>
import fileparse
with open('../Data/camion.csv') as lineas:
     camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'],
                                                               types = [str, int, float])

camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
camion
sum([c.costo() for c in camion])
#%%