word = input('Enter your word ')
characters = list(word)
from random import choice
n = len(characters)
i = 0
while i < n :
    random_characters = choice(characters)
    print(random_characters, end=' ')
    characters.remove(random_characters)
    i = i + 1
count = 0
loop = True
while loop and count < 8 :
    guess = input("Your answer ")
    if guess.lower() == word :
        print("Winner Winner Chicken Dinner")
        loop = False

    else :
        print("Guess Again")
        print("You have", 7 - count, "turns left")
        count = count + 1
print("You lose")
