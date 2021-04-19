# this is known as the global scope
g = 'in the global namespace'
# in Python we try not to polute the global namespace
x = None # if we want a variable we MUST initialize it

def someFn():
    global g # we try not to do this too much, since an empty global is good
    g = 'in the function code block namespace'
    pass
    print(g)

# here we invoke our function
someFn()
print(g)