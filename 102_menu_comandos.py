#!/usr/bin/python3

import subprocess
import sys

#---------------------------------------------------------
def main():
    limpiar_pantalla()
    mostrar_menu()
    pedir_opcion()

#---------------------------------------------------------
def limpiar_pantalla():
    subprocess.run(['clear'])

#---------------------------------------------------------
def mostrar_menu():
    print('\n-----------MENÚ-----------')
    print('\t1) Mostrar fecha.')
    print('\t2) Mostrar quién soy.')
    print('\t3) Mostrar quién está conectado.')
    print('\t4) Mostrar el calendario.')
    print('\t5) Cambiar la contraseña.')
    print('\t6) Cerrar la aplicación.')

#---------------------------------------------------------
def pedir_opcion():
    while True:
        respuesta = input('\nSeleccione una opción del menú: ')

        if respuesta != "1" \
                and respuesta != "2" \
                and respuesta != "3" \
                and respuesta != "4" \
                and respuesta != "5" \
                and respuesta != "6":
            print('Debe introducir un número entre 1 y 6.')
            continue

        respuesta = int(respuesta)

        if respuesta == 1:
            mostrar_fecha()
        elif respuesta == 2:
            mostrar_quien_soy() 
        elif respuesta == 3:
            mostrar_usuarios_conectados()
        elif respuesta == 4:
            mostrar_calendario()
        elif respuesta == 5:
            cambiar_contraseña()
        elif respuesta == 6:
            cerrar_aplicacion()

#---------------------------------------------------------
def mostrar_fecha():
    subprocess.run(['date'])

#---------------------------------------------------------
def mostrar_quien_soy():
    subprocess.run(['whoami'])

#---------------------------------------------------------
def mostrar_usuarios_conectados():
    subprocess.run(["who"])

#---------------------------------------------------------
def mostrar_calendario():
    subprocess.run(["cal"])

#---------------------------------------------------------
def cambiar_contraseña():
    subprocess.run(["passwd"])

#---------------------------------------------------------
def cerrar_aplicacion():
    sys.exit(0)

#---------------------------------------------------------
if __name__ == "__main__":
    main()