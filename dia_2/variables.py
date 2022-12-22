# Day 2: 30 Days of python programming
first_name = "Helena"
last_name = "Troncoso"
full_name = "Helena Troncoso"
country = "España"
city = "Jerez"
age = 16
year = 2022
is_married = False
is_true = True
is_light_on = True
a, b = 4, 8
print(country , city)

print(type(full_name))      #1
print(len(full_name))       #2
print(len(last_name))       #3

num_one = 5     #4
num_two = 4

total = num_one + num_two   #4i
print(total)

diff = num_two - num_one      #4ii
print(diff)

product = num_one * num_two     #4iii
print(product)

exp = pow(num_one , num_two)      #4iv
print(exp)

floor_division = num_one // num_two     #4v
print(floor_division)

division = num_one / num_two      #4vi
print(division)

remainder = num_two % num_one     #4vii
print(remainder)

r = 30      #5
pi = 3,14
diameter = r * 2
area_of_circle = pi * r      #i
circum_of_circle = pi * diameter        #ii

print(area_of_circle , circum_of_circle)

r = input('Cual es el radio: ')        #iii
print(f"El radio es {r}")

area_of_circle = pi * r
circum_of_circle = pi * diameter 

firt_name = input('Cual es tu nombre: ')        #6
print(f"Mi nombre es {first_name}")

last_name = input('Cual es tu primer apellido: ')
print(f"Mi primer apellido es {last_name}")

country = input('En qué país vives: ')
print(f"El país donde vivo {country}")

age = input('Cuántos años tienes: ')
print(f"Tengo {age} años")