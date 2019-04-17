from unittest import TestCase

from lib.scanner.CarPlateReader import CarPlateReader

class CarPlateReaderTests(TestCase):
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
        print("setup             class:CarPlateReaderTests")

    def tearDown(self):
        print("teardown          class:CarPlateReaderTests")


    def setup_method(self, method):
        print("setup_method      method:%s" % method.__name__)

    def teardown_method(self, method):
        print("teardown_method   method:%s" % method.__name__)

    def test_read_plate_from_image(self):
        reader = CarPlateReader()
        # text = reader.read_plate_from_image("car.png")
        text = reader.read_plate_from_image("/Users/hbaktas/projects/practice/python-tdd/data/car.png")
        print('I read this from image test_read_plate_from_image: YAAY --> ' + text+'\n')

    def test_read_screenshot(self):
        reader = CarPlateReader()
        # text = reader.read_plate_from_image("car.png")
        # text = reader.read_other_image("/Users/hbaktas/projects/practice/python-tdd/data/scan2.png")
        # print('I read this from image test_read_other: YAAY --> ' + text+'\n')
        # text = reader.read_other_image("/Users/hbaktas/projects/practice/python-tdd/data/image004.jpg")
        # print('I read this from image test_read_other: YAAY --> ' + text+'\n')
        text = reader.read_other_image("/Users/hbaktas/projects/practice/python-tdd/data/HASHEM.JPG")
        print('I read this from image test_read_other: YAAY --> ' + text+'\n')
        # text = reader.read_other_image("/Users/hbaktas/projects/practice/python-tdd/data/gordy.png")
        # print('I read this from image test_read_other: YAAY --> ' + text+'\n')

    def test_read_bowling_scores(self):
        reader = CarPlateReader()
        # text = reader.read_plate_from_image("car.png")
        text = reader.read_other_image("/Users/hbaktas/projects/practice/python-tdd/data/scores.png")
        print('I read this from image test_read_other: YAAY --> ' + text +'\n')

    def test_read_other_scan3(self):
        reader = CarPlateReader()
        # text = reader.read_plate_from_image("car.png")
        text = reader.read_other_image("/Users/hbaktas/projects/practice/python-tdd/data/scan3.png")
        print('I read this from image test_read_other_scan3: YAAY --> ' + text+'\n')
