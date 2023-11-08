import os.path

path = "/Users/omar/Python_FH/test.txt"

if os.path.exists(path):
    print("Locations exist")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("it is a directory")
else:
    print("nothing bro")