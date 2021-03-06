import ejercicio2
import unittest

class Ejercicio2Test(unittest.TestCase):

    def testIngresaListaVaciaDevuelveListaVacia(self):
        n = []
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        resultado = ejercicio2.batallaDeBotes(n,posicionesDeDisparosDePrueba)
        self.assertEqual(resultado,[])

    def testIngresaVacioDevuelveListaVacia(self):
        n = ""
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        resultado = ejercicio2.batallaDeBotes(n,posicionesDeDisparosDePrueba)
        self.assertEqual(resultado,[])

    def testIngresaCadenaDeCaracteresCompuestaPorEspacioDevuelveListaVacia(self):
        n = "      "
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        resultado = ejercicio2.batallaDeBotes(n,posicionesDeDisparosDePrueba)
        self.assertEqual(resultado,[])

    def testIngresaCadenaDeCaracteresInvalidosDevuelveListaVacia(self):
        n = ["soy NO valido"]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        resultado = ejercicio2.batallaDeBotes(n,posicionesDeDisparosDePrueba)
        self.assertEqual(resultado,[])

    def testIngresaListaDeCadenaDeCaracteresInvalidosDevuelveListaVacia(self):
        n = ["yo","tambien","soy","invalido"]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        resultado = ejercicio2.batallaDeBotes(n,posicionesDeDisparosDePrueba)
        self.assertEqual(resultado,[])

    def testIngresaListaDeCadenaDeCaracteresConDistintoLargoDevuelveListaVacia(self):
        n = ["b.b.","....","..bb","b.b"]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        resultado = ejercicio2.batallaDeBotes(n,posicionesDeDisparosDePrueba)
        self.assertEqual(resultado,[])
    def testIngresaListaDeCadenaDeCaracteresCorrectaDevuelveRespuestaCorrecta(self):
        n = ["b.b..","b...b",".....","....b"]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]
        resultado = ejercicio2.batallaDeBotes(n,posicionesDeDisparosDePrueba)
        self.assertEqual(resultado,[(2,1),(2,5)])

    def testIngresaListaDeCadenaDeCaracteresCorrectaSinPosicionesDeDisparosDevuelveRespuestaCorrecta(self):
        n = ["b..","...","..b"]
        posicionesDeDisparosDePrueba = []
        resultado = ejercicio2.batallaDeBotes(n, posicionesDeDisparosDePrueba)
        self.assertEqual(resultado, [(1,1),(3,3)])

