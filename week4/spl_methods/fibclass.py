""" Implementation of a Fibonacci generator as a class """

class FibGen:
    def fibn(self, n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return b

    def __getitem__(self, n):
        return self.fibn(n)
