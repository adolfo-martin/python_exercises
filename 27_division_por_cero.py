
def dividir(dividendo, divisor):
    if divisor == 0:
        raise Exception('División por cero')
    
    cociente = dividendo / divisor
    return cociente


try:
    print(dividir(7, 7))
    print(dividir(7, 0))
except Exception as error:
    print(f'ERROR: {error}')