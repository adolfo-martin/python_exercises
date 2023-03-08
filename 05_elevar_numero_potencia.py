import os

os.system('cls')

# Primera forma
base = 2
exponente = 8

resultado = base ** exponente
print(f'El número {base} elevado a {exponente} es {resultado}')
print(f'El número {3} elevado a {5} es {3 ** 5}')

# Segunda forma
base = 5
exponente = 2
resultado = pow(base, exponente)
print('El número %d elevado a %d es %d' % (base, exponente, resultado))

# Tercera forma
import math

resultado = math.pow(4, 3)
print(f'El número 4 elevado a 3 es {resultado}')
