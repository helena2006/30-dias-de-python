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
if nota >= A:
    print("Congratulations! You got an A")
if nota >= B:
    print("You got a B")
if nota >= C:
    print("You got a C")
if nota >= D:
    print("You got a D")
if nota >= F:
    print("You failed")