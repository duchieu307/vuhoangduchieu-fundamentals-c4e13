hangman = [
"""
  ________
  |      o
  |     -|-
  |     (`)
__|__
"""
,
"""
  ________
  |      o
  |     -|-
  |     (`
__|__
"""
,
"""
  ________
  |      o
  |     -|-
  |
__|__
"""
,
"""
  ________
  |      o
  |     -|
  |
__|__
"""
,
"""
  ________
  |      o
  |      |
  |
__|__
"""
,
"""
  ________
  |      o
  |
  |
__|__
"""
,
"""
  ________
  |
  |
  |
__|__
"""
,
]

from random import choice
words_list = ['drink', 'vodka', "play",'dota']
word = choice(words_list)
word_characters = list(word)

n = len(word_characters)
count = 7

space = '_' * n
space_list = list(space)
SPACE = list(space)

i = 0
loop = True
while loop and i < count :

    guess = input("Let`s guess ")
    guess = guess.lower()

    if guess in word_characters:
        for index, character in enumerate(word_characters):
            if character == guess:
                space_list[index] = guess
                word_characters[index] = '_'
                print(*space_list, sep = ' ')
                i = i + 1

                if word_characters == SPACE :
                    print('Winner Winner Chicken Dinner')
                    loop = False
# thay dau _ bang chu dung
    else:
        print(hangman[6 - i])

        i = i + 1
        if i == 7 :
            print("You only have one job :(")
