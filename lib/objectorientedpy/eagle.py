from lib.objectorientedpy.animal import Animal


class Eagle(Animal):

    def __init__(self,id, age):
        super().__init__(id, 'Eagle', age)

    def move(self):
        print('I Fly!')

    def talk(self):
        print('IDK!')

    def __str__(self):
        return 'Lovely '+ super().__str__()

