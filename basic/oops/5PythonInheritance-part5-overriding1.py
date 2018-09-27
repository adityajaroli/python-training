
# Parent class
class Employee:

    def __init__(self):
        print("Employee class constructor")

    def get_designation(self):
        print("Employee class get_designation")

class Manager(Employee):

    def __init__(self):
        super().__init__()
        print("Manager class constructor")

    """
        Method Overriding: This is one of the important property of oops which python supports.
        
        As we know in inheritance the child class receives methods and variables from the super class.
        So implementing the inherited method into the child class again is called method overriding.

        So in the below scenario, get_designation() method is avaiable in both the super and sub class.
        Here in sub class we have implemented the get_designation method again so we call this method as overriding method
        and this concept as method overriding
    """
    def get_designation(self):
        print("Manager class get_designation")


if __name__ == "__main__":
    mark = Manager()
     
    # call to get_designation()
    mark.get_designation()

    # Use super() to call the super class method from the subclass. Check the next example

"""

Output of this program:
    Employee class constructor
    Manager class constructor
    Manager class get_designation
"""
