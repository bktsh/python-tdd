from lib.collecsions.CollectionNotebook import CollectionNotebook
from tests.my_base_test_case import BaseTestCase


class TestCollectionNotebookTests(BaseTestCase):
    def setUp(self):
        self.subject = CollectionNotebook()
        print("setup             class:TestCollectionNotebookTests")

    def tearDown(self):
        print("teardown          class:TestCollectionNotebookTests")

    def test_fibSeriesUptoN(self):
        result = self.subject.fibSeriesUptoN(10000)
        print(result)

    def test_fibSeriesUptoN(self):
        result = self.subject.pow4OfList([1,2,3,4,5,6,7,8,9])
        print(result)
