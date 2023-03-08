#!/usr/bin/python3

lineas_factura = [
    {'nombre': 'Barra pan normal', 'unidades': 3, 'precio': 0.75, 'impuesto': 'superreducido'},
    {'nombre': 'Botella lavavajillas 1l', 'unidades': 1, 'precio': 2.25, 'impuesto': 'normal'},
    {'nombre': 'Docena de huevos', 'unidades':1, 'precio': 1.40, 'impuesto':'superreducido'},
    {'nombre': 'Papel higienico 12 rollos', 'unidades':1, 'precio':1.95, 'impuesto':'normal'},
    {'nombre': 'Bandeja pechuga pollo 500g', 'unidades':2, 'precio': 4.20, 'impuesto':'reducido'},
    {'nombre': 'Bolsa harina 1kg', 'unidades':2, 'precio': 1.20, 'impuesto': 'superreducido'},
    {'nombre': 'Lubina fileteada', 'unidades':1, 'precio': 12.95, 'impuesto': 'reducido'},
    {'nombre': 'Emeperador filete', 'unidades':2, 'precio': 7.80, 'impuesto': 'reducido'},
    {'nombre': 'Detergente ropa botella 1l', 'unidades': 3, 'precio': 4.55,'impuesto': 'normal'},
    {'nombre': 'Trapo cocina','unidades':5, 'precio':0.65,'impuesto': 'normal'},
    {'nombre': 'Caviar','unidades':1, 'precio': 90,'impuesto': 'lujo'},
    {'nombre': 'Champagne','unidades':2, 'precio': 40,'impuesto': 'lujo'},
]

impuestos = { 
    'superreducido':0, 
    'reducido':10, 
    'normal':21,
    'lujo': 35    
}

def calcular_total_por_tipo_impuesto(tipo_impuesto):
    total_superreducido = 0
    for linea in lineas_factura:
        if linea['impuesto'] ==  tipo_impuesto:
            total_superreducido = total_superreducido + round(linea['unidades'] * linea['precio'],2)
    return total_superreducido




def calcular_impuesto(tipo_impuesto):
    impuesto_reducido = round(calcular_total_por_tipo_impuesto(tipo_impuesto) * impuestos[tipo_impuesto]/100,2)
    return impuesto_reducido

    


def calcular_total():
    total = 0
    for impuesto in impuestos:
        total += calcular_total_por_tipo_impuesto(impuesto)
    return total
    
def mostrar_items():
    print()
    print("FACTURA DE LA COMPRA")
    print('---------------------------------------------------------------')
    for linea in lineas_factura:
        print(f"{linea['nombre']:30} {linea['unidades']:5} {linea['precio']:6} {round(linea['unidades'] * linea['precio'],2):8}")


def mostrar_impuestos():
    print('---------------------------------------------------------------')
    
    print(f"{'':28} {'Base imponible':16}  {'Impuestos':10}")
    for impuesto in impuestos:
        print(f"{'':7} {impuesto:29} {round(calcular_total_por_tipo_impuesto(impuesto) - calcular_impuesto(impuesto), 2):5} {calcular_impuesto(impuesto):8}")

def mostrar_total():
    print('---------------------------------------------------------------')
    print(f"{'TOTAL':48}{calcular_total():0}")
    print()

def main():
    mostrar_items()
    mostrar_impuestos()
    mostrar_total()
    
if __name__ == "__main__":
    main()