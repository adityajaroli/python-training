
# Define function
# Calling a function
# Passing argument and default values
# Named arguments
# passing many arguments
# return value

# defining a function
def function_name():
    print('"def" is a keyword to define a function')
    print("function_name is the name of the function.")

def function_with_args(name, age, id=1):
    print(id, name, age)

def function_nammed_args(name, age, id):
    print(id, name, age)

def function_many_args_tuple(*args):
    print(args)

def function_many_args_dict(**kwargs):
    print(kwargs)

def function_returs_sum(x, y):
    return x + y

# calling a function
function_name()

# Here it is not mandatory to pass an id to the function. When not passed, it takes the default
# assigned value.
function_with_args("Mark", 24)

# You can pass the arguments in the call with the name. It increases the readability of the code.
# It is highly recommended that when you use any third party library, pass the arguments as nammed arguments
function_nammed_args(id=100, name="Mark", age=24)

# Python supports passing many arguments to the function. Functions like print and format are the example of it.
# Case where you need to have variable number of arguments in the function definition, you can use variable argument concept of python
# It supports two ways:

# 1: Passed as unnameed values
# In this way, all the arguments will be stored in a tuple
function_many_args_tuple(1, "Mark", 25, "India", True)

# 2: Passed as nameed values
# In this way, all the arguments will be stored in a dictionary
function_many_args_dict(id=1, name="Mark", age=25, country="India", isPerson=True)

# Return vaule: Python uses the return keyword to return the values from the method
returned_value = function_returs_sum(10, 90)
print(returned_value)

