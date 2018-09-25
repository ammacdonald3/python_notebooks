# Exponent function using iteration
def iterPower(base, exp):
    total = 1
    while exp > 0:
        total *= base
        exp -= 1
    return total

print(iterPower(2, 4))


# Exponent function using recursion
def recurPower(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recurPower(base, exp - 1)
    
print(recurPower(2, 4))