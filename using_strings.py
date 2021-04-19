# string collections are immutable

s = '    all done    '
# s[0] = 'A' # fails
s = '     All done    '
s2 = s.lower() # we CANNOT mutate in place, we must asign
s3 = s2.strip() # strip any whitespace
print(s3)