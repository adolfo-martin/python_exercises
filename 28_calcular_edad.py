
ANHO_ACTUAL: int = 2023


def calcular_edad(anho_nacimiento: int) -> int:
    edad = ANHO_ACTUAL - anho_nacimiento

    if edad > 130:
        raise Exception(f'La edad es improbable: {edad}')
    elif edad < 0:
        raise Exception(f'La edad es imposible: {edad}')

    return edad
    

