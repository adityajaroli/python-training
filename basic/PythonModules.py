"""
A module is a file containing Python definitions and statements.
File name is the module name.
Python modules are imported using 'import' keyword
"""

# 1 way:

# To import display_global_variable() function from VariableScope module/file
import VariableScope

# Access the method
VariableScope.display_global_variable()

# 2 way:

# To import display_global_variable() function from VariableScope module/file
# here we are just renaming the module
import VariableScope as VariableModule

# Access the method
VariableModule.display_global_variable()

# 3 way: We can import only the required function

# To import display_global_variable() function from VariableScope module/file
from VariableScope import display_global_variable

# Access the method
display_global_variable()

# 4 way: import all (*) - We should not import everything as it decreses the readability of the code

# To import display_global_variable() function from VariableScope module/file
from VariableScope import *

# Access the method
display_global_variable()

"""
Introducing __name__ variable:
When we execute the script, Python sets the __name__ global variable with value __main__.
Programmer use this variable to determine whether the script is imported or directly ran.
"""

# We can restrict the use of this file only to the direct run by using __name__ variable

if __name__ == "__main__":
    print("Executing script")

# The python modules are imported the imported script is executed only once and it is cached.
# If you see the output of this script, when it imports the VariableScope module first time, it prints
# 100 100 10 and later it doesn't print.

# 100 100 10 is the output of the call with in the script. You can prevent it by guarding the module with
# __name__ variable.



