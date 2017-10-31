loop = True

while loop :
    from random import randint
    print(randint(0,100))
    numb = randint(0,100)
    if numb > 10:
        loop = False
        print(numb)
