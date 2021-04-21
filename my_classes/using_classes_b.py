# we are going to inherit from the Person class
from using_classes_a import Person

class Coder(Person): # this class inherits everything the Person class has
    def __init__(self, name, email, age, language):
        super().__init__(name, email, age) # call the parent
        self.language = language
    # we can override methods of the parent class
    def __str__(self):
        return 'Name is {}, email is {} age is {} and language is {}'.format(self.name, self.email, self.get_age(), self.language)

if __name__ == '__main__':
    c = Coder('Clare', 'c@dell.ie', 45, 'python')
    d = Coder('Deirdre', 'd@dell.ie', 35, 'python')
    print(d.language)
    print(c)