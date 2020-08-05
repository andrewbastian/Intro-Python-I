# Write a function is_even
# that will return true if the passed-in number is even.
# YOUR CODE HERE


def is_even(num):
    if(num % 2 == 0):
        print(num, "EVEN")
    else:
        print(num, "ODD")

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE

is_even(num)

# Read a string from the keyboard
s = input("Enter some characters: ")

# Write a function that reverses the input string s
# YOUR CODE HERE


def sesrever(s):
    return s[::-1]

print(sesrever(s))
