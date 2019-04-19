
class Zoo(object):

    def __init__(self, animals):
        super().__init__()
        self.animals = animals[:]

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)

