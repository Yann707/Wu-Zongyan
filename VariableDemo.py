'''a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))

a, b = b, a

print(f"a = {a}")
print(f"b = {b}")

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter = (length + width) * 2

area = length * width

print(f"The perimeter of the rectangle is: {perimeter:}")
print(f"The area of the rectangle is: {area:}")'''

age = int(input("Enter your age: "))
if 15 <= age < 18:
    weight = float(input("Enter your weight (kg): "))
if (age >=18 or age>=15 and weight >=55):
    print("The medicine can be used.")

