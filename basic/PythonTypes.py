

def int_float_type():
    x = 5
    y = 5.4
    print("Displaying int and float")
    print(x)
    print(y)
    print(int(y))
    print('_______________________________________________________________')


def string_type():
    type1 = 'String can be defined in the single quotes'
    type2 = "String can be defined in the double quotes"
    type3 = """String can be defined in the triple quotes"""

    print(type1)
    print(type2)
    print(type3)

    # String important functions
    print("String's capitalize function will capitalize the first letter of the string: {0}".format(type1.capitalize()))
    print("To split the string by a delimiter: {0}".format(type1.split(" ")))
    print('_______________________________________________________________')

def list_type():
    # Create list
    list_obj = ['ABC', 134, True]
    print("Original List: {0}".format(list_obj))
    
    # Access list
    print("First element: {0}".format(list_obj[0]))
    print("Last element: {0}".format(list_obj[-1]))
    
    # Update list
    list_obj[1] = "Updated object"
    print("List after updating an element: {0}".format(list_obj))
    list_obj.append("New Object")
    print("List after updating the list with a new element: {0}".format(list_obj))
    
    # Delete element from list
    del list_obj[0]
    print("List after deleting an element: {0}".format(list_obj))

    # Find an element in the list
    print( "Finding 'Updated object' element in the list: {0}".format("Updated object" in list_obj) )

    # List slicing
    print(f"Skipping first element from the list: {list_obj[1:]}")
    print(f"Skipping first and last elements from the list: {list_obj[1:-1]}")
    # Iterate with index 
    for i in range(0, len(list_obj)):
        print(list_obj[i])
    
    # Iterate without index 
    for obj in list_obj:
        print(obj)
    print('_______________________________________________________________')

def bool_type():
    if(True): 
        print('true')
    if(not False):
        print('Not false')  
    print('_______________________________________________________________')

def dict_type():
    # Create a dictionary
    employee = {
        "Name": "Steve",
        "Id": 1,
        "Senior": True,
        "Feedback": {
            "comment": None
        }
    }
    print("Original dictionary is: {0}".format(employee))

    # Access a dictionary
    print("Name of the employee is {0}".format(employee['Name']))

    # Update an element in the dictionary
    employee['Name'] = "Mark"
    print("Updated Name of the employee is {0}".format(employee['Name']))

    # Get all keys and vaules
    print(f"All the keys: {employee.keys()}")
    print(f"All the values: {employee.values()}")
    
    # Delete a key value pair
    del employee["Name"]
    print(employee)

# Tuples are ordered and unchangeable (immutable)
def tuple_type():
    # Create a tuple
    employee = (10, "Hello", 3.4, True, "Hello")

    # Access a tuple
    print("First element of a tuple: {0}".format(employee[0]))
    print("Last element of a tuple: {0}".format(employee[-1]))
    
    # Update a tuple
        # One cannot update a tuple as it is immutable

    # Delete an element from the tuple
        # One cannot delete an element from the tuple as it is immutable

    # This method will return the count of appearance of the vaule in the tuple
    print(employee.count("Hello"))
    # This method will return the index of the value in the tuple
    print(employee.index(3.4))
    
    # Delete a complete tuple
    del employee

   

# call one by one all the methods and understand the concept
int_float_type()
string_type()
list_type()
bool_type()
dict_type()
tuple_type()