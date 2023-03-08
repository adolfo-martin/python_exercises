#!/usr/bin/python3

import subprocess
import sys
import os

FONDO_BLANCO_TEXTO_ROJO = '\033[0;31;47m'
FONDO_AZUL_TEXTO_BLANCO = '\033[0;34;37m'

def main():
    limpiar_pantalla()

    if not es_numero_argumentos_correcto():
        print(f'{FONDO_BLANCO_TEXTO_ROJO}El número de argumentos es erróneo.{FONDO_AZUL_TEXTO_BLANCO}')
    else:
        directorio = obtener_nombre_directorio()
        if not es_un_directorio(directorio):
            print(f'{FONDO_BLANCO_TEXTO_ROJO}El argumento "{directorio}" no es un directorio.{FONDO_AZUL_TEXTO_BLANCO}')
        else:
            print('Es un directorio')
    

def es_un_directorio(fichero, ruta = None) -> bool:
    if ruta:
       if os.path.isdir(os.path.join(ruta, fichero)):
           return True
       else:
           return False
    else:      
       if os.path.isdir(fichero):
           return True
       else:
           return False



def obtener_nombre_directorio() -> str:
    argumentos = sys.argv[1:]
    if len(argumentos):
        return argumentos[0]
    else:
        os.getcwd()


def limpiar_pantalla():
    subprocess.run(['clear'])


def es_numero_argumentos_correcto() -> bool:
    argumentos = sys.argv[1:]
    return True if len(argumentos) <= 1 else False


if __name__ == "__main__":
    main()