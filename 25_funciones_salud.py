def main():
    peso = pedir_peso_en_kilogramos()
    altura = pedir_altura_en_centimetros()
    masa_corporal = calcular_masa_corporal(peso, altura)
    informar_usuario(masa_corporal)

#----------------------------------------------
def pedir_peso_en_kilogramos():
    peso = float(input('Dime tu peso en kilogramos: '))    
    return peso

#----------------------------------------------
def pedir_altura_en_centimetros():
    altura = int(input('Dime tu altura en centimetros: '))
    return altura

#----------------------------------------------
def calcular_masa_corporal(peso_kg, altura_cm):
    masa_corporal = round(peso_kg / (altura_cm / 100)**2, 1)
    return masa_corporal

#----------------------------------------------
def es_peso_inferior_al_normal(masa_corporal):
    if masa_corporal < 18.5:
        return True
    else: 
        return False

#----------------------------------------------
def es_peso_normal(masa_corporal):
    if masa_corporal >= 18.5 and masa_corporal <= 24.9:
        return True
    else: 
        return False

#----------------------------------------------
def es_peso_superior_al_normal(masa_corporal):
    if masa_corporal >= 25.0 and masa_corporal <= 29.9:
        return True
    else: 
        return False

#----------------------------------------------
def es_peso_obeso(masa_corporal):
    if masa_corporal >= 30.0:
        return True
    else: 
        return False

def informar_usuario(masa_corporal):
    if es_peso_inferior_al_normal(masa_corporal):
        print('Tu peso es inferior a lo normal. Debes de comer más.')
    elif es_peso_normal(masa_corporal):
        print('Tu peso es el idóneo para tu estatura.')
    elif es_peso_superior_al_normal(masa_corporal):
        print('Tu peso es superior a lo normal. Debes comer un poco menos.')
    elif es_peso_obeso(masa_corporal): 
        print('Tienes sobrepeso. Debes hacer dieta y ejercicio.')

#----------------------------------------------
if __name__ == "__main__":
    main()