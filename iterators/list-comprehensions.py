""" List Comprehensions collapse for-loops for building lists into a single line.
"""

# ************ Populating a list ************
print('\n****** Populating a list: ******')

# Populating a list with a for-loop
print('Using a for-loop:')
numbers = [15, 7, 18, 4, 11]
new_numbers = []
for num in numbers:
    new_numbers.append(num + 1)
print(new_numbers)

# Better alternative using only one line
print('\nUsing a list comprehension:')
numbers = [15, 7, 18, 4, 11]
new_numbers = [num + 1 for num in numbers]
print(new_numbers)


# ************ List comprehension with range() ************
print('\n****** List comprehension with range() - from 0 to 9: ******')
result = [number for number in range(10)]
print(result)


# ************ Nested loops ************
print('\n****** Nested loops: ******')

# Nested loops with for-loops
print('Using a for-loop:')
pairs = []
for number1 in range(0, 2):
    for number2 in range(6, 8):
        pairs.append((number1, number2))
print(pairs)

# Better alternative using only one line
print('\nUsing a list comprehension:')
pairs2 = [(number1, number2) for number1 in range(0, 2) for number2 in range(6, 8)]
print(pairs2)


# Nested loops to create a matrix using a list of lists
print('\n****** Replacing nested loops to create a matrix using a list of lists: ******')
matrix = [[col for col in range(5)] for row in range(5)]

for row in matrix:
    print(row)

# ************ Conditionals in comprehensions ************
print('\n****** Conditionals in comprehensions: ******')

# (1) Conditionals on the iterable
print('(1) Conditionals on the iterable:')
squares = [num ** 2 for num in range(10) if num % 2 == 0]
print(squares)

# Another example
print('\nAnother example:')
heroes = ['Batman', 'Superman', 'Wonder Woman']
heroes_new = [hero for hero in heroes if len(hero)>6]
print(heroes_new)

# (2) Conditionals on the output expression
print('\n(2) Conditionals on the output expression:')
squares2 = [num ** 2 if num % 2 == 0 else num for num in range(10)]
print(squares2)

print('\nAnother example:')
heroes_new = [hero if len(hero)>6 else "" for hero in heroes]
print(heroes_new)


# ************ Dictionary comprehension - Use braces! ************
print('\nDictionary comprehension:')
pos_neg = {num: -num for num in range(10)}
print(pos_neg) # Output: {0: 0, 1: -1, 2: -2, 3: -3, 4: -4, 5: -5, 6: -6, 7: -7, 8: -8}
