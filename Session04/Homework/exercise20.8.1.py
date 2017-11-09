word = input("Enter your sentence ")
word = word.lower()
list_word = list(word)
list_word.sort()
word_dictionnary = {}

for letter in list_word:
    word_dictionnary[letter] = word_dictionnary.get(letter , 0) + 1 # gan gia tri moi vao tu dien
for keys in word_dictionnary.keys():
    if keys == ' ':
        pass
    else :
        print(keys, word_dictionnary[keys])
