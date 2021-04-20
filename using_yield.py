def my_gen(start=1, stop_before=10, step=2):
    '''
    we need to generate increasing multiples of a range of numbers
    '''
    number = start
    while number < stop_before:
        yield number # yield will return the next value in the generated sequence
        number *= step

if __name__ == '__main__':
    r = my_gen(stop_before=20)
    print(type(r)) # it is a generator
    for x in r:
        print(x)