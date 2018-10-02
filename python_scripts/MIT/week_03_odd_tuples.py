def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    return tuple([i for i in aTup[::2]])

    # EASIER SOLUTION BELOW
    return aTup[::2]

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))