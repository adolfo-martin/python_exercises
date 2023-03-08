#!/usr/bin/python3


def main():
    equipos: list[dict] = obtener_equipos()

    # cantidad = calcular_cantidad_equipos(equipos)
    # print(f'La cantidad de equipos es: {cantidad}')

    # equipo = obtener_detalle_equipo(equipos, 'bet')
    # print(f'El detalle es {equipo}')

    obtener_equipos_jugaran_champions(equipos)

def obtener_equipos() -> list[dict]:
    return [
        { 'id': 'atm', 'nombre': 'Atlético de Madrid', 'victorias': 11, 'empates': 5, 'derrotas': 5, 'goles_favor': 30, 'goles_contra': 17 },
        { 'id': 'bar', 'nombre': 'Barcelona', 'victorias': 18, 'empates': 2, 'derrotas': 1, 'goles_favor': 43, 'goles_contra': 7 },
        { 'id': 'bet', 'nombre': 'Betis', 'victorias': 10, 'empates': 4, 'derrotas': 7, 'goles_favor': 27, 'goles_contra': 22 },
        { 'id': 'rva', 'nombre': 'Rayo Vallecano', 'victorias': 9, 'empates': 6, 'derrotas': 6, 'goles_favor': 28, 'goles_contra': 23 },
        { 'id': 'rma', 'nombre': 'Real Madrid', 'victorias': 14, 'empates': 3, 'derrotas': 3, 'goles_favor': 40, 'goles_contra': 17 },
        { 'id': 'rso', 'nombre': 'Real Sociedad', 'victorias': 13, 'empates': 3, 'derrotas': 5, 'goles_favor': 31, 'goles_contra': 21 },
    ]


def calcular_cantidad_equipos(equipos: list[dict]) -> int:
    return len(equipos)


def obtener_identificadores_equipos(equipos: list[dict]) -> list[str]:
    ...


def obtener_detalle_equipo(equipos: list[dict], id: str) -> dict:
    for equipo in equipos:
        if equipo['id'] == id:            
            detalle = {
                'id': equipo['id'],
                'nombre': equipo['nombre'],
                'partidos_jugados': equipo['victorias'] + equipo['empates'] + equipo['derrotas'],
                'victorias': equipo['victorias'],
                'empates': equipo['empates'],
                'derrotas': equipo['derrotas'],
                'goles_favor': equipo['goles_favor'],
                'goles_contra': equipo['goles_contra'],
                'puntos': equipo['victorias'] * 3 + equipo['empates'],
            }
            break
        
    return detalle
        

def obtener_equipo_primero(equipos: list[dict], ) -> str:
    ...


def obtener_equipo_ultimo(equipos: list[dict], ) -> str:
    ...


def obtener_equipos_jugaran_champions(equipos: list[dict]) -> list[str]:
    puntuaciones_equipos = []
    for equipo in equipos:
        puntos = equipo['victorias'] * 3 + equipo['empates']
        puntuaciones_equipos.append({ 'id': equipo['id'], 'puntos': puntos })

    puntuaciones_ordenadas = sorted(
        puntuaciones_equipos, 
        key = lambda equipo: equipo['puntos'],
        reverse = True
    )
    
    cuatro_primeros = puntuaciones_ordenadas[0:4]
    identificadores = []
    for equipo in cuatro_primeros:
        identificadores.append(equipo['id'])

    return identificadores




def obtener_equipos_descienden_segunda(equipos: list[dict], ) -> list[str]:
    ...

def obtener_equipos_ganan_mas_mitad_puntos_juego(equipos: list[dict], ) -> list[str]:
    ...

if __name__ == '__main__':
    main()