#!/usr/bin/python3

import subprocess
from CodigoIban import CodigoIban


def main():
    limpiar_pantalla()
    try:
        # codigo = CodigoIban('ES00')
        codigo = CodigoIban('ES0056789012345678901234')
    except Exception as error:
        print(f'ERROR: {error}')


def limpiar_pantalla():
    subprocess.run(['clear'])


if __name__ == '__main__':
    main()