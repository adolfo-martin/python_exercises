class CodigoIban:
    def __init__(self, codigo_iban: str):
        self.comprobar_codigo_iban(codigo_iban)

    def comprobar_codigo_iban(self, codigo_iban: str):
        if len(codigo_iban) != 24:
            raise Exception('La longitud del código IBAN no es correcta')