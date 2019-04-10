L = [2, 3, 5, 7]

def mymap(fn, iterable):
    for x in iterable:
        yield fn(x)

L3 = list(map(lambda x: x ** 2 + 1, L))
L4 = list(mymap(lambda x: x ** 2 + 1, L))
print("L3=", L3)
print("L4=", L4)

