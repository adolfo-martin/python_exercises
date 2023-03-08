puntuaciones = (0.75, 0.75, 1, 1, 1.25, 1.5, 2, 1.75)

notas = []
for i in range(1, 9):
    nota = int(input(f'Dame la nota de la pregunta {i}: '))
    notas.append(nota)

calificacion = 0
for i in range(0, len(puntuaciones)):
    calificacion = calificacion + (puntuaciones[i] * notas[i]) / 100

print(f'La calificación de tu examen es {calificacion}')