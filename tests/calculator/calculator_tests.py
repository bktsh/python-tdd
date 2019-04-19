from lib.calculator.calculator import *
from tests.my_base_test_case import BaseTestCase


class CalculatorTests(BaseTestCase):

    def setUp(self):
        self.calc = Calculator('Cisco')
        print("setup             class:CalculatorTests")

    def tearDown(self):
        print("teardown          class:CalculatorTests")

    def test_add_ouside(self):
        self.assertEqual(add_outside(2, 40), 42)

    def test_add(self):
        self.assertEqual(self.calc.add(2, 40), 42)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 40), 80)

    def test_divide(self):
        self.assertEqual(self.calc.divide(200, 40), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 40), -38)
