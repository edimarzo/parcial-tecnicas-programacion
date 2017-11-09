import ejercicio1
import unittest
class PruebaTest(unittest.TestCase):
    def testVacioDevuelveListaVacia(self):
        n = ""
        resultado=ejercicio1.rotaPalabra(n)
        self.assertEqual(resultado,[])
    def testIngresaCadenaDeCaracteresCompuestaPorEspacios(self):
        n="     "
        resultado = ejercicio1.rotaPalabra(n)
        self.assertEqual(resultado, [])

    def testIngresaCadenaDeUnCaracter(self):
        n = "a"
        resultado = ejercicio1.rotaPalabra(n)
        self.assertEqual(resultado, ['a'])

    def testIngresaCadenaDeDosCaracteres(self):
        n = "ab"
        resultado = ejercicio1.rotaPalabra(n)
        self.assertEqual(resultado, ['ab','ba'])

    def testIngresaCadenaDeTresCaracteres(self):
        n = "paz"
        resultado = ejercicio1.rotaPalabra(n)
        self.assertEqual(resultado, ['paz','azp','zpa'])

    def testIngresaCadenaDeCuatroCaracteres(self):
        n = "so l"
        resultado = ejercicio1.rotaPalabra(n)
        self.assertEqual(resultado, ['so l','o ls',' lso','lso '])

    def testIngresaCadenaDeCincoCaracteres(self):
        n = "rotar"
        resultado = ejercicio1.rotaPalabra(n)
        self.assertEqual(resultado, ['rotar','otarr','tarro','arrot','rrota'])

        """assert (rotaPalabra("") == [])
        assert (rotaPalabra("     ") == [])
assert (rotaPalabra("a") == ['a'])
assert (rotaPalabra("ab") == ['ab','ba'])
assert (rotaPalabra("paz") == ['paz','azp','zpa'])
assert (rotaPalabra("so l") == ['so l','o ls',' lso','lso '])
assert (rotaPalabra("rotar") == ['rotar','otarr','tarro','arrot','rrota'])"""