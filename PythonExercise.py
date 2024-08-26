#Exercise1
'''print("Hello, Wu Zongyan!")

#Exercise2
#1
name = input("Enter your name here: ")

print(f"Hello, {name}!")

#2

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * (radius ** 2)

print(f"The area of the circle is: {area:}")

#3

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter = (length + width) * 2

area = length * width

print(f"The perimeter of the rectangle is: {perimeter:}")
print(f"The area of the rectangle is: {area:}")

#4

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

sum= num1 + num2 + num3
product = num1 * num2 * num3
average = sum / 3

print(f"Sum: {sum}")
print(f"Product: {product}")
print(f"Average: {average}")

#5

def convert(talents, pounds, lots):
    talent = 20
    pound = 32
    lot = 13.3

    grams = (talents * talent * pound * lot + pounds * pound * lot + lots * lot)

    kilograms = grams // 1000
    grams = grams % 1000

    return kilograms, grams

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

kilograms, grams = convert(talents, pounds, lots)
print(f"The weight in modern units is: {kilograms:.0f} kilograms and {grams:.2f} grams.")

#6

import random

code1 = [random.randint(0, 9),
         random.randint(0, 9),
         random.randint(0, 9)]
code2 = [random.randint(0, 9),
         random.randint(0, 9),
         random.randint(0, 9)]
code3 = [random.randint(1, 6),
         random.randint(1, 6),
         random.randint(1, 6),
         random.randint(1, 6)]
code4 = [random.randint(1, 6),
         random.randint(1, 6),
         random.randint(1, 6),
         random.randint(1, 6)]
print("3-digit code:", code1)
print("3-digit code:", code2)
print("4-digit code:", code3)
print("4-digit code:", code4)'''

#Exercise2

size = 42
length = float(input("Enter the length of the zander in centimeters: "))

if length >= size:
    print("No problem! You can keep the zander.")
else:
    centimeters = size - length
    print(f"The zander is {centimeters:.2f} centimeters below the size limit.")
    print("Please release the fish back into the lake.")







