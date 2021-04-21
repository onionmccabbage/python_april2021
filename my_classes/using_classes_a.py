
# we can declare a class
class Person(): # all classes descend from object implicitly
    '''
    Explain your class in a docstring like this
    This class inherits from object and declares a Person
    Age must be an integer
    '''
    def __init__(self, newname, email, age): # self is required
        # note  - we are implicitly calling the setter methods here
        self.name = newname # these are properties of this class
        self.email = email # double underscore is called 'name mangling'
        self.set_age(age) # invoke our setter method
    # we can write getter and setter methods for properties
    def get_age(self):
        return self.__age
    def set_age(self, updated_age):
        # we can check the age is a positive integer
        if isinstance(updated_age, int):
            self.__age = updated_age
        else:
            self.__age = 100 # set a default
    # we can write accessor and mutator methods as property decorators
    @property # this is a built-in decorator
    def name(self): # getter
        return self.__name
    @name.setter # setter
    def name(self, updated_name):
        # we sould ensure the value is valid
        if isinstance(updated_name, str) and updated_name != '':
            self.__name = updated_name
    @property 
    def email(self):
        return self.__email
    @email.setter
    def email(self, updated_email): 
        # we sould ensure the value is valid
        if isinstance(updated_email, str) and updated_email != '':
            self.__email = updated_email
    def __str__(self): # the __str__ method is ALWAYS used by any print statement
         return 'Name is {}, email is {} and age is {} [{}]'.format(self.name, self.email, self.__age, self.__internal())
    # we can name mangle a method
    def __internal(self):
        return 'hidden'

if __name__ == '__main__':
    p = Person('Polly', 'p@p.ie', 42)
    q = Person('Timnit', 't@g.ie', 'coffee')

    # explore the instances
    p.__age = 'this is not a number' # here we create another arbitrary property called __age
    p.name = 'does thsi work' # this uses the setter method
    print(p.__age) #, q.__name)
    print(p) # this will use the __str__ method
    # we CANNOT directly aces properties or methods that have been name-mangled
    # print( p.__internal() ) # fails
    # we can assign arbitrary properties
    q.wibble = 'wobble'
    print(q.wibble)
    # it IS posible to access the name mangled proerties if your really try
    print(p._Person__age) 
    # we can use the decorated members as if they are properties
    p.email = 'altered@g.ie'
    print(p.email)
    # we can access the docstring like this
    print(p.__doc__)