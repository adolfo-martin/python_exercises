import os

# if os.name == 'nt':
#     'cls'
# else: 
#     'clear'

# Operador ternario
os.system('cls' if os.name == 'nt' else 'clear')

edad = 20

if edad < 2:
    print('Eres un bebe')
elif edad < 12:
    print('Eres un niño')
elif edad < 18:
    print('Eres un adolescente')
elif edad < 35:
    print('Eres un joven')
elif edad < 65:
    print('Eres un maduro')
else:
    print('Eres un anciano')

print('El programa ha terminado')