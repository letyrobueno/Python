""" Iterable: objects associated with an iter() method
    Examples: strings, lists, file connections, dictionaries
    Iterator: produces next value with next()
"""

# ******** RANGES ********

# Create a range object
numbers = range(5,11)
print('\nRANGES: Printing range object values')
print(numbers) # It outputs range(5, 11)

# Create a list from a range object
numbers_list = list(numbers)
# Sum the numbers
numbers_sum = sum(numbers)

# Iterating with a for-loop (from 0 to 2)
print('\nRANGES: Iterating with a for-loop (from 0 to 2)')
for i in range(3):
    print(i)

# Iterating with a for-loop (from 5 to 10)
print('\nRANGES: Iterating with a for-loop (from 5 to 10)')
for i in range(5,11):
    print(i)

# Using iter()
print('\nRANGES: Using iter() - from 0 to 2')
number = iter(range(3))

print(next(number))
print(next(number))
print(next(number))


# ******** STRINGS ********

# Iterating with a for-loop
print('\nSTRINGS: Iterating with a for-loop')
for letter in 'Super cool!':
    print(letter)

# Using iter()
print('\nSTRINGS: Using iter()')
word = 'Batman'
it = iter(word)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Iterating at once with *
print('\nSTRINGS: Iterating at once with *')
word = 'Batman'
it = iter(word)
print(*it)


# ******** DICTIONARIES ********
# Dictionaries are enclosed in braces
cars = {'toyota': 'corolla', 'ford': 'mustang'}

# Iterating with a for-loop
print('\nDICTIONARIES: Iterating with a for-loop')
for key, value in cars.items():
    print(key, value)


# ******** FILES ********
file = open('file.txt')

# Using iter()
print('\nFILES: Using iter()')
it = iter(file)
print(next(it))
print(next(it))


# ******** LISTS AND TUPLES ********
# Lists and tuples can contain any type of objects (they are like arrays)

# Lists are mutable so they can be extended or reduced at will
# Lists are enclosed in brackets
heroes = ['Batman', 'Superman', 'Wonder Woman']

# Iterating with a for-loop
print('\nLISTS: Iterating with a for-loop')
for item in heroes:
    print(item)

# Using iter()
print('\nLISTS: Using iter()')
heroes_iter = iter(heroes)
print(next(heroes_iter))
print(next(heroes_iter))
print(next(heroes_iter))

# Iterating to print just the first character of each string
print('\nLISTS: Iterating to print just the first character of each string')
result = [hero[0] for hero in heroes]
print(result)

# Using enumerate()
print('\nLISTS: Using enumerate()')
heroes_e = enumerate(heroes)

# Create a list from the enumerated list
heroes_new = list(heroes_e)
print(heroes_new) # Outputs [(0, 'Batman'), (1, 'Superman'), (2, 'Wonder woman')]

# Iterating with a for-loop and enumerate()
print('\nLISTS: Iterating with a for-loop and enumerate()')
for index, value in enumerate(heroes): # default: starts in 0
    print(index, value)
# It outputs:
# 0 Batman
# 1 Superman
# 2 Wonder Woman

# Iterating with a for-loop and enumerate(), setting start
print('\nLISTS: Iterating with a for-loop and enumerate(), setting start')
for index, value in enumerate(heroes, start=5): # starting in 2
    print(index, value)

# Using zip()
print('\nLISTS: Using zip()')
heroes = ['Batman', 'Superman', 'Wonder Woman']
names = ['Bruce Wayne', 'Clark Kent', 'Diana Prince']
result = zip(heroes, names) # it can be two or more lists

# Creating a list of the tuples done by zip() from two lists
result_list = list(result)
print(result_list) # It outputs: [('Batman', 'Bruce Wayne'), ('Superman', 'Clark Kent'), ('Wonder Woman', 'Diana Prince')]

# "Unzipping" tuples
print("\nLISTS: Using zip() and 'unzipping'")
result = zip(heroes, names) # we load the object again (it was unloaded when we printed it)
print('Before unzipping:')
print(*result) # Output: ('Batman', 'Bruce Wayne') ('Superman', 'Clark Kent') ('Wonder Woman', 'Diana Prince')
result = zip(heroes, names) # we load the object again (it was unloaded when we printed it)
result_unzipped = list(zip(*result))
print('After unzipping:')
print(result_unzipped) # Output: [('Batman', 'Superman', 'Wonder Woman'), ('Bruce Wayne', 'Clark Kent', 'Diana Prince')]


# Iterating with a for-loop and zip()
print('\nLISTS: Iterating with a for-loop and zip()')
for z1, z2 in zip(heroes, names):
    print(z1, z2)
# It outputs:
# Batman Bruce Wayne
# Superman Clark Kent
# Wonder Woman Diana Prince

# Yet another way:
print('\nLISTS: Iterating with a for-loop and zip() - Another way')
result = zip(heroes, names)
print(*result)
# It outputs: ('Batman', 'Bruce Wayne') ('Superman', 'Clark Kent') ('Wonder Woman', 'Diana Prince')

# "Unziping" tuples
# Tuples like strings are immutable. Tuples are enclosed in parentheses
heroes = ('Batman', 'Superman', 'Wonder Woman')
names = ('Bruce Wayne', 'Clark Kent', 'Diana Prince')
result = zip(heroes, names)
result1, result2 = zip(*result)

# Checking if result1 and result2 are exactly like the origin lists
print(result1 == heroes)
print(result2 == names)