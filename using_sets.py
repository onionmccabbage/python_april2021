# a set - a dictionary with no keys!! (just values)
s = {4,3,2,1, 3.2} # or s = set()
s.add(8)

# members of a set MUST be unique within the set
s2 = {1, 1.0, 1.1, 1.2, 1.3456 } #,2,1,2,1,1,2,1,1,2, '?'}

print(s, s2, type(s), 1 in s)