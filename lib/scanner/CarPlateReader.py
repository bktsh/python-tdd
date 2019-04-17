try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
# import os.path


class CarPlateReader:

    def read_plate_from_image(self, imageUrl):
        # print('imageUrl --> ' + imageUrl)
        # my_path = os.path.abspath(os.path.dirname(__file__))
        # print('my_path --> ' + my_path)
        # path = os.path.join(my_path, "../../data/"+imageUrl)
        # print('path --> ' + path)
        # image = Image.open(path)
        image = Image.open(imageUrl)
        return pytesseract.image_to_string(image)

    def read_other_image(self, imageUrl):
        image = Image.open(imageUrl)
        try:
            return pytesseract.image_to_string(image)
        except:
            raise Exception("WRONNNNNG IMAGE")
