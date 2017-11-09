word = input("Enter your sentence ")
list_word = list(word)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
 ]
print(alphabet)
for i in range(len(list_word)):
    count = 0
    for index, character in enumerate(list_word):
        if list_word[index] in alphabet:
            count = count + 1

    print(list_word[index], count)
    del list_word[index]
