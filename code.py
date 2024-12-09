# Implementação da calculadora
class Calculadora:
    def adicionar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b

    def exponenciar(self, a, b):
        return a ** b

# Testes de unidade
import unittest

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_adicionar(self):
        self.assertEqual(self.calc.adicionar(2, 3), 5)
        self.assertEqual(self.calc.adicionar(-1, 1), 0)
        self.assertEqual(self.calc.adicionar(0, 0), 0)

    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(10, 5), 5)
        self.assertEqual(self.calc.subtrair(0, 5), -5)
        self.assertEqual(self.calc.subtrair(-5, -5), 0)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 4), 12)
        self.assertEqual(self.calc.multiplicar(-2, 3), -6)
        self.assertEqual(self.calc.multiplicar(0, 5), 0)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertEqual(self.calc.dividir(-10, 2), -5)
        self.assertRaises(ValueError, self.calc.dividir, 10, 0)

    def test_exponenciar(self):
        self.assertEqual(self.calc.exponenciar(2, 3), 8)
        self.assertEqual(self.calc.exponenciar(5, 0), 1)
        self.assertEqual(self.calc.exponenciar(3, -2), 1/9)

if __name__ == "__main__":
    unittest.main()
