from unittest import TestCase

from lib.collecsions.CollectionNotebook import CollectionNotebook

class TestCollectionNotebookTests(TestCase):

    @classmethod
    def setUpClass(self):
        print("setup_class       class:%s" % self.__name__)

    @classmethod
    def tearDownClass(self):
        print("teardown_class    class:%s" % self.__name__)

    def setUp(self):
        self.subject = CollectionNotebook()
        print("setup             class:CollectionNotebook")

    def tearDown(self):
        print("teardown          class:CollectionNotebook")

    def setUpMethod(self, method):
        print("setup_method      method:%s" % method.__name__)

    def tearDownMethod(self, method):
        print("teardown_method   method:%s" % method.__name__)


    def test_fibSeriesUptoN(self):
        result = self.subject.fibSeriesUptoN(10000)
        print(result)

    def test_fibSeriesUptoN(self):
        result = self.subject.pow4OfList([1,2,3,4,5,6,7,8,9])
        print(result)
