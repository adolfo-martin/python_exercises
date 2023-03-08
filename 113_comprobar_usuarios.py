#!/usr/bin/python3

import subprocess
import sys


def main():
    limpiar_pantalla()

    argumentos = recuperar_argumentos()
    usuarios_del_sistema = extraer_usuarios_del_sistema()
    informar_si_los_usuarios_pertenecen_al_sistema(argumentos, usuarios_del_sistema)


def informar_si_los_usuarios_pertenecen_al_sistema(usuarios, usuarios_del_sistema):
    for usuario in usuarios:
        if usuario in usuarios_del_sistema:
            print(f'El usuario {usuario} existe en el sistema')
        else:
            print(f'El usuario {usuario} no existe en el sistema')


def extraer_usuarios_del_sistema() -> list[str]:
    resultado = subprocess.run(
        ['cat', '/etc/passwd'], 
        capture_output=True, 
        text=True
    )

    if resultado.returncode != 0:
        print('ERROR')
        sys.exit(2)

    lineas = resultado.stdout.split('\n')

    usuarios = []
    for linea in lineas:
        usuario = linea.split(':')[0]
        usuarios.append(usuario)

    return usuarios[0:len(usuarios) - 1]


def recuperar_argumentos():
    argumentos = sys.argv[1:]

    if len(argumentos) == 0:
        print('ERROR')
        sys.exit(100)
    else:
        return argumentos


def limpiar_pantalla():
    subprocess.run(['clear'])


if __name__ == '__main__':
    main()