#!/usr/bin/python3 

import math
import sys


ERROR_PROBLEMA_CON_LOS_ARGUMENTOS = 1


def main():
    try:
        radio = obtener_radio()
    except Exception as error:
        print(error)
        sys.exit(ERROR_PROBLEMA_CON_LOS_ARGUMENTOS)

    mostrar_informacion_circulo(radio)


def mostrar_informacion_circulo(radio) -> None:
    print('El diámetro es', round(calcular_diametro(radio), 2), 'cm')
    print('El perímetro es', round(calcular_perimetro(radio), 2), 'cm')
    print('El área es', round(calcular_area(radio), 2), 'cm2')


def obtener_radio() -> float:
    argumentos = sys.argv[1:]

    if len(argumentos) != 1:
        raise Exception('El número de argumentos es erróneo')

    try:
        radio = float(argumentos[0])
    except Exception as error:
        raise Exception('El argumento no es un número')

    return radio


def calcular_diametro(radio: float) -> float:
    diametro: float = 2 * radio
    return diametro


def calcular_perimetro(radio: float) -> float:
    perimetro = 2 * math.pi * radio
    return perimetro


def calcular_area(radio: float) -> float:
    area = math.pi * math.pow(radio, 2)
    return area



if __name__ == "__main__":
    main()