#!/usr/bin/python3

import sys
import subprocess

def main():
    if not son_argumentos_correctos():
        sys.exit()
    
    mes, año = obtener_argumentos()

    mostrar_calendario(mes, año)


def mostrar_calendario(mes: str, año: int) -> None:
    mes = mes.lower()

    meses = ( 'enero', 'febrero',  'marzo', 'abril', 'mayo', 'junio', \
        'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre' )
    mes_en_numero = meses.index(mes) + 1

    subprocess.run(['cal', str(mes_en_numero), str(año)])


def obtener_argumentos():
    argumentos = sys.argv[1:]
    mes = argumentos[0]
    año = int(argumentos[1])

    return mes, año




def son_argumentos_correctos() -> bool:
    argumentos = sys.argv[1:]

    if len(argumentos) != 2:
        print('Error: no has introducido dos argumentos. Debes de poner el mes y el año.')
        return False

    mes = argumentos[0]
    año = argumentos[1]

    if not es_mes(mes):
        print('ERROR: No has introducido el nombre de un mes como primer argumento.')
        return False
    
    if not año.isnumeric():
        print('ERROR: el segundo argumento debe ser un número entero porque es el año.')
        return False

    return True


def es_mes(mes) -> bool:
    mes = mes.lower()

    meses = ( 'enero', 'febrero',  'marzo', 'abril', 'mayo', 'junio', \
        'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre' )

    if mes in meses:
        return True
    else:
        return False

    # if mes != 'enero' \
    #     and mes != 'febrero' \
    #     and mes != 'marzo' \
    #     and mes != 'abril' \
    #     and mes != 'mayo' \
    #     and mes != 'junio' \
    #     and mes != 'julio' \
    #     and mes != 'agosto' \
    #     and mes != 'septiembre' \
    #     and mes != 'octubre' \
    #     and mes != 'noviembre' \
    #     and mes != 'diciembre':
    #     return False
    # else:
    #     return True




if __name__ == "__main__":
    main()