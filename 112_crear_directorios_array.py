#!/usr/bin/python3

import subprocess
import sys


def main():
    limpiar_pantalla()

    if not son_argumentos_correctos():
        sys.exit(1)

    alumnos = obtener_alumnos()
    try:
        crear_directorios(alumnos)
    except Exception as error:
        print(f'ERROR: {error}')


def son_argumentos_correctos() -> bool:
    argumentos = sys.argv[1:]

    if len(argumentos) != 2:
        print('ERROR: El número de argumentos no es correcto.')
        return False

    try:
        curso = int(argumentos[0])
    except Exception as error:
        print('ERROR: El primer argumento no es un número')
        return False

    return True


def limpiar_pantalla():
    subprocess.run(['clear'])


def obtener_alumnos() -> list[dict]:
    return [
        { 'nre': 45371, 'nombre': 'Marcos', 'apellido': 'España', 'curso': 1, 'grupo': 'daw' },
        { 'nre': 45387, 'nombre': 'Francisco', 'apellido': 'Sánchez', 'curso': 2, 'grupo': 'daw' },
        { 'nre': 45714, 'nombre': 'Alexa', 'apellido': 'Jiménez', 'curso': 1, 'grupo': 'daw' },
    ]


def crear_directorios(alumnos: list[dict]) -> None:

    try:
        resultado = subprocess.run(
            ['mkdir', 'alumnos'],
            capture_output=True,
            text=True
        )
    except Exception as error:
        raise Exception('No se ha podido crear el directorio alumnos')
    
    if resultado.returncode != 0:
        raise Exception(f'(Code {resultado.returncode}) {resultado.stderr}')

    for alumno in alumnos:
        try:
            resultado = subprocess.run(
                args=['mkdir', f'{alumno["nombre"]}.{alumno["apellido"]}' ], 
                cwd='./alumnos',
                capture_output=True,
                text=True,
            )
        except Exception as error:
            raise Exception('No se han podido crear los directorios. Por favor, revise si se ha creado alguno.')

        if resultado.returncode != 0:
            raise Exception(f'(Code {resultado.returncode}) {resultado.stderr}')


if __name__ == '__main__':
    main()