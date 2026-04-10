#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Federico Pfund
 E-mail:federicopfund@gmail.com 
"""
#%%
# <------------------------------ Imports ----------------------------------->
import informe as informe
import lote
import sys
#%%
# <------------------------- Costo del camion ------------------------------->

def costo_camion(file_name):
    # Variables
    costo = 0
    rows = informe.leer_camion(file_name)

    # Imprimo datos y, a la vez, calculo precio de cajones
    for i, row in enumerate(rows, start=1):
        try:
            Ncajones = row.cajones
            Precio = row.precio
            costo += Ncajones * Precio
        except ValueError: # Si faltan datos, tirame un warning
            print(f'Fila {i}: No se puede interpretar: {row}')
    # Retorno con resultado
    return (costo)

# <----------------------------- Main --------------------------------------->
def main (argv):
    if len(sys.argv) != 2:
            raise SystemExit(f'Uso adecuado: {sys.argv[0]}' ' archivo_camion ')
    duele = costo_camion('../Data/camion.csv')
    print('\nTotal pagado por los cajones es: $', round(duele,2))

# <--------------------------- Sys ------------------------------------------>
if __name__ == '__main__':
    main(sys.argv)
# <----------------------------Por Terminar --------------------------------->
#python ../Data/camion.csv