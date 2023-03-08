# Primera forma de concatenar
texto1 = 'Hola'
texto2 = 'Pepe'
texto3 = 'Python'

print('Mi mensaje es: ' + texto1 + ' soy ' + texto2 + '. Me gusta ' + texto3)

# Segunda forma de concatenar
lenguaje = 'Python'
calificacion = 10

print(f'Mi mensaje es: {lenguaje} se merece un {calificacion}')

# Tercera forma
print('Mi mensaje es: %s se merece un %d' % (lenguaje, calificacion))

# Cuarta forma
print('Mi mensaje es: {0} se merece un {1}'.format(lenguaje, calificacion))

# Alternativa: con una función
def unir_cadenas_de_texto(cadena1, cadena2):
    return f'{cadena1} {cadena2}'

print(unir_cadenas_de_texto(lenguaje, calificacion))
print(unir_cadenas_de_texto('Adolfo', 'Martín'))
