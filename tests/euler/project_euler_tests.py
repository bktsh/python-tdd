from lib.euler.ProjectEuler import ProjectEuler
from tests.my_base_test_case import BaseTestCase


class ProjectEulerTests(BaseTestCase):

    def setUp(self):
        self.euler = ProjectEuler()
        print("setup             class:ProjectEulerTests")

    def tearDown(self):
        print("teardown          class:ProjectEulerTests")

    def test_below1000_multiplies_of_3or5(self):
        result = self.euler.below1000_multiplies_of_3or5()
        print(result)
        print('test_below1000_multiplies_of_3or5 --> ' , sum(result))

    def test_below1000_multiplies_of_3and5(self):
        result = self.euler.below1000_multiplies_of_3and5()
        print(result)
        print ('test_below1000_multiplies_of_3and5 --> ', sum(result))

    def test_sum_natural(self):
        print('sum(range(1,1000)) --> ',sum(range(1,1000)))