#!/usr/bin/python3

import math


def main():
    radio = pedir_radio()

    diametro = calcular_diametro(radio)
    print('Diámetro:', diametro)

    print('Perímetro:', calcular_perimetro(radio))

    print('Área:', round(calcular_area(radio), 2))


def pedir_radio():
    radio = int(input('Dime el radio del círculo: '))
    return radio


def calcular_diametro(radio):
    diametro = 2 * radio
    return diametro


def calcular_perimetro(radio):
    perimetro = 2 * math.pi * radio
    return perimetro


def calcular_area(radio):
    return math.pi * radio**2


if __name__ == "__main__":
    main()