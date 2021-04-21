from random import randint
from countries import countries

class Weather():
    '''
    The Weather class takes a non-empty string for the description
    and a floating point number for the temperature
    '''
    def __init__(self, desc, temp):
        self.desc = desc # make use of the setter methods
        self.temp = temp
    @property
    def desc(self):
        return self.__desc
    @desc.setter
    def desc(self, new_desc):
        if type(new_desc) == str and new_desc != '':
            self.__desc = new_desc
        else:
            self.__desc = 'fine'
    @property
    def temp(self):
        return self.__temp
    @temp.setter
    def temp(self, new_temp):
        if type(new_temp) == int or type(new_temp) == float:
            self.__temp = new_temp
        else:
            self.__temp = 12 # a reasonable default
    def changeTemp(self):
        # alter the temperature by a small random amount
        tempChange = randint(-5, 5) 
        self.temp += tempChange
    def __str__(self):
        # output a nicely formatted weather report
        report  = 'The weather is {0} at {1:.2f}C'.format(self.__desc, self.__temp)
        return report

if __name__ == '__main__':
    # exercise this module
    w_ath = Weather('rainy', 9.04)
    w_gal = Weather('windy', 6.70)
    w_kt = Weather('Sunny', 27.98)
    w_kt.changeTemp()
   
    print(w_ath)
    print(w_gal)
    print(w_kt)

    w_default = Weather([], ()) # wrong data types so should fall back to the defaults
    print(w_default)
