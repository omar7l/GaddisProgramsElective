
def main():
    print("This program finds the two largest integers in a list.")
    print()

    # Get the input from the user
    nums = []
    num = input("Enter a number (blank to quit): ")
    while num != "":
        nums.append(int(num))
        num = input("Enter a number (blank to quit): ")

    # Sort the list in ascending order
    nums.sort()

    # Display the two largest numbers
    print("The two largest numbers are:", nums[-1], "and", nums[-2])