# here is a python comment
a = 3 # an integer
b = 7

c = a/b # a floating point value
c = b//a # integer part of division
c = b%a # remainder after division

c = b**a
c = 'hello' # a string
print(c, type(c))

# Python is restricted only by available resources
g = 10**1000

print(g)

# collections indexed by numbers
s = 'here is a string of characters'

print( s[10:18:2] ) # [start:stop-before:step]

# we can reverse
print(s[::-1])

# lists and tuples
l = [6, False, 5, (8,8,8), 4, c, 'nearly coffee', 3] # this is a list (mutable)
t = (8, 7, True, ['a'], 6, 5, l) # this is a tuple (immutable)

l[1] = 99
# t[1] = 99 # NOOOO!!!!!

# can we mutate members of members of a tuple
t[3][0] = 'b'

print(type(l), type(t), l[1:7], t[::-1])

# we can grab user input - always as a string

u = input('is it coffee yet?')
print(type(u), float(u) )

# True, False and None
print('' == None) # False
print({} == False) # False - it DOES equate to False