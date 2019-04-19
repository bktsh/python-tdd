from lib.scanner.TextExtractor import TextExtractor
from tests.my_base_test_case import BaseTestCase


class TextExtractorTests(BaseTestCase):

    def setUp(self):
        print("setup             class:TextExtractorTests")

    def tearDown(self):
        print("teardown          class:TextExtractorTests")

    def test_using_cv2(self):
        reader = TextExtractor()
        # text = reader.read_image_using_cv2("/Users/hbaktas/projects/practice/python-tdd/data/bowling_scores.png")
        # print('I read this from image bowling_scores: YAAY --> ' + text+'\n')
        # text = reader.read_image_using_cv2("/Users/hbaktas/projects/practice/python-tdd/data/car.png")
        # print('I read this from image car: YAAY --> ' + text+'\n')
        # text = reader.read_image_using_cv2("/Users/hbaktas/projects/practice/python-tdd/data/gordy.png")
        # print('I read this from image gordy: YAAY --> ' + text+'\n')
        text = reader.read_image_using_cv2("/Users/hbaktas/projects/practice/python-tdd/data/HASHEM.JPG")
        print('I read this from image HASHEM: YAAY --> ' + text+'\n')
        # text = reader.read_image_using_cv2("/Users/hbaktas/projects/practice/python-tdd/data/image004.jpg")
        # print('I read this from image image004: YAAY --> ' + text+'\n')
        # text = reader.read_image_using_cv2("/Users/hbaktas/projects/practice/python-tdd/data/scan2.png")
        # print('I read this from image scan2: YAAY --> ' + text+'\n')
        # text = reader.read_image_using_cv2("/Users/hbaktas/projects/practice/python-tdd/data/scan3.png")
        # print('I read this from image scan3: YAAY --> ' + text+'\n')

    def test_read_using_pil(self):
        reader = TextExtractor()
        # text = reader.read_image_using_pil("/Users/hbaktas/projects/practice/python-tdd/data/bowling_scores.png")
        # print('I read this from image : YAAY --> ' + text+'\n')
        text = reader.read_image_using_pil("/Users/hbaktas/projects/practice/python-tdd/data/car.png")
        print('I read this from image bowling_scores: YAAY --> ' + text+'\n')
        # text = reader.read_image_using_pil("/Users/hbaktas/projects/practice/python-tdd/data/gordy.png")
        # print('I read this from image gordy: YAAY --> ' + text+'\n')
        # text = reader.read_image_using_pil("/Users/hbaktas/projects/practice/python-tdd/data/HASHEM.JPG")
        # print('I read this from image HASHEM: YAAY --> ' + text+'\n')
        # text = reader.read_image_using_pil("/Users/hbaktas/projects/practice/python-tdd/data/image004.jpg")
        # print('I read this from image image004: YAAY --> ' + text+'\n')
        # text = reader.read_image_using_pil("/Users/hbaktas/projects/practice/python-tdd/data/scan2.png")
        # print('I read this from image scan2: YAAY --> ' + text+'\n')
        # text = reader.read_image_using_pil("/Users/hbaktas/projects/practice/python-tdd/data/scan3.png")
        # print('I read this from image scan3: YAAY --> ' + text+'\n')
