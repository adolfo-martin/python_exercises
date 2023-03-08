#!/usr/bin/python3 

import subprocess

def main():
    limpiar_pantalla()
    valor_path = extraer_valor_linea_path()
    enumerar_directorios_path(valor_path)


def enumerar_directorios_path(path):
    directorios = path.split(':')

    print('Los directorios incluidos en el PATH son:')
    for i, directorio in enumerate(directorios):
        print(f'\t{i+1}) {directorio}')


def extraer_valor_linea_path():
    resultado = subprocess.run(
        ['env', '|', 'grep', 'PATH'],
        capture_output=True,
        text=True
    )

    if resultado.returncode != 0:
        print('No se han podido recuperar las variables de entorno')
        print(resultado.stderr)
    else:
        linea = resultado.stdout
        linea_como_lista = linea.split('=')
        if linea_como_lista[0] == "PATH":
            return linea_como_lista[1]
            

def limpiar_pantalla():
    subprocess.run(['clear'])

if __name__ == "__main__":
    main()
