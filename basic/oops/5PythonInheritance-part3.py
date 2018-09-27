
# Parent class
class Employee:

    def __init__(self):
        self.name = "Employee"
        print("Employee class constructor")

    def get_designation(self):
        print("Employee class get_designation")


class Manager(Employee):

    def __init__(self):
        super().__init__()
        print("Manager class constructor")


if __name__ == "__main__":
    mark = Manager()
    """
        We can see that Manager class doesn't have name variable and get_designation() method.
        These are defined in the Employee class. But as Manager as inherited the Employee class,
        instance of Manager class can use these properties
    """
    print("Accesing Employee calss's name using Manager class's instance: {0}".format(mark.name))
    mark.get_designation()

"""

Output of this program:
    Employee class constructor
    Manager class constructor
    Accesing Employee calss's name using Manager class's instance: Employee
    Employee class get_designation
"""
