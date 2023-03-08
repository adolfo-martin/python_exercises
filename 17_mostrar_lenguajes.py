#!/usr/bin/python3

lenguajes = ('Java', 'SQL', 'Python', 'HTML', 'CSS', 'JavaScript', 'PHP', 'NodeJS', 'Angular')

print('Los lenguajes que vamos a aprender durante estos dos cursos son: ')

for i in range(0, len(lenguajes)):
    print(f'\t{i+1}) {lenguajes[i]}')