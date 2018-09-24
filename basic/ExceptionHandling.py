# Exception Handling: To avoid abnormal termination of the program because of unwanted and unhandled erros, we use 
# exception handling.
# Python uses try-except block to handle exceptions. (Syntax can be seen in the below methods)

session = {
    "Topic": "Python Intro",
    "Time": "12 pm to 1 pm",
    "attendees": "30"
}

# When we try to access a property which is not a part of dictionary, it throws
# a KeyError. We handle that error by mentioning the potential code which can throw an error in the try block
# and mention the error in the except.
def handle_single_exception():
    try:
        count = session["attendee"]
    except KeyError:
        print("Key doesn't exist")

# The first line now will not throw an error as 'attendees' exist in the dictionary but the second line will throw
# a TypeError as the returned attendees is in string format and we are trying to add string with integer.
# So you can handle multiple errors by defining multiple except block
def handle_multiple_exceptions():
    try:
        count = session["attendees"]
        final_count = count + 1
    except KeyError:
        print("Key doesn't exist")
    except TypeError:
        print("Type error")
    except Exception:
        print("Generic exception handler")

# To get the actual error message, we can use the except block like below:
def get_the_actual_exception():
    try:
        count = session["attendees"]
        final_count = count + 1
    except TypeError as error:
        print(error)
    finally:
        print("In the finally")

# This will learn in module section
def get_the_stack_trace():
    pass

# Calling methods
handle_single_exception()
handle_multiple_exceptions()
get_the_actual_exception()
get_the_stack_trace()

print("Final line of the program!!!")