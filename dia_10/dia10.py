#Level 1 - 1

cont = 0
while cont < 10:
    print(cont)
    cont = cont + 1


#Level 1 - 2

cont = 10
while cont > 0:
    print(cont)
    cont = cont - 1


#Level 1 - 3

for n in range (7):
    print("#" * n)


#Level 1 - 4

for x in range(1,4):
    for y in range(1,4):
        print("# "*8)


#Level 1 - 5

numbers = (0,1,2,3,4,5,6,7,8,9,10)
for number in numbers:
    if number == 3:
        continue
    print(f"{number} x {number} = ", number * number) if number != 10 else print("loop's end")


#Level 1 - 6

langs = ['Python', 'Numpy','Pandas','Django', 'Flask']
for l in langs:
    print(l)


#Level 1 - 7

cont = 0
while cont < 100:
    if(cont / 2 == 0):
        print(cont)
        cont = cont + 1
    else:
        continue


#Level 1 - 8




#Level 1 - 3

numbers = [0, 1, 2, 3, 4, 5, 6, 7]
for n in numbers:
    print("#" * n)


m = [[1 , 2] , [3 , 4]]
for n in range (7):
    print("#" * n)

