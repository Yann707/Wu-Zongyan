'''#Exercise1
print("Hello, Wu Zongyan!")

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
print("4-digit code:", code4)

#Exercise3
#1
length = float(input("Enter the length of the zander in centimeters: "))

if length >= 42:
    print("No problem!")
else:
    centimeters = 42 - length
    print(f"The zander is {centimeters:.2f} centimeters below the size limit.Please release the fish back into the lake.")

#2
cabin_class = input("Enter the cabin class (LUX, A, B, or C): ")

if cabin_class == "LUX":
    print("You have selected a LUX cabin: upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("You have selected a cabin in class A: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("You have selected a cabin in class B: windowless cabin above the car deck.")
elif cabin_class == "C":
    print("You have selected a cabin in class C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

#3
gender = input("Enter biological gender (male or female): ")

if gender == "female":
   hemoglobin_value=float(input("Enter hemoglobin value(g/l): "))
   min = 117
   max = 155

elif gender == "male":
   hemoglobin_value=float(input("Enter hemoglobin value(g/l): "))
   min = 134
   max = 167

if hemoglobin_value >= min and hemoglobin_value <= max:
    print("Please stay in good health! Your hemoglobin level is normal.")
elif hemoglobin_value > max :
    print("Please pay attention to your health! Your Hemoglobin level is high.")
elif hemoglobin_value < min :
    print ("Please pay attention to your health! Your Hemoglobin level is low.")

#4
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Exerise 4
#1
number = 1

while number <= 1000:
    if number % 3 == 0:
        print(number)

    number = number+1

#2
while True:
    inches=float(input("Enter inches: "))

    if inches < 0:
        print("Inches cannot be less than zero. The program ends.")
        break
    centimeters = inches * 2.54
    print(f"{inches} inches is equal to {centimeters} centimeters.")

#3
number = []

while True:
    user_input= input("Enter a number or press Enter to quit: ")

    if user_input == "":
        break

    number.append(user_input)

if number:
    min = min(number)
    max = max(number)
    print(f"The smallest number is: {min}")
    print(f"The largest number is: {max}")
else:
    print("No numbers were entered.")

#4
import random
random_number = random.randint(1, 10)
number = 0
while True:
    user = int(input("Enter a number between 1 and 10: "))
    number = number + 1
    if user == random_number:
       print(f"Correct!")
    elif user > random_number:
        print(f"Too high!")
    elif user < random_number:
        print(f"Too low!")

#5
username = "python"
password = "rules"
max_attempts = 5
attempts = 0

while True:
    user_input = input("Enter a username: ")

    if user_input == username:
        user_input = input("Enter a password: ")

        if user_input == password:
            print("Welcome!")
            break
        else:
            print("Invalid password. Please try again.")
    else:
        print("Invalid username. Please try again.")

    attempts += 1

    if attempts >= max_attempts:
        print("Access denied.")
        break
#6
import random

def pi(points):

    inside = 0
    for _ in range(points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            inside += 1

    return 4 * inside / points

if __name__ == "__main__":
    points = int(input("Enter the number of random points: "))
    p = pi(points)
    print("Approximation of pi:", p)


#Exerise 5
#1
import random

user=int(input("how many dice to roll:"))

sum = 0
for i in range(user):
    roll = random.randint(1,6)
    sum += roll
    print(f" {roll}")

print(f"The sum of the numbers is {sum}")

#2
number = []

while True:
    user_input= input("Enter a number or press Enter to quit: ")

    if user_input == "":
        break

    number.append(user_input)

number.sort(reverse=True)

print("The five greatest numbers are:")
for i in range(min(5, len(number))):
    print(number[i])

#3
def prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

user_input = int(input("Enter an integer: "))

if prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")

#4

cities = []

for i in range(5):
    city = input(f"Enter the name of city {i + 1}: ")
    cities += [city]

print("The names of the cities are:")
for city in cities:
    print(city)

#Exercise 6
#1
def dice():
    return random.randint(1, 6)

def main():
    count = 0
    while True:
        count += 1
        result = dice()
        print(f"The result of the {count} roll of the dice is {result}")

        if result == 6:
            break

dice()
main()

#2

import random

def roll_dice(sides):
    roll = 0
    rolls_count = 0

    while roll != sides:
        roll = random.randint(1, sides)
        rolls_count += 1
        print(f"Rolled: {roll}")

    return rolls_count

def main():
    sides = int(input("Enter the number of sides on the dice: "))
    rolls = roll_dice(sides)
    print(f"It took {rolls} rolls to get the maximum number {sides}.")

main()

#3

def main():
    while True:
        num = input("Enter the gallons: ")
        gallons = float(num)

        if gallons < 0:
            break

        liters = gallons * 0.2642
        print(f"{gallons} American gallons is approximately {liters} liters.")


main()

#4
def list(numbers):
    return sum(numbers)

def main():
    numbers = [1, 2, 3, 4, 5]

    result = list(numbers)

    print(f"The sum of the list is: {result}")

main()

#5
def remove_num(input):
    even_num = [x for x in input if x % 2 == 0]
    return even_num

def main():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
    cut_down_list = remove_num(original_list)
    print("original_list:", original_list)
    print("cut_down_list:", cut_down_list)

if __name__ == '__main__':
    main()

#6

def unit_price(diameter, price):
    radius = diameter / 2
    Square_centimeter = 3.14159 * (radius ** 2)
    Square_meter= Square_centimeter * 10000
    unit_price = price / Square_meter
    return unit_price

def main():
    diameter1 = float(input("Enter the diameter of the first pizza in centimeters: "))
    price1 = float(input("Enter the price of the first pizza in euros: "))

    diameter2 = float(input("Enter the diameter of the second pizza in centimeters: "))
    price2 = float(input("Enter the price of the second pizza in euros: "))

    pizza_price1 = unit_price(diameter1, price1)
    pizza_price2 = unit_price(diameter2, price2)

    if pizza_price1 < pizza_price2:
        print("The first pizza provides better value for money.")
    elif pizza_price1 > pizza_price2:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas have the same unit price.")

if __name__ == "__main__":
    main()
'''
#Exercise7
#1
def season(month):
    seasons = ("Winter", "Spring", "Summer", "Autumn")
    if 1 <= month <= 2 or month == 12:
        return seasons[0]
    elif 3 <= month <= 5:
        return seasons[1]
    elif 6 <= month <= 8:
        return seasons[2]
    elif 9 <= month <= 11:
        return seasons[3]

def main():
    month = int(input("Enter the month from 1-12  :"))
    seasons = season(month)
    print(f"The season for month {month} is {seasons}.")

if __name__ == "__main__":
    main()

#2
new_name = set()
existing_name = []

while True:
    name = input("Enter a name: ")

    if name == "":
        break

    if name in new_name:
        print("Existing name")
    else:
        new_name.add(name)
        print("New name")

    existing_name.append(name)

print("All entered names:")
for name in existing_name:
    print(name)

#

