#!/usr/bin/python3

import subprocess

subprocess.run('clear')

equipos = {
    'alm': 'Almería',
    'abi': 'Athletic de Bilbao',
    'ama': 'Atlético de Madrid',
    'bar': 'Fútbol Club Barcelona',
    'bet': 'Real Betis Balompié',
    'cad': 'Cádiz',
    'cvi': 'Celta de Vigo',
    'elc': 'Elche',
    'esp': 'Espanyol',
    'get': 'Getafe',
}

equipos['gir'] = 'Girona'
equipos['mal'] = 'Mallorca'
equipos['osa'] = 'Osasuna'
equipos['rso'] = 'Real Sociedad'
equipos['ray'] = 'Rayo Vallecano'
equipos['rma'] = 'Real Madrid'
equipos['rva'] = 'Real Valladolid'
equipos['sev'] = 'Sevilla'
equipos['val'] = 'Valencia'
equipos['vil'] = 'Villarreal'

print(f'Los {len(equipos)} equipos de la liga española son:')

contador = 0
for i in equipos:
    contador += 1
    if contador < 10:
        print(f'\t {contador}) {equipos[i]}')
    else:
        print(f'\t{contador}) {equipos[i]}')