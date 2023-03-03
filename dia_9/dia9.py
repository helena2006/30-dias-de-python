a = int(input("Inserte su edad: "))     #Level 1 - 1
if a >= 18:
    print("Usted tiene edad para conducir")
if a < 18:
    print("Usted no tiene edad suficiente para conducir")

b = int(input("Who is older?"))     #Level 1 - 2
my_age = 16
if b < my_age:
    print(f"Im {my_age - b} years older than you")
if b > my_age:
    print(f"You are {b - my_age} years older than me")
if b == my_age:
    print("We are the same age")

number_one = int(input("Enter a number: "))     #Level 1 - 3
number_two = int(input("Enter a second number:"))
if number_one > number_two:
    print(f"{number_one} is greater than {number_two}")
if number_two < number_one:
    print(f"{number_two} is less than {number_one}")
if number_one == number_two:
    print(f"{number_one} is equal to {number_two}")

nota = int(input("¿Cual es tu nota?:"))     #Level 2 - 1
A = 90, 100
B = 70, 89
C = 60, 69
D = 50, 59
F = 0, 49
if nota >= 90 and nota <= 100:
    print("Congratulations! You got an A")
elif nota >=70 and nota <= 89:
    print("You got a B")
elif nota >= 60 and nota <=69:
    print("You got a C")
elif nota >= 50 and nota <= 59:
    print("You got a D")
elif nota >= 0 and nota <= 49:
    print("You failed")

season = str(input("¿En que mes estamos?  "))     #Level 2 - 2
season_capitalized=season.capitalize()     
Autumn = "September, October or November"
Winter = "December, January or February"
Spring = "March, April or May"
Summer = "June, July or August"

if season_capitalized == "September" or season_capitalized == "October" or season_capitalized == "November":
    print("It's Autumn")
elif season_capitalized == "December" or season_capitalized == "January" or season_capitalized == "February":
    print("It's winter")
elif season_capitalized == "March" or season_capitalized == "April" or season_capitalized == "May":
    print("It's spring")
elif season_capitalized == "June" or season_capitalized == "July" or season_capitalized == "August":
    print("It's summer")


fruits = ["banana", "orange", "mango", "lemon"]     #Level 2 - 3
new_fruit = str(input("Dime una fruta:  "))
season_capitalized=season.capitalize()

if new_fruit in fruits:
    print("La fruta ya esta en la lista")
else:
    fruits.append(new_fruit)
    print(fruits)