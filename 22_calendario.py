import subprocess

subprocess.run('clear')

dias_semana = (
    'Lunes    ',
    'Martes   ',
    'Miércoles',
    'Jueves   ',
    'Viernes  ',
    'Sábado   ',
    'Domingo  ',
)

print('       ', end='')
for i in range(0, len(dias_semana)):
    print(dias_semana[i], end="  ")
print()

for numero in range(1, 32):
    print('{:11}'.format(numero), end='')

    if numero % 7 == 0:
        print()

print('\n\n')