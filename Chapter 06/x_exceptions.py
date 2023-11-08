# Exception

try:
    numerator = int(input("enter a number "))
    denominator = int(input("enter a number you wanna divide it with "))
    result = numerator / denominator
    print(result)
except ZeroDivisionError as e:
    print("dont divide by 0")
except ValueError as e:
    print(e)
    print("enter a number coban")
else:
    print(f"you had no mistake, your result again is: {result:.2f}")
finally:
    print("all ways lead to finally")

# except Exception:
#     print("404x")