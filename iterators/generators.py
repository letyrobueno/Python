""" Generator functions allow to declare a function that behaves like an iterator
	List comprehension returns a list (wholly generated at its creation time), while generators return a generator object
	A generator can be created in two ways:
	(1) Very similar to a list comprehension;
	(2) As a function, using yield to return the next value.
"""

# Instead of this list comprehension:
print('\nList comprehension:')
product = [2 * num for num in range(10)]
print(product)

# We can use this generator:
print('\nUsing a generator:')
product_gen = (2 * num for num in range(10)) # Use parentheses instead of brackets
# Iterating over the generator:
print(list(product_gen))

# Another way:
product_gen = (2 * num for num in range(10)) # Use parentheses instead of brackets
for num in product_gen:
	print(num)

# Another way - Lazy Evaluation (object is evaluated when it is needed, not when it is created):
print('\nLazy Evaluation:')
product_gen = (2 * num for num in range(10)) # Use parentheses instead of brackets
print(next(product_gen))
print(next(product_gen))
print(next(product_gen))


# A generator from a list:
print('\nA generator from a list:')
heroes = ['Batman', 'Superman', 'Wonder Woman']
lengths = (len(hero) for hero in heroes)
print(list(lengths))

# Another way:
print('\nA generator from a list - Using a function with yield:')
# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the length of the strings in input_list."""

    for person in input_list:
        yield len(person)

print(list(get_lengths(heroes)))


# ************ Conditionals in generators ************
print('\nConditionals in generators:')
even_numbers = (number for number in range(10) if number % 2 == 0)
print(list(even_numbers))


# ************ Generator as a function, using yield to return the next value ************
print('\nGenerator as a function, using yield to return the next value:')
def number_sequence(n):
	"""Generate values from 0 to n."""
	i = 0
	while i < n:
		yield i
		i += 1
result = number_sequence(5)
print(list(result))