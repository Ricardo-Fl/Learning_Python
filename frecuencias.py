"""Frecuencias de Colores"""

#lista = ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde',
        #'verde', 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo']

def color_frecuente(lista):
    colores = {'azul':0, 'rojo':0, 'verde':0, 'amarillo':0}
    for letter in lista:
        if letter == 'azul':
            colores['azul'] += 1
        elif letter == 'rojo':
            colores['rojo'] += 1
        elif letter == 'verde':
            colores['verde'] += 1
        elif letter == 'amarillo':
            colores['amarillo'] += 1

    if (colores['azul'] >= colores['rojo'] and colores['azul'] >= colores['verde'] and colores['azul'] >= colores['amarillo']):
        print(f'"azul"', colores['azul'],)
    elif(colores['rojo'] >= colores['verde'] and colores['rojo'] >= colores['amarillo'] and colores['rojo'] > colores['azul']):
        print(f'"rojo"', colores['rojo'],)
    elif(colores['verde'] >= colores['amarillo'] and colores['verde'] > colores['azul'] and colores['verde'] > colores['rojo']):
        print(f'"verde"', colores['verde'],)
    elif(colores['amarillo'] > colores['azul'] and colores['amarillo'] > colores['rojo'] and colores['amarillo'] > colores['verde']):
        print(f'"amarillo"', colores['amarillo'],)

#lista=[]
#lista.append(valor)
lista=[input("Ingrese los colores: \n")]
color_frecuente(lista)