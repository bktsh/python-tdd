import unittest
from lib.helloworld.helloworld import *

class HelloworldTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("setup_class       class:%s" % self.__name__)

    @classmethod
    def tearDownClass(self):
        print("teardown_class    class:%s" % self.__name__)

    def setUpModule(module):
        print("setup_module      module:%s" % module.__name__)

    def tearDownModule(module):
        print("teardown_module   module:%s" % module.__name__)

    def setUp(self):
        print("setup             class:HelloworldTests")

    def tearDown(self):
        print("teardown          class:HelloworldTests")


    def setup_method(self, method):
        print("setup_method      method:%s" % method.__name__)

    def teardown_method(self, method):
        print("teardown_method   method:%s" % method.__name__)

    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')

    def test_custom_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)

    def test_custom_func_x(self):
        self.assertEqual(custom_func_x(3,2,3), 54)
        print(custom_func_x(3,2,3))

    def test_custom_non_lin_num_list(self):
        self.assertEqual(custom_non_lin_num_list(5, 2, 3)[2], 16)
        print(custom_non_lin_num_list(5, 2, 3))
        self.assertEqual(custom_non_lin_num_list(5, 3, 2)[4], 48)
        print(custom_non_lin_num_list(5, 2, 3))

    if __name__ == '__main__':
        unittest.main()