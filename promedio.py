"""Promedio"""
from math import sqrt

def desviacion_std(lista,media):
    a=0
    for valor in lista:
        a += (valor - media)**2
    y = a/(len(lista)-1)
    
    return sqrt(y)

def promedio_std(lista):
  x=0
  for valor in lista:
    x += valor
  x = x/len(lista)
  return x

lista = list(map(int,input('Introduce los numeros: \n').strip().split()))
media=promedio_std(lista)
resultado=desviacion_std(lista,media)
print(f'Tu promedio es: {media}\n')
print(f'Tu desviacion estandar es: {resultado}\n')