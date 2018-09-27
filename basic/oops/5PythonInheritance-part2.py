
# Parent class
class Employee:

    def __init__(self):
        print("Employee class constructor")


class Manager(Employee):

    def __init__(self):
        super().__init__()
        print("Manager class constructor")


if __name__ == "__main__":
    mark = Manager()

"""
We use super() method to call the constructor of the super class.

Output of this program:
    Employee class constructor  
    Manager class constructor
"""
