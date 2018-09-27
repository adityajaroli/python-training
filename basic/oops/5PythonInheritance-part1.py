"""
    Inheritance: Accepting properties and methods from one class to another class is called inheritance
    Here in the below example Employee is my parent (super_class) class and Manager is my child (sub-class) class.
"""

# Parent class
class Employee:

    def __init__(self):
        print("Employee class constructor")


# Child class. To inherit a class, we use the below syntax:
# ChildClass(ParentClass)
class Manager(Employee):

    def __init__(self):
        print("Manager class constructor")


if __name__ == "__main__":
    mark = Manager()

"""
When object of child class is created, constructor of only child class is called. Check next session to see how we call constructor of 
super class from sub class.

Output of this program:
    Manager class constructor
"""
