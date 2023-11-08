path = "/Users/omar/Python_FH/testt.txt"

try:
    with open(path) as file:  # will close automatically
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("no file bruv, :(")
