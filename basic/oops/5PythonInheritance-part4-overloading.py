
# Parent class
class Employee:

    def __init__(self):
        print("Employee class constructor")


class Manager(Employee):

    def __init__(self):
        super().__init__()
        print("Manager class constructor")

    """
        Method Overloading: This is one of the important property of oops
        which python doesn't support.
        Defining multiple methods with the same name but different arguments is called the method
        overloading. We may overload the methods but can only use the latest defined method.

        So in the below scenario, one can call over_load_method(self, id, name) only as it is the latest defined one 
        in the class.
    """
    def over_load_method(self, name):
        print("Overload method with name parameter")
    
    def over_load_method(self, id, name):
        print("Overload method with id and name parameter")

if __name__ == "__main__":
    mark = Manager()

    # call to over_load_method("Mark") will fail. Commenting out the below call as it will fail the execution
    # mark.over_load_method("Mark")
     
    # call to over_load_method(1, "Mark") will pass
    mark.over_load_method(1, "Mark")

"""

Output of this program:
    Employee class constructor
    Manager class constructor
    Overload method with id and name parameter
"""
