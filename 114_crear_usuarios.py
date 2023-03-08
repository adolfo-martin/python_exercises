#!/usr/bin/python3

import subprocess
import sys

ERROR_HAY_UN_PROBLEMA_CON_LOS_ARGUMENTOS = 1
ERROR_NO_SE_HAN_PODIDO_CREAR_LOS_USUARIOS = 2

def main():
    limpiar_pantalla()

    # if not son_argumentos_correctos(sys.argv[1:]):
    #     print('ERROR')
    #     sys.exit(ERROR_HAY_UN_PROBLEMA_CON_LOS_ARGUMENTOS)

    try:
        nombres_usuarios = extraer_usuarios()
    except Exception as error:
        print(f'ERROR: {error}')
        sys.exit(ERROR_HAY_UN_PROBLEMA_CON_LOS_ARGUMENTOS)

    return

    try:
        crear_usuarios(nombres_usuarios)
    except Exception as error:
        print(f'ERROR: {error}')
        sys.exit(ERROR_NO_SE_HAN_PODIDO_CREAR_LOS_USUARIOS)



# def son_argumentos_correctos(argumentos) -> bool:
#     if len(argumentos) == 0:
#         return False
#     else:
#         return True


def extraer_usuarios() -> list[str]:  
    argumentos = sys.argv[1:]

    if len(argumentos) < 2:
        # return []
        # return None
        raise Exception('Hay que suministrar al menos un usuario')
    
    try:
        cantidad = int(argumentos[0])
    except Exception as error:
        raise Exception('El primer argumento no es un número')
        
    # if not argumentos[0].isnumeric():
    #     raise Exception('El primer argumento no es un número')
    
    if cantidad != len(argumentos) - 1:
        raise Exception('No coinciden la cantidad y el número de nombres')

def limpiar_pantalla():
    subprocess.run(['clear'])

def crear_usuarios(usuarios: list[str]):
    for usuario in usuarios:
        try:
            crear_directorio(usuario)
            contraseña_encriptada = encriptar_contraseña('Hola1234')
            crear_usuario(usuario, contraseña_encriptada, f'/home/{usuario}')
            cambiar_propietario(usuario, f'/home/{usuario}')
            cambiar_permisos('700', f'/home/{usuario}')
        except Exception as error:
            print (error)

def crear_directorio(directorio):
    resultado = subprocess.run([
        'mkdir', directorio],
        capture_output=True,
        text=True,
        cwd='/home'
    )

    if resultado.returncode != 0:
        raise Exception(f'No se ha podido crear el directorio: [{resultado.returncode}] {resultado.stderr}')
    
    

def encriptar_contraseña(contraseña):
    resultado = subprocess.run([
        'mkpasswd', contraseña],
        capture_output=True,
        text=True,
    )

    if resultado.returncode != 0:
        raise Exception(f'No se ha podido encriptar la contraseña: [{resultado.returncode}] {resultado.stderr}')
    
    return resultado.stdout.strip()


def crear_usuario(usuario, contraseña, directorio):
    resultado = subprocess.run(
        ['useradd', '-p', contraseña, '-d', directorio,  usuario],
        capture_output=True,
        text=True,
    )

    if resultado.returncode != 0:
        raise Exception(f'No se ha podido crear el usuario: [{resultado.returncode}] {resultado.stderr}')
    

def cambiar_propietario(usuario, directorio):
    resultado = subprocess.run(
        ['chown', usuario, directorio],
        capture_output=True,
        text=True,
    )

    if resultado.returncode != 0:
        raise Exception(f'No se ha podido cambiar el propietario del directorio {directorio} a {usuario}: [{resultado.returncode}] {resultado.stderr}')
    


def cambiar_permisos(permisos, directorio):
    resultado = subprocess.run(
        ['chmod', permisos, directorio],
        capture_output=True,
        text=True,
    )

    if resultado.returncode != 0:
        raise Exception(f'No se han podido cambiar los permisos: [{resultado.returncode}] {resultado.stderr}')



if __name__ == '__main__':
    main()