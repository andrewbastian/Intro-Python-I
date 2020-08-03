"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string
method, and by using f-strings.
"""


# Using the printf operator (%),
# print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
x = 10
print("%d" % (x,))

y = 2.25
print("%f" % (y,))

z = "I like turtles"
print("%s" % (z,))
# Use the 'format' string method to print the same thing
print('{}'.format(x))
print('{}'.format(y))
print('{}'.format(z))
# Finally, print the same thing using an f-string
print(f"x is {x}, y is {y}, and I'd just like to say {z}")