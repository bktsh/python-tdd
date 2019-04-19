try:
    import Image
except ImportError:
    from PIL import Image
import cv2
import pytesseract
# import os.path


class TextExtractor:

    def read_image_using_cv2(self, imageUrl):
        print(cv2.__version__)
        # print('imageUrl --> ' + imageUrl)
        # my_path = os.path.abspath(os.path.dirname(__file__))
        # print('my_path --> ' + my_path)
        # path = os.path.join(my_path, "../../data/"+imageUrl)
        # print('path --> ' + path)
        # image = Image.open(imageUrl)
        image = cv2.imread(imageUrl, cv2.IMREAD_COLOR)
        # config = ('-l eng --oem 1 --psm 3')
        config = ('--psm 11 --oem 3 -l eng')
        # config = ('--tessdata-dir "tessdata" -l eng --oem 1 --psm 3')
        return pytesseract.image_to_string(image, config=config)
        # return pytesseract.image_to_string(image)

    def read_image_using_pil(self, imageUrl):
        image = Image.open(imageUrl)
        try:
            # config = ('--tessdata-dir "/usr/local/Cellar/tesseract/4.0.0_1/share/tessdata" -l eng --oem 1 --psm 3')
            config = ('--psm 11 --oem 3 -l eng')
            return pytesseract.image_to_string(image, config=config)
            # return pytesseract.image_to_string(image)
        except:
            raise Exception("WRONNNNNG IMAGE")
