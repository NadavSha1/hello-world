from random import randint

def function():
    n1 = randint(1, 5)
    n2 = randint(6, 10)
    return n1, n2

n1, n2 = function()
print(n1, n2)
