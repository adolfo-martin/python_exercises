import os

os.system('cls')

numero_decimal = input('Dame el número decimal: ')
numero_decimal = int(numero_decimal)

numero_binario = ''
cociente = numero_decimal

while cociente >= 2:
    resto = cociente % 2
    cociente = cociente // 2

    numero_binario = str(resto) + numero_binario
    
numero_binario = str(cociente) + numero_binario
print(numero_binario)