# comprehensions iterate through a generator

# a list generator (we comprehesively iterate over the values)
num_l = [num for num in range(0, 100, 5)]
# a generator
num_t = (num-1 for num in range(0,100, 20))

print(num_l)

# iterate over our generator
for i in num_t:
    print(i, end=' ')

# dictionary comprehension
phrase = 'are we there yet?'
char_counts = {letter: phrase.count(letter) for letter in phrase}
print(char_counts)


