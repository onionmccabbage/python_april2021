# determine if a number is larger or smaller than another number

a = int(float(input('first number? ')))
b = int(float(input('secomd number? ')))

# using 'if' logic

if a<b: # the colon begins a code block
    print('first is less than second')
elif a>b:
    print('second is less than first')
else:
    print('probably the same number')

