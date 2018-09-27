
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
        Calling Super class method from overrided method in sub class
        You can call the super class method from the overrided method using super()
    """
    def get_designation(self):
        super().get_designation()
        print("Manager class get_designation")


if __name__ == "__main__":
    mark = Manager()
     
    mark.get_designation()

"""

Output of this program:
    Employee class constructor
    Manager class constructor
    Employee class get_designation
    Manager class get_designation
"""
