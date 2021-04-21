# we can override any of the built-ins of python

# example: we want a Word class which has equality without respect to case
class Word():
    def __init__(self, text):
        self.text = text
    # here we override the buit-in equality operator
    def __eq__(self, other_word):
        return self.text.lower() == other_word.text.lower()

# __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-or-equal

# other 'magic methods'
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the object

if __name__ == '__main__':
    # normal string comparison
    low = 'hello'
    hi  = 'HELLO'
    print(low==hi) # False
    # now we try our Word class
    w1 = Word('hello')
    w2 = Word('HELLO')
    print(w1==w2) # True