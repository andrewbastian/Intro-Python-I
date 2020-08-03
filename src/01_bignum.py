# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE

# There are 3 options:
import math


# option 1:
def exponent_option_1(n):
    return n ** 65536

num = 2

print('option 1:')

print(exponent_option_1(num))

# option 2:
value = 2

exponent_option_2 = pow(value, 65536)

print('option 2:')

print(exponent_option_2)


# option 3:
# needed to use a smaller exponent to get an answer
# math.pow() will convert both arguments to floating point values
# and will always return a float
math_value = 2

exponent_option_3 = math.pow(2, 6)

print('option 3:')

print(exponent_option_3)
