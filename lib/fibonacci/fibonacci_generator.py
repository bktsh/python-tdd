import types

class FibonacciGenerator(object):

    # fill in this function
    def fib(self):
        a, b = 1, 1
        while 1:
            yield a
            a, b = b, a + b

    def fib_generator(self, max):
        if type(self.fib()) == types.GeneratorType:
            print("Good, The fib function is a generator.")
            counter = 0
            for n in self.fib():
                print(n)
                counter += 1
                if counter == max:
                    break

if (__name__ == '__main__'):
    tester = FibonacciGenerator()
    tester.fib_generator(10)


