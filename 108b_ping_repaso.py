#!/usr/bin/python3

import subprocess
import sys


ERROR_NUMERO_ARGUMENTOS_ERRONEO = 1
ERROR_DIRECCION_NO_VALIDA = 2


def main():
    limpiar_pantalla()
    direccion = obtener_direccion()
    testear_conexion(direccion)


def testear_conexion(direccion: str) -> None: 
    resultado = subprocess.run(
        ['ping', '-c', '1', direccion],
        text=True,
        capture_output=True
    )

    if resultado.returncode != 0:
        print(f'No se ha podido establecer comunicación con la dirección {direccion}')
    else:
        print(f'Hay comunicación con la dirección {direccion}')


def obtener_direccion() -> str:
    argumentos = sys.argv[1:]
    if len(argumentos) > 1:
        print('ERROR: Solo puedes poner cero o un argumentos.')
        sys.exit(ERROR_NUMERO_ARGUMENTOS_ERRONEO)    

    if len(argumentos) == 0:
        direccion = pedir_direccion_por_teclado()
    else:
        direccion = extraer_direccion(argumentos)

    if not es_direccion_correcta(direccion):
        print('ERROR: El elemento introducido no es una dirección.')
        sys.exit(ERROR_DIRECCION_NO_VALIDA)

    return direccion

    
def es_direccion_correcta(direccion: str) -> bool:
    numeros = direccion.split('.')

    if len(numeros) != 4:
        return False

    for numero in numeros:
        if not numero.isnumeric():
            return False

        numero = int(numero)
        if numero < 0 or numero > 255:
            return False

    return True


def pedir_direccion_por_teclado() -> str:
    direccion = input('Dime la dirección con la que quieres comunicarte: ')
    return direccion


def extraer_direccion(argumentos: list[str]) -> str:
    return argumentos[0]


def limpiar_pantalla():
    subprocess.run(['clear'])


if __name__ == "__main__":
    main()