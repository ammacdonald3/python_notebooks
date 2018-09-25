# Note that 'reverse' has the default value of False
def printName(firstName, lastName, reverse = False):
    """
    Input: firstName (string), lastName (string), reverse (boolean)
    Returns firstName lastName if reverse = False or not included; otherwise returns lastName, firstName
    """
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)

# When calling the function, we can pass parameters without the argument name
print("Normal Order:")
printName('Andrew', 'MacDonald')

print("")

# If we want to reverse the order, we need to name the parameters
print("Reversed Order:")
printName(lastName = 'MacDonald', reverse = True, firstName = 'Andrew')