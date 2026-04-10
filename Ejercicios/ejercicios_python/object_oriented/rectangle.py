# -*- coding: utf-8 -*-
# <-----------------------------Clase Rectangulo ---------------------------->
"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%%
# <------------------------------ Imports ----------------------------------->
import pprint
#%%
# <---------------- Defino un punto ------------------->
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

    def __add__(self, b):
      return Punto(self.x + b.x, self.y + b.y)
  

    def __str__(self):
        return f'({self.x}, {self.y})'

   
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
#%%
# <---------------- Clase Rectangulo ------------------------>    
class Rectangulo():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # Esquinas
        self.esquina = {
            'inferior_derecho' : Punto(max(p1.x, p2.x), min(p1.y, p2.y)),
            'superior_derecho' : Punto(max(p1.x, p2.x), max(p1.y, p2.y)),
            'inferior_izquierdo' : Punto(min(p1.x, p2.x), min(p1.y, p2.y)),
            'superior_izquierdo' : Punto(min(p1.x, p2.x), max(p1.y, p2.y)),
            }
        
    def base(self):
        return abs(self.p1.x - self.p2.x)
    
    def altura(self):
        return abs(self.p1.y - self.p2.y)
    
    def area(self):
        return self.base() * self.altura()
    
    def posicion_relativa(self):
        for k, esquina in self.esquina.items():

            if esquina.__repr__() == self.p1.__repr__():
                bandera_p1 = k
            if esquina.__repr__() == self.p2.__repr__():
                bandera_p2 = k
        
        return bandera_p1, bandera_p2
                
                
    def rotar(self):
        punto_relativo1, punto_relativo2 = self.posicion_relativa()
        
        self.esquina['superior_derecho'] += Punto(self.altura(), - self.altura())
        self.esquina['inferior_izquierdo'] += Punto(self.base(), self.base())
        self.esquina['superior_izquierdo'] += Punto(self.base() + self.altura(),
                                                - self.altura() + self.base())
        
        self.p1 = self.esquina[punto_relativo1]
        self.p2 = self.esquina[punto_relativo2]
        
        return self.p1, self.p2
        
        
    def desplazar(self, desplazamiento):
        
        self.p1 += desplazamiento
        self.p2 += desplazamiento
        return self.p1, self.p2
        
        
        
    def __str__(self):
        return f'Rectangulo -> base:{self.base()} , altura: {self.altura()}'
    
    def __repr__(self):
        return f'Rectangulo({self.p1.__repr__()}, {self.p2.__repr__()})'
    
#%%
# <-------------Analisis---------------->
punto = Rectangulo(Punto(1, 2), Punto(3, 9))
print('Punto1 -> ', punto.p1)
print('Punto2 -> ', punto.p2)
pprint.pprint(punto.esquina)
punto.rotar()
print()
print('|<{:-^35}>|'.format('Rotar Rectangulo'))
pprint.pprint(punto.esquina)
print()
print('|<{:-^35}>|'.format('Luego de Rotar'))

print('Punto1 -> ', punto.p1)
print('Punto2 -> ', punto.p2)
