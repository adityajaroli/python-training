import json

def add_attendees(attendees):
    try:
        with open("attendees.txt", "w") as att_file:
            json.dump(attendees, att_file)
    except Exception:
        print("error while writing to file")   


def get_attendees():
    try:
        with open("attendees.txt", "r") as att_file:
            if( len(att_file.readlines()) ) != 0:
                return json.load(att_file)
            return []
    except FileNotFoundError:
        print("No record found")
        return []

def display_attendees():
    print(get_attendees())

def read_attendee_info():
    attendees = get_attendees()
    while True:
        empid = input("Enter employee id: ")
        name = input("Enter employee name: ")
        email = input("Enter employee email: ")
        attendees.append({ "empid": empid, "name": name, "email": email })
        print("________________________________________")
        _continue = input("Do you want to continue? (y/n): ")
        if _continue.upper() == "N":
            break
    add_attendees(attendees)

if __name__ == "__main__":
    display_attendees()
    read_attendee_info()