# -*- coding: utf-8 -*-

nombre_fruta = input('Ingrese fruta: ')
def buscar_precio(nombre_fruta):
    with open('../Data/precios.csv', 'rt', encoding='utf-8') as f:	# Abre el archivo en subd /Data
        costo=0
        for line in f:			# Lee por cada línea
            row = line.split(',')	# Lee por cada elemento del row por separado
            fruta = row[0]		# Lee la clase de fruta
            try:
                if fruta == nombre_fruta:
                    precio = float(row[1])	# Lee precio por cajón
                    costo = precio
            except:
                  print(f'{nombre_fruta} no figura en el listado de precios')
    return costo    
            
costo = buscar_precio(nombre_fruta)
print(f'El precio de la {nombre_fruta} es: {costo:0.2f}')	# Muestra en pantalla


"""Construcción de diccionarios"""

precios = {}  # Empezamos con un diccionario vacío

with open('../Data/precios.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        try:
            precios[row[0]] = float(row[1])
            
        except IndexError:
            
            print(f'se encontro una ecepcion..')
            
print(f'{precios}\n')

