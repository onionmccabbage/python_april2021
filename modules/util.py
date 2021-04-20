# this is util.py, inside the 'modules' package

# here is a function to check a value can be cast as an integer

def checkInt(i):
    '''
    This utility checks a value is an integer
    '''
    if type(i) == int:
        return i
    else:
        # we might get an exception so use a 'try' block
        try:
            i = int(float(i))
        # we can have one or more exception blocks
        except ValueError as e: # specifically handle 'ValueError' exception ehre
            print(e)
            i = 0 # sensible default
        except Exception as e: # handle any other exception here
            print(e)
        finally:
            return i

if __name__ == '__main__':
    # we can exercise the code
    print( checkInt(3) ) # expect 3
    print( checkInt(5.6) ) # expect 5
    print( checkInt('oops') ) # expect an exception
    print( checkInt('-87.654') ) # expect -87