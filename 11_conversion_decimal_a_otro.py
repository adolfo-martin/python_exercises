import os

os.system('cls')

numero_decimal = input('Dame el número decimal: ')
numero_decimal = int(numero_decimal)

base_sistema = int(input('Dame la base del sistema de numeración (2|8|16): '))


numero_binario = ''
cociente = numero_decimal

while cociente >= base_sistema:
    resto = cociente % base_sistema
    cociente = cociente // base_sistema

    if base_sistema == 16:
        if resto == 10:
            numero_binario = 'A' + numero_binario
        elif resto == 11:
            numero_binario = 'B' + numero_binario
        elif resto == 12:
            numero_binario = 'C' + numero_binario
        elif resto == 13:
            numero_binario = 'D' + numero_binario
        elif resto == 14:
            numero_binario = 'E' + numero_binario
        elif resto == 15:
            numero_binario = 'F' + numero_binario
        else:
            numero_binario = str(resto) + numero_binario
    else:
        numero_binario = str(resto) + numero_binario   

if base_sistema == 16:
    match resto:
        case 10:
            numero_binario = 'A' + numero_binario
        case 11:
            numero_binario = 'B' + numero_binario
        case 12:
            numero_binario = 'C' + numero_binario
        case 13:
            numero_binario = 'D' + numero_binario
        case 14:
            numero_binario = 'E' + numero_binario
        case 15:
            numero_binario = 'F' + numero_binario
        case _:    
            numero_binario = str(cociente) + numero_binario
else:
    numero_binario = str(cociente) + numero_binario


print(f'{numero_binario}){base_sistema}')