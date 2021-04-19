# we can iterate over collections

l = [5,4,3,True,(1,), 'hi']

for item in l:
    print(item)

# there is a range object...
r = range(99) 
print(r, type(r))

# we can use a range to generate values
for i in range(-9, 10, 3): # start, stop-before, step
    print(i)

# we can iterate over collections
s = 'is it lunch yet'
d = {'name':'Ada', 'age':148, 'member':True}

for char in s:
    print(char)

for item in d: # careful - dict is NOT indexed by number
    print(item, d[item])

for key, value in d.items(): # items() returns all items in the dict
    print(key, value)

# we can write our own generator
my_values = ( num**0.5 for num in range(-10*100, 10*100) ) # a tuple generator object
print(type(my_values))

# we can now use our generator to generate values as we need them
for root in my_values:
    print(root)

# we could write a generator for even nubmers
evens = ( num for num in range(0, 100) if num%2 == 0 )
for e in evens:
    print(e)