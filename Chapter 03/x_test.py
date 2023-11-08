height = float(input('Enter your height in m: '))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height * height)

print(f"your BMI is: {BMI:.2f}")

if BMI >= 25:
    print("You are too fat bruv")
elif BMI < 25:
    print("You are too skinny bruv")