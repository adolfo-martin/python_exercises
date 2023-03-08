#!/usr/bin/python3

import subprocess

subprocess.run('clear')

marcas = (
    'Seat',
    'Audi',
    'Renault',
    'Nissan',
    'Citroen',
    'Volkswagen',
    'Mercedes',
    'Tesla',
    'Opel',
    'Skoda',
    'Ferrari',
    'Mini',
    'Porsche',
)

marcas_grupo_volkswagen = (
    'Seat',
    'Audi',
    'Volkswagen',
    'Skoda',
    'Porsche',
)

print('Las marcas del grupo Volkswagen son:')

for i in range(0, len(marcas_grupo_volkswagen)):
    print(marcas_grupo_volkswagen[i])

print('Las marcas que no son del grupo Volkswagen son:')

for i in range(0, len(marcas)):
    es_marca_volkswagen = False

    for j in range(0, len(marcas_grupo_volkswagen)):
        if marcas[i] == marcas_grupo_volkswagen[j]:
            es_marca_volkswagen = True
            break

    if not es_marca_volkswagen:
        print(marcas[i])