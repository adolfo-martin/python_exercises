#!/usr/bin/python3

import subprocess
import sys

def main():
    limpiar_pantalla()
    try:
        resultado = obtener_uso_memoria_por_usuario_y_proceso()
    except Exception as error:
        print(error)
        sys.exit()

    imprimir_uso_por_pantalla(resultado)


def imprimir_uso_por_pantalla(procesos):
    print('{:20} {:60} {:10}'.format('USUARIO', 'PROCESO', 'MEMORIA'))
    for proceso in procesos:
        print('{:20} {:60} {:10}'.format(proceso[0], proceso[1], proceso[2]))


def obtener_uso_memoria_por_usuario_y_proceso() -> list[list]:
    resultado = subprocess.run(['ps', '-u', '-a', '-x'], text=True, capture_output=True)

    if resultado.returncode != 0:
        raise Exception(f'ERROR: código de error {resultado.returncode}')

    lineas_como_texto = resultado.stdout
    lineas_como_lista = lineas_como_texto.split('\n')

    CAMPO_USUARIO = 0
    CAMPO_MEMORIA = 4
    CAMPO_PROCESO = 10

    resultado = []

    for linea in lineas_como_lista[1:len(lineas_como_lista) - 1]:
        columnas = linea.split()

        if int(columnas[CAMPO_MEMORIA]) == 0:
            continue

        resultado.append([
            columnas[CAMPO_USUARIO], 
            columnas[CAMPO_PROCESO], 
            columnas[CAMPO_MEMORIA]
        ])

    return resultado

    



def limpiar_pantalla():
    subprocess.run(['clear'])


if __name__ == '__main__':
    main()