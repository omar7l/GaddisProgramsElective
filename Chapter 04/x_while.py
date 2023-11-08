# name = input("gimme your name ")
#
# while name == "":
#     print("you did not enter ur name bruv")
#     name = input("gimme your name ")
#
# print(f"whatsup {name}")

food = int(input(f"enter your favourite food "))
Foods = []

while not food == "x":

    Foods.append(food)
    print(f"{food} is added toy our list")


    food = input(f"enter another one of your favourite foods or x to exit ")

print(f"Your favourite foods are:{Foods}")

