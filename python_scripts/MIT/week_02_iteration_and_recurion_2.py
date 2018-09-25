# Greatest common divisor function using iteration
def gcdIter(a, b):
    test = min(a, b)
    while a%test != 0 or b%test != 0:
        test -= 1
    return test

print(gcdIter(34, 40))


# Greatest common divisor function using recursion
def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        