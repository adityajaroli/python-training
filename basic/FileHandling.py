
# Opens/Creates a file if doesn't exist
def open_file(file_name="new-file.txt"):
    try:
        file = open(file_name, "w")
        file.close()    
    except Exception:
        print("Could not open a file")

def write_to_file(file_name, text):
    try:
        file = open(file_name, "a")
        file.write(text+"\n")
        file.close()
    except Exception:
        print("Could not write to the file")    

def read_data_from_file(file_name):
    try:
        file = open(file_name, "r")
        for line in file.readlines():
            print(line)
        file.close()
    except Exception:
        print("Could not read from the file")    

open_file()
write_to_file("new-file.txt", "This is the first line")
read_data_from_file("new-file.txt")