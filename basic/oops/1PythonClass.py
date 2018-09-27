
#Global variable
employees = []

# Class is defined to hold the properties and functions of an entity
# Classes increase readability of the code
# In Python, we create class using the keyword 'class'.
# It's a good practice to keep the first letter of your class name capital
class DummyClass:

    # Static variable: static variables can be accessed wthouting creating the instance of the
    # class. 
    COMPANY_NAME = "XYZ Pvt. Ltd."

    """
        Constructor: constructor is a special method which is added to the code by default.
        You can define your own constructor method or I would say you can override the constructor
        method. We use contructor to initialize instance variables
    """
    def __init__(self):
        print("Constructor is called")

if __name__ == "__main__":
    """
        Create Object: The objects are created like below. 
    """
    instance__ = DummyClass()

# Output: When you run this scritp you will get below output: 'Constructor is called'
