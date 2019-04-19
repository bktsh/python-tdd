class Animal(object):

    def __init__(self, id, name, age):
        self.name = name
        self.age = age
        self.id = id

    def __str__(self):
        return self.name + ' : %s ' % self.age

    def move(self):
        print('NOT DEFINED HOW!')

    def talk(self):
        print('NOT DEFINED HOW!')

    def __eq__(self, other) -> bool:
        return self.id.__eq__(other.id)

