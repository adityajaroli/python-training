
class Employee:

    COMPANY_NAME = "XYZ Pvt. Ltd."

    def __init__(self, empid, name):
        self.empid = empid
        self.name = name

    def print_emp_details(self):
        print(f"empid: {self.empid} - name: {self.name}")
    
    @staticmethod
    def get_complete_address():
        print(f"static method is called: {Employee.COMPANY_NAME}")
    
    """
        class methods are defined using @classmethod annotation. class method requires one
        parameter cls (class name). The class name is passed by interpreter. So one should not
        pass it explicitely like self for instance methods.
        One can call the class method as they call static method. The only difference between
        static and class method is that class method has one required argument and static method
        doesn't
    """
    @classmethod
    def get_address(cls):
        print(f"class method is called from {cls} class")


if __name__ == "__main__":
    # calling static method
    Employee.get_complete_address()

    # calling class method
    Employee.get_address()