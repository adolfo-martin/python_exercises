lenguajes: list[str] = ['Java', 'PHP', 'C#', 'JavaScript', 'CSS', 'Ruby on Rails', 'TypeScript']

# print(lenguajes)

# try:
#     lenguajes.remove('Sass')
# except Exception as error:
#     print(f'\nNo se puede eliminar el elemento: \n\t{error}\n')

# print(lenguajes)

# inserta un elemento si no existe en la lista
def insertar(lista: list[str], elemento: str) -> int:
    try:
        posicion = lista.index(elemento)
    except Exception as error:
        lista.append(elemento)
        return
        
    raise Exception(f'No puedo añadir {elemento} porque ya está en la lista')



# print(f'El elemento {elemento} ha sido añadido al final de la lista')
# print(f'No puedo añadir {elemento} porque ya está en la lista')

insertar(lenguajes, 'NodeJS')
insertar(lenguajes, 'CSS')
