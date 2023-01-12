#TESTING GENERATORS
#YOUTUBE LINK: https://www.youtube.com/watch?v=7lmCu8wz8ro

from time import sleep

def add1(x,y):
    return x + y

class Adder:
    def __call__(self, x, y):
        return x + y

add2 = Adder()

def compute():
    rv = []
    for i in range(10):
        sleep(.5)
        rv.apppend(i)
    return rv

class Compute:
    def __call__(self):
        rv = []
        for i in range(10000):
            sleep(.5)
            rv.append(i)
        return rv

compute = Compute()
