import unittest
import random
from datetime import datetime
from Simple_calc import Calculator, fun


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(random.randrange(0, 10000, 0.00001))

    def test_add(self):
        print("Begin: ", str(datetime.now().time()), '\n')

        self.calculator.value = random.randrange(0, 10000, 0.00001)
        calc_value = self.calculator.value

        self.assertEqual(self.calculator.add(1000, 200, 300, 12).value, calc_value + 1512)
        self.assertEqual(self.calculator.add(10.0, 2.3, 3.07).value, calc_value + 15.37)
        self.assertEqual(self.calculator.add(0, 1, 0).value, calc_value + 1)
        self.assertEqual(self.calculator.add(-5, -1, 0).value, calc_value - 6)
        self.assertEqual(self.calculator.add(-3.1415926535, -2.718281828).value, calc_value - 5.8598744815)
        self.assertIs(self.calculator.add('test', '$').value, int or float)  # тест не будет пройден
        print("End: ", str(datetime.now().time()), '\n')

    def test_mul(self):
        print("Begin: ", str(datetime.now().time()), '\n')
        self.calculator.value = random.randrange(0, 10000, 0.00001)
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.multiply(5, 2, 90).value, calc_value * 90)
        self.assertEqual(self.calculator.multiply(10.0, 2.3, 3.07).value, calc_value * 85.1)
        self.assertEqual(self.calculator.multiply(-3.1415926535, 0, 10000000000).value, 0)
        self.assertEqual(self.calculator.multiply(-1000, 10000, -100000).value, calc_value * 1e12)
        self.assertIs(self.calculator.multiply('test', '@@@', 'multiply').value, int or float)  # тест не будет пройден
        print("End: ", str(datetime.now().time()), '\n')

    def test_divide(self):
        print("Begin: ", str(datetime.now().time()), '\n')
        self.calculator.value = random.randrange(0, 10000, 0.00001)
        calc_value = self.calculator.value
        self.assertEquals(self.calculator.divide(2, 3).value, calc_value / 6)
        self.assertEquals(self.calculator.divide(2.2, 3.3).value, calc_value / 7.26)
        self.assertEquals(self.calculator.divide(-1).value, calc_value * -1)
        self.assertEquals(self.calculator.divide(0).value, 0)
        print("End: ", str(datetime.now().time()), '\n')

    def test_pow(self):
        print("Begin: ", str(datetime.now().time()), '\n')
        self.calculator.value = random.randrange(0, 10000, 0.00001)
        calc_value = self.calculator.value
        self.assertEquals(self.calculator.pow(2, 3).value, calc_value**6)
        self.assertEquals(self.calculator.pow(0, 3).value, 1)
        self.assertEquals(self.calculator.pow(-4, 3.14).value, calc_value ** -12.56)
        self.assertEquals(self.calculator.pow(0.02, 3.14).value, calc_value ** 0.0628)
        self.calculator.value = 0
        self.assertEquals(self.calculator.pow(0).value, 0)
        print("End: ", str(datetime.now().time()), '\n')

    def test_root(self):
        print("Begin: ", str(datetime.now().time()), '\n')
        self.calculator.value = random.randrange(0, 10000, 0.00001)
        calc_value = self.calculator.value
        self.assertEquals(self.calculator.root(2, 3).value, calc_value**1/6)
        self.assertEquals(self.calculator.root(0, 3).value, 0)
        self.assertEquals(self.calculator.root(-4, 3.14).value, calc_value ** -1/12.56)
        self.assertEquals(self.calculator.root(0).value, 0)
        print("End: ", str(datetime.now().time()), '\n')


if __name__ == '__main__':
    unittest.main()
