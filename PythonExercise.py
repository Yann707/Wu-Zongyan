'''
#Exercise1
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
for i in range(len(number)):
    if i >= 5:
        break
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

#3
data = {}

while True:
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        icao_code = input("Enter the ICAO code of the airport: ")
        airport_name = input("Enter the name of the airport: ")
        data[icao_code] = airport_name
        print("Airport information saved.")

    elif choice == '2':
        icao_code = input("Enter the ICAO code of the airport: ")
        if icao_code in data:
            print(f"The name of the airport is: {data[icao_code]}")
        else:
            print("Airport not found.")

    elif choice == '3':
        print("Program execution ends.")
        break

#Exercise8
#1
import mysql.connector

def get_airport_info(cursor, icao_code):
    query = "SELECT name, municipality FROM airports WHERE ident = %s"
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()
    return result

def main():
    icao_code = input("Enter the ICAO code of the airport: ")

    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='0707',
        database='table',
        autocommit=True
    )

    cursor = connection.cursor()

    airport_info = get_airport_info(cursor, icao_code)

    if airport_info:
        airport_name, municipality = airport_info
        print(f"Airport: {airport_name}, Location: {municipality}")
    else:
        print("No airport found.")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()

#2
import mysql.connector

def fetch_airports_by_country(cursor, iso_country):
    query = """
    SELECT type, COUNT(*) as count
    FROM airports
    WHERE iso_country = %s
    GROUP BY type
    ORDER BY count DESC
    """
    cursor.execute(query, (iso_country,))
    return cursor.fetchall()

def main():
    iso_country = input("Enter the ISO country code (e.g., 'FI' for Finland): ").upper()

    connection = mysql.connector.connect(
        host='127.0.1.1',
        port=3306,
        database='table',
        user='root',
        password='0707',
        autocommit=True
    )

    cursor = connection.cursor()

    airport_data = fetch_airports_by_country(cursor, iso_country)
    if airport_data:
        print(f"Airports in country '{iso_country}':")
        for airport_type, count in airport_data:
            print(f"{count} {airport_type} airport(s)")
    else:
        print(f"No airports found for country code '{iso_country}'.")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()


#3
import mysql.connector
from geopy.distance import geodesic

def coordinates(cursor, ident):
    query = f"SELECT latitude_deg, longitude_deg FROM airports WHERE ident = '{ident}'"
    cursor.execute(query)
    result = cursor.fetchone()
    return result

def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

def main():
    airport1_icao = input("Enter the ICAO code of the first airport: ").upper()
    airport2_icao = input("Enter the ICAO code of the second airport: ").upper()

    connection = mysql.connector.connect(
        host='127.0.1.1',
        port=3306,
        database='table',
        user='root',
        password='0707',
        autocommit=True
    )

    try:
        cursor = connection.cursor()

        airport1_coords = coordinates(cursor, airport1_icao)
        airport2_coords = coordinates(cursor, airport2_icao)

        if airport1_coords is None or airport2_coords is None:
            print("One or both airports not found in the database.")
            return

        distance = calculate_distance(airport1_coords, airport2_coords)
        print(f"The distance between {airport1_icao} and {airport2_icao} is {distance:.3f} kilometers.")

    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()

#Exercise 9

import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change=None):
        if speed_change is not None:
            new_speed = self.current_speed + speed_change
        else:
            new_speed = self.current_speed + random.randint(-10, 15)

        self.current_speed = max(0, min(new_speed, self.max_speed))

    def drive(self, hours=1):
        distance_covered = self.current_speed * hours
        self.travelled_distance += distance_covered


def print_race_status(cars):
    print(
        f"{'Registration Number':<20} {'Max Speed (km/h)':<20} {'Current Speed (km/h)':<20} {'Distance Traveled (km)':<25}")
    for car in cars:
        print(f"{car.registration_number:<20} {car.max_speed:<20} {car.current_speed:<20} {car.travelled_distance:<25}")


if __name__ == "__main__":
    cars = [Car(registration_number=f"ABC-{i + 1}", max_speed=random.randint(100, 200)) for i in range(10)]

    special_car = Car(registration_number="ABC-123", max_speed=142)
    special_car.travelled_distance = 2000

    special_car.accelerate(60)
    print(f"---Special Car Before Driving---")
    print(f"Registration number: {special_car.registration_number}")
    print(f"Maximum speed: {special_car.max_speed} km/h")
    print(f"Current speed: {special_car.current_speed} km/h")
    print(f"Travelled distance: {special_car.travelled_distance} km")

    special_car.drive(1.5)
    print(f"Travelled distance after driving 1.5 hours: {special_car.travelled_distance} km")


    while any(car.travelled_distance < 10000 for car in cars):
        for car in cars:
            car.accelerate()
            car.drive()

    print_race_status(cars)


#Exercise 10
#1

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def floor(self, target_floor):
        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")
        else:
            print("The elevator's already on the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")
        else:
            print("The elevator's already on the bottom floor.")

def main():
    my_elevator = Elevator(1, 10)
    my_elevator.floor(7)
    my_elevator.floor(1)

if __name__ == "__main__":
    main()

#2
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")
        else:
            print("The elevator's already on the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")
        else:
            print("The elevator's already on the bottom floor.")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, destination_floor):
        if 0 <= elevator_num < len(self.elevators):
            print(f"Running elevator {elevator_num + 1} to floor {destination_floor}:")
            self.elevators[elevator_num].go_to_floor(destination_floor)

def main():
    my_building = Building(bottom_floor=1, top_floor=8, num_elevators=2)
    my_building.run_elevator(elevator_num=0, destination_floor=5)
    my_building.run_elevator(elevator_num=1, destination_floor=3)
if __name__ == "__main__":
    main()

#3
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

    def go_to_floor(self, target_floor):
        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")
        else:
            print("The elevator's already on the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")
        else:
            print("The elevator's already on the bottom floor.")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, destination_floor):
        if 0 <= elevator_num < len(self.elevators):
            print(f"Running elevator {elevator_num + 1} to floor {destination_floor}:")
            self.elevators[elevator_num].go_to_floor(destination_floor)

    def move(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.elevators[0].bottom_floor)

def main():
    my_building = Building(bottom_floor=1, top_floor=8, num_elevators=2)
    my_building.run_elevator(elevator_num=0, destination_floor=1)
    my_building.run_elevator(elevator_num=1, destination_floor=4)
    my_building.move()

    print("Fire alarm ! All elevators have been moved to the bottom floor")
if __name__ == "__main__":
    main()


#4

import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance_traveled = 0

    def accelerate(self):
        self.speed += random.randint(-10, 15)
        self.speed = max(0, min(self.speed, self.max_speed))

    def drive(self):
        self.distance_traveled += self.speed


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate()
            car.drive()

    def print_status(self):
        print(f"{'Registration Number':<20} {'Max Speed (km/h)':<20} {'Distance Traveled (km)':<25}")
        for car in self.cars:
            print(f"{car.registration_number:<20} {car.max_speed:<20} {car.distance_traveled:<25}")

    def race_finished(self):
        return any(car.distance_traveled >= self.distance for car in self.cars)


def main():
    cars = [Car(registration_number=f"ABC-{i+1}", max_speed=random.randint(100, 200)) for i in range(10)]
    grand_demolition_derby = Race(name="Grand Demolition Derby", distance=8000, cars=cars)

    hour_counter = 0
    while not grand_demolition_derby.race_finished():
        if hour_counter % 10 == 0:
            grand_demolition_derby.print_status()
        grand_demolition_derby.hour_passes()
        hour_counter += 1

    grand_demolition_derby.print_status()


if __name__ == "__main__":
    main()

'''
#Exercise 11
#1
class Publication:
    def __init__(self, name):
        self.name = name

    def information(self):
        print(f"Publication Name: {self.name}")


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        super().information()
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().information()
        print(f"Chief Editor: {self.chief_editor}")


Donald_Duck = Magazine(name="Donald Duck", chief_editor="Aki Hyyppä")
Compartment_No6  = Book(name="Compartment No. 6", author="Rosa Liksom", page_count=192)

Donald_Duck.print_information()
Compartment_No6.print_information()

#2
import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance_traveled = 0

    def accelerate(self):
        self.speed += random.randint(-10, 15)
        self.speed = max(0, min(self.speed, self.max_speed))

    def drive(self):
        self.distance_traveled += self.speed


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity  # in kWh


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume  # in liters


def main():
    electric_car = ElectricCar("ABC-15", 180, 52.5)  # 52.5 kWh battery
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)  # 32.3 liters tank

    electric_car.speed = 120  # km/h
    gasoline_car.speed = 100  # km/h

    for _ in range(3):
        electric_car.drive()
        gasoline_car.drive()

    # Print results
    print(f"Electric Car ({electric_car.registration_number}):")
    print(f"  Distance Traveled: {electric_car.distance_traveled} km")
    print(f"  Battery Capacity: {electric_car.battery_capacity} kWh\n")

    print(f"Gasoline Car ({gasoline_car.registration_number}):")
    print(f"  Distance Traveled: {gasoline_car.distance_traveled} km")
    print(f"  Tank Volume: {gasoline_car.tank_volume} liters")


if __name__ == "__main__":
    main()

#Exercise 12
#1
import requests

def joke():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url)
    data = response.json()

    if response.status_code == 200:
        text = data["value"]
        print(text)

if __name__ == "__main__":
    joke()

#2
import requests

def conversion(kelvin):
    return kelvin - 273.15

def weather(city):
    api_key = "933db7694960924d0fd1d4285703df2e"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        weather_description = data['weather'][0]['description']
        kelvin = data['main']['temp']
        celsius = conversion(kelvin)

        print(f"Weather in {city}: {weather_description}")
        print(f"Temperature: {celsius:.2f} °C")
    else:
        data = response.json() if response.text else None
        error_message = data.get('message') if data else 'Unknown Error'
        print(f"Error: {error_message}")

    if response.status_code != 200:
        print(f"Error: {response.text}")

if __name__ == "__main__":
    city = input("Enter the name of a municipality : ")
    weather(city)

#Exercise 13
#1
from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def prime(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

#2
from flask import Flask, jsonify
import mysql.connector
app = Flask(__name__)
connection = mysql.connector.connect(
    host='127.0.1.1',
    port=3306,
    database='table',
    user='root',
    password='0707',
    autocommit=True
)
@app.route('/')

def home():
    return jsonify({"message": "Welcome to the airports API"})
@app.route(rule='/airports/<icao>', methods=['GET'])
def get(icao):
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM airports WHERE ident = "{icao}"')
    airport_info = cursor.fetchone()

    if airport_info:
        response = {
            "ICAO": airport_info['ident'],
            "Name": airport_info['name'],
            "Location": airport_info['municipality']
        }
        return jsonify(response)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)



