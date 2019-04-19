from lib.objectorientedpy.animal import Animal


class Cat(Animal):

    def __init__(self, id, age):
        super().__init__(id, 'Cat', age)

    def move(self):
        print('I do cat walk!')

    def talk(self):
        print('MEEEEEEWOAH!')
