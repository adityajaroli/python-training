
# Global scope 
# Local scope
# Change global variable in local scope
# nonlocal scope

# name is a global variable with 'Global Python' as a value
_name = 'Global Python'

# This method will print value of global variable name
def display_global_variable():
    print(_name)

# This defines a two variables name and _id. These are local variables
# we have a global variable named as name which is again defined in this method
# so when this method uses name, it will use the locally defined variable's value
def varibale_scope():
    #Local scope 
    _name = "Local Python"
    _id = 10
    print(_name, _id)

# To change global variable's value you need to tell python interpreter that I am going to use global variable
# Use global keyword for that
def change_global_name():
    global _name
    _name = "Changed Global Python"

# Python can have inner methods.
# So a variable can be defined in the method and in the inner method as well.
# Take an example of x. It is defined in the main method and in the outer method.
# If inner method wants to change the outer method's x then it has to use nonlocal keyword.
def non_local_keyword():
    x = 10
    def outer():
        x = 5

        def inner():
            nonlocal x
            x = 100
            print(x)
        
        inner()
        print(x)
    
    outer()
    print(x)

non_local_keyword()
