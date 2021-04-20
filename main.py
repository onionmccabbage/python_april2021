# we can import stuff
import using_functions as fn

# we can import from the python standard library
import math

# we can import libraries that have been installed to our python
import requests # remember to pip install requests

from using_functions import sumNumbers
from modules.util import checkInt
# any module that is invoked directly is given an internal __name__ of '__main__'
if __name__ == '__main__':
    # ask user for x and y
    x = input('value for x? ')
    y = input('value for y? ')

    # check they are int (or default)
    x = checkInt(x)
    y = checkInt(y)

    # use in pythag
    r = fn.pythag(x,y)
    print('For x={} and y={} r={}'.format(x, y, r))

    x = fn.pythag(30, 40)
    print(x)
    y = sumNumbers(5,4,3,2,1)
    print(y)

    print(math.sqrt(100)) # expect 10