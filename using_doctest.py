import doctest

def cube(x):
    '''
    this function returns the cube of a number
    >>> cube(3)
    27
    >>> cube(-1)
    -1
    '''
    return x*x*x

if __name__ == '__main__':
    doctest.testmod(verbose=True)
    cube(3) # expect 27

