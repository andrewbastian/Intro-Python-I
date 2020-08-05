"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated.

Take a look at
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [i for i in range(1, 6)]
"""for x in range(1, 6):
    y.append(x)
"""
print(f'task1 {y}')

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

cubes = [i**3 for i in range(10)]
"""for c in range(10):
    cubes.append(c**3)
"""
print(f'task2 {cubes}')

# Write a list comprehension that utilizes slicing syntax to product
# a list with the elements from the first half of the `cubes` list

first_half_of_cubes = []
first_half_of_cubes.append(cubes[:5])

print(f'task3 {first_half_of_cubes}')

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

lowercase = ["foo", "bar", "baz"]

uppercase = [u.upper() for u in lowercase]
"""for u in lowercase:
    uppercase.append(u.upper())"""
print(uppercase)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

num_list = [n for n in x if int(n) % 2 == 0]

print(num_list)
# What do you need between the square brackets to make it work?
