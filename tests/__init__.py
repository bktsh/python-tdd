from tests.calculator.calculator_tests import CalculatorTests
from tests.helloworld.helloworld_tests import HelloworldTests

print(f'Invoking __init__.py for {__name__}')
__all__ = [
        'calculator',
        'helloworld',
        ]

import unittest

def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(CalculatorTests())
    test_suite.addTest(HelloworldTests())
    return test_suite

if __name__ == '__main__':
   suite = create_suite()

   runner=unittest.TextTestRunner()
   runner.run(suite)