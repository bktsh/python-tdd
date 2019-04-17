__all__ = ['Calculator', 'add_outside']

def add_outside(a, b):
    return a + b

class Calculator:

    def __init__(self, brand='SONY'):
        print('Creating a %s calculator' % brand)
        self.brand =  brand

    def add(self,a, b):
        return a + b

    def multiply(self,a, b):
        return a * b

    def divide(self,a, b):
        return a / b

    def subtract(self,a, b):
        return a - b

    if (__name__ == '__main__'):
        print('welcome to my calculator')