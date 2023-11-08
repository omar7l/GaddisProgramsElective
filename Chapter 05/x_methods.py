def BMI(height, weight):
    return weight / (height ** 2)


height1 = float(input("put in your height"))
weight1 = float(input("put int your weight"))

print(f"{BMI(height1, weight1):.2f}")
