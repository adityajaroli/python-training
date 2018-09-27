
class Employee:

    """
        Static variable: Define any variable outside of the method body in the class, will be 
        created as static variable. Here COMPANY_NAME is a static variable
        static variables can be accessed wthouting creating the instance of the class.
    """ 
    COMPANY_NAME = "XYZ Pvt. Ltd."

    def __init__(self, empid, name):
        self.empid = empid
        self.name = name

    def print_emp_details(self):
        print(f"instance method is called: empid: {self.empid} - name: {self.name}")
    
    """
        we use '@staticmethod' to define the static methods. Static method can be called without without 
        creating an instance of the class.
        Static methods will not receive self pointer as first parameter in the method body.
        This means inside static method, one cannot access any instance method or variable.
    """
    @staticmethod
    def get_complete_address():
        print(f"static method is called: {Employee.COMPANY_NAME}")


if __name__ == "__main__":
    """
        Create Object: Now in this we have defined the constructor with two parameters i.e. 
        whenever we create an instance of this class, we should pass these parameters 
    """
    mark = Employee(123, "Mark")
    # calling an instance method
    mark.print_emp_details()

    # calling static method
    Employee.get_complete_address()

    # One can call static method using class instance as well
    mark.get_complete_address()

    # Accessing static variable ex: Employee.COMPANY_NAME
    print(f"Static variable is accessed: {Employee.COMPANY_NAME}")

    # One can access static variable using class instance as well ex: mark.COMPANY_NAME
    print(f"Static variable is accessed: {mark.COMPANY_NAME}")

