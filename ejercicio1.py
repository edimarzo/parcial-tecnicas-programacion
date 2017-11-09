def rotaPalabra(a):
    """Recibe una cadena de caracteres.
    Devuelve una lista con todas las rotaciones de las palabras."""
    lista=[]
    if chequeoPalabra(a) == lista:
        return lista
    elif len(a) == 1:
        lista.append(a)
        return lista
    else:
        lista = [a, ]
        for letra in a:
            a = a[1:len(a)] + a[0]
            lista.append(a)
        return lista[:len(a)]

def chequeoPalabra(a):
    """Recibe una cadena de caracteres y revisa si es una lista vacía o si todos los caracteres no sean espacios en blanco.
    Devuelve la cadena analizada o una cadena vacía en caso que todos los caracteres fueran espacios o una lista vacía."""
    lista = []
    contador = 0
    if a == "":
        return lista
    for x in a:
        if x == " ":
            contador = contador+1
    if contador == len(a):
        return lista
    else:
        return a