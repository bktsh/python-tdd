import unittest

from lib.calculator.calculator import *

class CalculatorTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("setup_class       class:%s" % self.__name__)

    @classmethod
    def tearDownClass(self):
        print("teardown_class    class:%s" % self.__name__)

    def setUp(self):
        self.calc = Calculator('Cisco')
        print("setup             class:CalculatorTests")

    def tearDown(self):
        print("teardown          class:CalculatorTests")

    def setUpMethod(self, method):
        print("setup_method      method:%s" % method.__name__)

    def tearDownMethod(self, method):
        print("teardown_method   method:%s" % method.__name__)

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
