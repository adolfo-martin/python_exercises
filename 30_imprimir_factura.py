#!/usr/bin/python3

lineas_factura = [
    {'producto': 'Barra pan normal', 'unidades': 3, 'precio': 0.75, 'impuesto': 'superreducido'},
    {'producto': 'Botella lavavajillas 1l', 'unidades': 1, 'precio': 2.25, 'impuesto': 'normal'},
    {'producto': 'Docena de huevos', 'unidades': 1, 'precio': 1.40, 'impuesto': 'superreducido'},
    {'producto': 'Papel higienico 12 rollos', 'unidades': 1, 'precio': 1.95, 'impuesto': 'normal'},
    {'producto': 'Bandeja pechuga pollo 500g', 'unidades': 2, 'precio': 4.20, 'impuesto': 'reducido'},
    {'producto': 'Bolsa harina 1 kg', 'unidades': 2, 'precio': 1.20, 'impuesto': 'superreducido'},
    {'producto': 'Lubina fileteada', 'unidades': 1, 'precio': 12.95, 'impuesto': 'reducido'},
    {'producto': 'Emperador filete', 'unidades': 2, 'precio': 7.80, 'impuesto': 'reducido'},
    {'producto': 'Detergente ropa botella 1l', 'unidades': 3, 'precio': 4.55, 'impuesto': 'normal'},
    {'producto': 'Trapo cocina', 'unidades': 5, 'precio': 0.65, 'impuesto': 'normal'},
]

impuestos = {
    'superreducido': 0,
    'reducido': 10,
    'normal': 21,
}


def main():
    imprimir_factura(lineas_factura)


def imprimir_factura(lineas):
    print('FACTURA DE COMPRA')
    print('------------------------------------------------')
    imprimir_lineas(lineas)
    imprimir_base_e_impuestos(lineas)


def imprimir_lineas(lineas):
    for linea in lineas:
        print(f"{linea['producto']:<35} {linea['unidades']:<5} {linea['precio']:<8} {round(linea['precio'] * linea['unidades'], 2)}")

def imprimir_base_e_impuestos(lineas):
    print('------------------------------------------------')
    for impuesto in impuestos:
        print(calcular_base_imponible_por_tipo(lineas, impuesto))
        print(calcular_impuestos_por_tipo(lineas, impuesto))


def obtener_tasa(tipo_impuesto):
    return impuestos[tipo_impuesto]


def calcular_base_imponible_por_tipo(lineas, tipo_impuesto):
    base_imponible = 0
    tasa = obtener_tasa(tipo_impuesto)

    for linea in lineas:
        if linea['impuesto'] == tipo_impuesto:
            base_imponible += (linea['precio'] * linea['unidades']) * (1 - (tasa/100))

    return round(base_imponible, 2)

def calcular_impuestos_por_tipo(lineas, tipo_impuesto):
    impuestos = 0
    tasa = obtener_tasa(tipo_impuesto)

    for linea in lineas:
        if linea['impuesto'] == tipo_impuesto:
            impuestos += (linea['precio'] * linea['unidades']) * (tasa/100)

    return round(impuestos, 2)


if __name__ == "__main__":
    main()
