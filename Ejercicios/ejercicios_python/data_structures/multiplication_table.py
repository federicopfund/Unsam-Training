# -*- coding: utf-8 -*-
"""
@author: federico pfund
"""
def tabla(n):
    print('      ',end=' ')
    for j in range (n):
        print(f'{j:>5}',end='')
    print('\n' )
    print('      ','-----'*n, end='')
    for x in range (n):
        valor = 0
        print()
        print(f'{x:>5}:|',end='')
        for y in  range(n):
            print(f'{valor:>5}',end='')
            valor = valor + x
tabla(11)          
