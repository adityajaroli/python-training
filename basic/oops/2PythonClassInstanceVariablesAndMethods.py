

class Employee:

    def __init__(self, empid, name):
        # self is a this pointer which holds properties and function call of the calling object
        # Instance variables can be accessed using instance of the class only.
        self.empid = empid
        self.name = name
    
    """
        This is an instance method. An instance method can be called only by the instance of the class in which
        method is defined. Instance method is defined same as functions defined in python scripts except
        the instance method takes an argument called 'self'. Programmer doesn't need to pass self explicitely. It is
        passed by interpreter.
    """
    def print_emp_details(self):
        print(f"Instance method is called: empid: {self.empid} - name: {self.name}")
        

if __name__ == "__main__":
    """
        Create Object: Now in this we have defined the constructor with two parameters i.e. 
        whenever we create an instance of this class, we should pass these parameters 
    """
    mark = Employee(123, "Mark")
    
    # calling an instance method
    mark.print_emp_details()

    # accessing instance variable
    print(f"Static variable is accessed: {mark.name}")
