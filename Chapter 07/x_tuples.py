#TUPLES, ORDERED and UNCHANGEABLE

Heroes = ("Superman", 34, "male")

print(Heroes.count("male"))
print(Heroes.index("male"))

for _ in Heroes:
    print(_)

if 34 in Heroes:
    print("34 years")

