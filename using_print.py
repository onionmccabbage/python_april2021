# there are several ways to print

x = 1

print(repr(x)) # repr is the represeentation of a value - not used in production code

# python using __str__() to generate printed output

# there is a format structure we can use for printing

temperature = 12
description = 'sunny'
wind_speed = 6.7

str = 'The weather is {0} (yes {0}) with a wind speed of {1:0.4f} and a temperature of {2:0.2f}'

print( str.format(description, wind_speed, temperature) )
