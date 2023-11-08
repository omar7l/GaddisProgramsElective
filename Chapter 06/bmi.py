def bmicalculator(height, weight):
    return  height / weight
try:
    print(bmicalculator(1.89, 85))
    print(bmicalculator(1.60, 0))
except Exception as e:
    print(e)