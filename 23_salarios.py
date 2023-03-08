empleados = [
    { 'nombre': 'Lucas', 'salario': 35000 },
    { 'nombre': 'Alexa', 'salario': 42000 },
    { 'nombre': 'Sebastián', 'salario': 37000 },
    { 'nombre': 'Gisela', 'salario': 29000 },
    { 'nombre': 'Raul', 'salario': 28000 },
    { 'nombre': 'Adrián', 'salario': 31000 },
    { 'nombre': 'Sara', 'salario': 35000 },
    { 'nombre': 'Fernando', 'salario': 40000 },
]

empleados.append({ 'nombre': 'Miguel', 'salario': 35000 })


# persona['nombre']
# persona['salario']

# Persona con mayor salario
posicion_maximo = -1
salario_maximo = -1

for i in range(0, len(empleados)):
    if empleados[i]['salario'] > salario_maximo:
        posicion_maximo = i
        salario_maximo = empleados[i]['salario']

mensaje = f""" 
    La persona de mayor salario es {empleados[posicion_maximo]['nombre']}.
    Su salario es {empleados[posicion_maximo]['salario']}.
"""
print(mensaje)

# Masa salarial (suma de todos los salarios)

# Diferencia entre el mayor y el menor salario

# Mostrar todos los salarios netos
retenciones = [
    { 'desde': 10000, 'hasta': 19999, 'porcentaje': 10 },
    { 'desde': 20000, 'hasta': 29999, 'porcentaje': 15 },
    { 'desde': 30000, 'hasta': 39999, 'porcentaje': 20 },
    { 'desde': 40000, 'hasta': 49999, 'porcentaje': 25 },
    { 'desde': 50000, 'hasta': 59999, 'porcentaje': 30 },
]

for i in range(0, len(empleados)):
    for j in range(0, len(retenciones)):
        if empleados[i]['salario'] >= retenciones[j]['desde'] and empleados[i]['salario'] <= retenciones[j]['hasta']:
            salario_bruto = empleados[i]['salario']
            retencion = retenciones[j]['porcentaje']
            salario_neto = salario_bruto - (salario_bruto * retencion) / 100
            print(empleados[i]['salario'], salario_neto)
            break

