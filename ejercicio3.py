def liderLigaDeFutbol(fixture):
    """Recibe el conjunto de partidos del campeonato.
    Devuelve sólo el líder. En caso de que dos equipos tengan la misma cantidad de puntos devolverá el primero en orden alfabético. """
    tabla = tablaPosiciones(fixture)
    if tabla == {}:
        return ""
    else:
        lider=ordenaTabla(tabla)
        return lider

def ordenaTabla(tablaposiciones):
    """Recibe un diccionario desordenado con los puntajes de cada equipo.
     Genera un listado ordenado y devuelve el líder.  En caso de que dos equipos tengan la misma cantidad de puntos devolverá el primero en orden alfabético"""
    a = tablaposiciones.values()
    b = []
    for x in tablaposiciones.items():
        b.append(x)
    lider = []
    for y in b:
        if y[1] == max(a):
            lider.append(y[0])
    lider.sort()

    return lider[0]

def tablaPosiciones(fixture):
    """Recibe el conjunto de partidos del campeonato.
    Devuelve un diccionario que agrupa los equipos y los puntos obtenidos."""

    tablaposiciones = {}
    if fixture=="":
        return tablaposiciones
    for partido in fixture:
        c= puntosLiga(partido)
        for x in c.items():
            if x[0] in tablaposiciones:
                tablaposiciones[x[0]] = tablaposiciones[x[0]] + x[1]
            else:
                tablaposiciones[x[0]] = x[1]
    return tablaposiciones


def puntosLiga(partido):

    """Recibe una tupla que representa cada partido.
    Devuelve los puntos que recibe cada equipo según el resultado"""
    tablaposiciones = {}
    for x in partido:
        if partido[1]>partido[3]:
            tablaposiciones[partido[0]] = 2
        elif partido[1] < partido[3]:
            tablaposiciones[partido[2]] = 2
        else:
            tablaposiciones[partido[0]] = 1
            tablaposiciones[partido[2]] = 1

    return tablaposiciones