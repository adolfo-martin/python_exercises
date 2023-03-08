#!/usr/bin/python3
import subprocess

subprocess.run('clear')

# lenguajes = ['Java', 'Python', 'SQL', 'HTML', 'CSS', 'JavaScript', 'NodeJS', 'TypeScript']
lenguajes = {
    'ja': 'Java', 
    'py': 'Python', 
    'sq': 'SQL', 
    'ht': 'HTML', 
    'cs': 'CSS', 
    'js': 'JavaScript', 
    'no': 'NodeJS', 
    'ts': 'TypeScript'
}

lenguajes['ph'] = 'PHP'
lenguajes['ba'] = 'bash/shell'

for i in lenguajes:
    print(f'El lenguaje con clave {i} es {lenguajes[i]}')

print()