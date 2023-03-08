#!/usr/bin/python3

import subprocess
import sys


EXITO = 0
ERROR_NUMERO_ARGUMENTOS_INCORRECTO = 1
ERROR_LA_DIRECCION_NO_ES_CORRECTA = 2
ERROR_NO_HAY_COMUNICACION_CON_EL_DESTINO = 3


def main():
    limpiar_pantalla()

    direccion = recuperar_direccion()
    if direccion is None:
        print('Hay un problema con el número de argumentos.')
        sys.exit(ERROR_NUMERO_ARGUMENTOS_INCORRECTO)
    
    if not es_direccion_correcta(direccion):
        print('El argumento no es una dirección IP correcta')
        sys.exit(ERROR_LA_DIRECCION_NO_ES_CORRECTA)

    if hay_comunicacion(direccion):
        print(f'Hay comunicación con el destino {direccion}')
        sys.exit(EXITO)
    else:
        print(f'No hay comunicación con el destino {direccion}')
        sys.exit(ERROR_NO_HAY_COMUNICACION_CON_EL_DESTINO)


def recuperar_direccion() -> str | None:
    argumentos = sys.argv[1:]
    if len(argumentos) == 1:
        return argumentos[0]
    else:
        return None


def es_direccion_correcta(direccion: str) -> bool:
    numeros = direccion.split('.')    
    if len(numeros) != 4:
        return False

    for i in range(0, len(numeros)):
        if not numeros[i].isnumeric():
            return False
        
        numero = int(numeros[i])
        if numero < 0 or numero > 255:
            return False

    return True


def hay_comunicacion(direccion: str) -> bool:
    result = subprocess.run(['ping', '-c', '1', direccion], text=True, capture_output=True)

    return True if result.returncode == 0 else False


def limpiar_pantalla():
    subprocess.run(['clear'])


if __name__ == "__main__":
    main()