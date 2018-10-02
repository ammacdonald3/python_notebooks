def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    lettersList = []
    output = ''
    for i in string.ascii_lowercase:
        lettersList += i

    for i in lettersList:
        if i not in lettersGuessed:
            output += i

    return output


lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
