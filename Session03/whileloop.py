from random import randint
i = randint(0,100)
a = True
b = 0

while a and b < 8 :
    n = int(input("Nhap so n "))
    if n == i :
        print("Bingo")
        a = False

    elif n < i :
        print("Too small")
        b = b + 1
        print("You have ", 8 - b, "turns left")

    else:
        print("Too big")

        b = b + 1
        print("You have ", 8 - b, "turns left")
print("You lose")
