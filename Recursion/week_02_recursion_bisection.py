def isIn(char, aStr):
    if aStr == '':
        return False
    half = int(len(aStr)/2)
    x = aStr[half]
    if char == x:
        return True
    elif char < x and char >= aStr[0]:
        return isIn(char, aStr[:half])
    elif char > x and char <= aStr[-1]:
        return isIn(char, aStr[half:])
    else:
        return False
        
print(isIn('b', 'bbmtw'))
        
