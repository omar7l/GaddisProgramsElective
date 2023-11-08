import sympy

num = int(input("Enter a number: "))

if sympy.isprime(num):
    print("number is", num, "is prime")
else:
    print("number is", num, "is not prime")