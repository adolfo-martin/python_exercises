#!/usr/bin/python3

try:
    numero = int(input('Introduce un número: '))

    if numero % 2 == 0:
        print('El número es par.')
    else:
        print('El número es impar.')
except:
    print('La expresión introducida no es un número entero.')
