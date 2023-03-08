import os

os.system('cls')

# numero = 1000

# while numero >= 1000 and numero <= 2000:
for numero in range(1000, 2000):
    if numero % 3 == 0:
        print(numero, end=',')

    # numero += 1