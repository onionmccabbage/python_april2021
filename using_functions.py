# we declare functions by defining them

def addNums(x=0,y=0):
    return x+y

# return the hypotenuse of a right angle triangle
def pythag(x,y):
    """
    This is a docstring - an opportunity to explain the purpose of the function
    Arguments received for x and y
    return the hypotenue or a r-a triangle
    """
    r = (x*x+y*y)**0.5
    return r 

# python does NOT support function overloading i.e. you can have ONE version of a function
# we CAN refer to the arguments collection (a tuple)
def myfn( *args ): # the asterisk makes the variable refer to the positional arguments
    for item in args:
        print( item , type(args), args[3] )

# or the keyword argument collection
def mykw( **kwargs ):
    print(kwargs, type(kwargs)) # kwargs is a dictionary

# sum every numeric value
def sumNumbers(*args):
    total = 0
    if len(args) == 0:
        pass # nothing to add
    elif len(args) == 1:
        total = args[0]
    else:
        for item in args:
            # we should check they are numeric
            if type(item)==float or type(item)==int:
                total += item
    return total

# we can construct structures from keyword args
def makeUser( **kwargs ):
    # the kwargs area dictioanry, so return them...
    return kwargs

if __name__ == '__main__':
    a1 = addNums(3, 2) # these are positional arguments
    a2 = addNums() # use the defaults i.e. zero
    a3 = addNums(y=9, x=3) # these are keyword arguments
    print( a3 )
    print( pythag(3,4) )

    # make use of our arguments function
    myfn(6,5,4,True,'ooo', [], (6,7,8,9))
    mykw(x=0, y=1, b=False, l=[], t=(1,), s='done')

    print( sumNumbers(42, '66', 42, 99, -22) )

    userA = makeUser(name='Ada', age=200, member=True, fave_pet='donkey')
    print(userA)