from unittest import TestCase

from lib.objectorientedpy.cat import Cat
from lib.objectorientedpy.eagle import Eagle
from lib.objectorientedpy.zoo import Zoo
from tests.my_base_test_case import BaseTestCase


class ZooTests(BaseTestCase):

    def setUp(self):
        print("setup             class:ZooTests")

    def tearDown(self):
        print("teardown          class:ZooTests")

    def test_add_animal(self):
        zoo = Zoo([Cat(1, 2), Eagle(2, 5)])
        self.assertEqual(len(zoo.animals), 2)
        zoo.add_animal(Eagle(3, 12))
        for animal in zoo.animals:
            print(animal)
        self.assertEqual(len(zoo.animals), 3)

    def test_remove_animal(self):
        zoo = Zoo([Cat(1, 2), Eagle(2, 5)])
        self.assertEqual(len(zoo.animals), 2)
        zoo.remove_animal(Cat(1, 2))
        self.assertEqual(len(zoo.animals), 1)
