# we can ask for input

# guess = input('guess the number')
# guess_float = float(guess)
# guess_int = int(guess_float)
# or...
# guess = int(float(input('guess the number')))

# print(guess)

# lists
l = [7,6,5,4,3] # or l = list()
l.append(99) # add a new member to the end of the list
l.insert(1, 'new') # ...at an index position
w = l.pop()
x = l.remove('new')
t = tuple(l)
print(t, w, x) # None type tells us there is no thing

# tuples
t = (8,) # careful - a one-member tuple
t = tuple([8])
print(t, type(t))

# non-indexed collection of values
# ... a dictionary, a collection of name:value pairs

d = {'name':'Timnit', 'age':42, 'member':True} # or d = dict()
d['status'] = l
print(d.keys(), d.values(), d['name'], d['member'], d, type(d))

