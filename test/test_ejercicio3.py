import ejercicio3
import unittest

class Ejercicio3Test(unittest.TestCase):

    def testIngresaListadePartidosVaciaDevuelveVacio(self):
        n = []
        resultado = ejercicio3.liderLigaDeFutbol(n)
        self.assertEqual(resultado,"")

    def testIngresaListaDeUnPartidoDevuelveGanadorDelPartido(self):
        n = [("a", 1, "b", 0)]
        resultado = ejercicio3.liderLigaDeFutbol(n)
        self.assertEqual(resultado,"a")

    def testIngresaListaDeTresPartidosDevuelveGanadorDelCampeonato(self):
        n = [("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]
        resultado = ejercicio3.liderLigaDeFutbol(n)
        self.assertEqual(resultado,"c")

    def testIngresaListaDePartidosDevuelveGanadorDelCampeonatoOrdenadoAlfabeticamente(self):
        n = [("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]
        resultado = ejercicio3.liderLigaDeFutbol(n)
        self.assertEqual(resultado,"Almagro")

    def testIngresaListaDePartidosDevuelveGanadorDelCampeonatoOrdenadoAlfabeticamente(self):
        n = [("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]
        resultado = ejercicio3.liderLigaDeFutbol(n)
        self.assertEqual(resultado,"a")



