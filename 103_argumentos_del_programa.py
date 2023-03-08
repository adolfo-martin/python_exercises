#!/usr/bin/python3

import sys
import subprocess

def main():
    limpiar_pantalla()
    mostrar_argumentos()


def limpiar_pantalla() -> None:
    subprocess.run(['clear'])


def mostrar_argumentos() -> None:
    nombre: str = sys.argv[0]
    argumentos: list[str] = sys.argv[1:]

    print('Nombre del script:', nombre)
    
    # print('Argumentos:', argumentos)
    if len(argumentos) == 0:
        print('El script no ha recibido argumentos.')
        return

    print('Los argumentos del script son:')
    for i in range(0, len(argumentos)):
        posicion = i + 1
        if posicion == 1 or posicion == 3:
            print(f'\t{posicion}\u1d49\u02b3 argumento) {argumentos[i]}')
        else:
            print(f'\t{posicion}\u1d52 argumento) {argumentos[i]}')


if __name__ == "__main__":
    main()
