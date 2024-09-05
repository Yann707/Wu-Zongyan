'''import random
random_number = random.randint(1, 9)
number = 0
while True:
    user = int(input("Enter a number between 1 and 9: "))
    number = number + 1
    if user == random_number:
       print(f"Well done!You guessed it in {number} attempts!")
       break
    else:
        print("Wrong number!Try again")

user_input= ""
while user_input != "exit":
    user_input = input("Type something (or exit to quit): ")
    print("You typed:", user_input)

number = []

while True:
    user_input= input("Enter a number (or press Enter to quit): ")

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

names = []

name = input("Enter the first name or quit by pressing Enter: ")
while name != "":
    names.append(name)
    name = input("Enter the next name or quit by pressing Enter: ")

print("Names list:", names)

otherNames = ["Allu", "Ninni"]
names.extend(otherNames)
print("After extending with ['Allu', 'Ninni']:", names)
'''

def num(a, b):
    total = a + b
    print(f"The sum is: {total}")
    subtraction = a - b
    print(f"The subtraction is: {subtraction}")
    multiplication = a * b
    print(f"The multiplication is: {multiplication}")
    division = a / b
    print(f"The division is: {division}")
    return total, subtraction, multiplication, division

num(50,4)
