""" 
User input the useful in the command-line apps or scripts Python provides 
an inbuilt function called input() to take values from the user. 
"""

# Creating a list to hold the students info
students = []

# method to add students
def add_student(_id, name, age):
    student = {
        "id": _id,
        "name": name,
        "age": age
    }
    students.append(student)

# get students
def get_students():
    return students

# display students
def display_studnet_names():
    students = get_students()
    for student in students:
        print(student["name"])

# Excercise: Do this for multiple students
_id = input("Enter your Id: ")
name = input("Enter your Name: ")
age = input("Enter your Age: ")

add_student(_id, name, age)

display_studnet_names()