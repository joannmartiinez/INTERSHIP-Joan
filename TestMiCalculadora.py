import unittest
from Calculadora import calcular
class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        num1= 10
        num2= 5
        result = num1 +num2
        self.assertEqual(result, 15)

    def test_subtraction(self):
        num1=10
        num2= 5
        result =num1 -num2
        self.assertEqual(result, 5)
   
    def test_multiplication(self):
        num1=10
        num2= 5
        result =num1 * num2
        self.assertEqual(result, 50)
   
    def test_division(self):
        num1=10
        num2= 5
        result = num1 / num2
        self.assertEqual(result, 2)
    
    def test_elevated(self):
        num1=10
        num2= 2
        result = num1 ** num2
        self.assertEqual(result, 100)
    
    def test_division_cero(self):
        num1=10
        num2= 0
        with self.assertRaises(ZeroDivisionError):
            result = num1 / num2
    
    def test_operacion_invalid(self):
        operation= "%"
        num1, num2 = 5, 3
        self.assertNotIn(operation, ["+","-","*","/","**"])
    if __name__ == "_main__":
        unittest.main()
    