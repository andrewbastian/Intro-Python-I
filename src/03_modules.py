"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import getpass
import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print('The name of script:', sys.argv[0])
print('The number of arguments:', len(sys.argv))
print('The arguments are:', str(sys.argv))

# Print out the OS platform you're using:
# YOUR CODE HERE
print('My platform is:', str(sys.platform))

# Print out the version of Python you're using:
# YOUR CODE HERE
print('My Python version is:', str(sys.version))

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print('Current process ID:', os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print('String of cwd:', os.getcwd())
print('Bytestring of cwd:', os.getcwdb())

# Print out your machine's login name
# YOUR CODE HERE
print('Login Name:', os.getlogin())


# more useful option for this:
print('Login Name w/ getpass:', getpass.getuser())
# better because it checks the env cariables LOGNAME or USERNAME
