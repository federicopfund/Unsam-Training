#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%%
# |----------------------> auße der Liebe,nights <---------------------------|
# <----------------------- Clase Canguro ------------------------------------>
class Canguro:
    # <-----------  Contructor --------------------->
    def __init__(self, nombre, contenido_marsupio=[]):
        '''
        __init__(string nombre, list marsupio)
        Defino nombre y contenido en marsupio del canguro
        '''
        self.nombre = nombre
        self.contenido_marsupio = contenido_marsupio
    
    # <---------- Meter en Marsupio ---------------->
    def meter_en_marsupio(self, cosa):
        
        # <---input----> "string"-> cosa
        # <---output---> ["contenido dentro de marsupio"]
        
        self.contenido_marsupio.append(cosa)
        
    # <---- Metodo especial "__str__" ------------->
    def __str__(self):
        '''Crea lista de strings con datos del canguro
        '''
        inventario = [self.nombre + ' tiene en su marsupio: ']
        for cosito in self.contenido_marsupio:
            inventario.append('\t'*2 + '-> ' + cosito)
        return '\n'.join(inventario)
#%%    
# <----- La gran Creacion de la clase ------------>   
madre = Canguro('Mamá Canguro')
hijo = Canguro('El Señor Grimson')
madre.meter_en_marsupio('La teoria del todo')
madre.meter_en_marsupio('Voon Neumann')
madre.meter_en_marsupio(hijo.nombre)
print(madre)
#%%

# <--------------- Canguro_Malo -------------------->
"""Este código continene un bug importante y dificil de ver"""
#%%
class Canguro:
    # <-----------  Contructor --------------------->    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido
        
    # <---- Metodo especial "__str__" ------------->
    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        # <---input----> "string"-> item ---->objeto
        # <---output---> ["contenido dentro de marsupio"]
        self.contenido_marsupio.append(item)

#%%
# <----- La gran Creacion de la clase ------------>  
madre_canguro = Canguro('Madre')
cangurito = Canguro('Hipegrafos asincronicos')
madre_canguro.meter_en_marsupio('Automata Celular')
madre_canguro.meter_en_marsupio('Regla del 30') #---->LA SOLUCION
#madre_canguro.meter_en_marsupio(cangurito)
madre_canguro.meter_en_marsupio(cangurito.nombre)

print(madre_canguro)
#%%

