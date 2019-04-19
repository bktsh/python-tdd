from unittest import TestCase


class BaseTestCase(TestCase):
    
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

    def setup_method(self, method):
        print("setup_method      method:%s" % method.__name__)

    def teardown_method(self, method):
        print("teardown_method   method:%s" % method.__name__)

