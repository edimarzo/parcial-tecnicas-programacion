def mapaCheck(mapa):
    """Recibe una lista de listas (mapa) y evalua si cumple con las condiciones del juego.
    Devuelve el mapa verificado y en caso de error devuelve una lista vacía."""

    if largoCheck(mapa)=="error":
        return "error"
    if caracteresCheck(mapa)=="error":
        return "error"
    return mapa

def largoCheck(mapa):
    """Recibe el mapa y verifica si cada una de las listas cuenta con la misma cantidad de caracteres.
    Devuelve el mapa verificado."""

    if mapa == "" or mapa == []:
        return "error"
    a = len(mapa[0])
    for x in mapa:
        if len(x) != a:
            return "error"
        else:
            continue
    return mapa

def caracteresCheck(mapa):
    """Recibe el mapa y verifica que los caracteres sean sólo "b" y "."
    Devuelve el mapa verificado o el mensaje error en caso de no cumplirse las condicionnes."""
    for x in mapa:
        for y in x:
            if y =="b" or y==".":
                continue
            else:
                return "error"
    return mapa

def coordenadasMapa(mapa):
    """Recibe el mapa y genera un listado de "coordenadas" donde se ubican los barcos."""
    cuentax=0
    listacoordenadas = []
    for x in mapa:
        cuentax = cuentax + 1
        cuentay=0
        for y in x:
            cuentay = cuentay + 1
            if y =="b":
                cord=(cuentax,cuentay)
                listacoordenadas.append(cord)
    return listacoordenadas

def batallaDeBotes(mapa,tiros):
    """Recibe el mapa y las "coordenadas" que representan los disparos.
    Devuelve las coordenadas de los barcos que no fueron hundidos."""
    mapavacio = []
    if mapaCheck(mapa)=="error":
        return mapavacio
    lista = coordenadasMapa(mapa)
    for x in tiros:
        for y in lista:
            if x == y:
                lista.remove(y)
            else:
                continue
    return lista