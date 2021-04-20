# by value
a = 1
b = a
a += 1
print(a,b)

# by reference
m = [8,7,6]
n = m.copy() # a separate copy of the list
p = m # by reference to the SAME structure

m[1] = 77

print(n,p)
