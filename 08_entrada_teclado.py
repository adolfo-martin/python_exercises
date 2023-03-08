import os

os.system('cls')

nombre = input('Cuál es tu nombre: ')
edad = input('Cuál es tu edad: ')
edad = int(edad)

# print(f'Hola, soy {nombre} y tengo {edad} años')
print('Hola, soy ' + nombre + ' y tengo ' + str(edad) + ' años')