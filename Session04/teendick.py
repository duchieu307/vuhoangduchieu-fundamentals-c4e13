teen_tudien ={
    "hc" : "hoc",
    "ng" : "nguoi",
    "wtf" : "what the fuck",
    "dm" : "dau ma",
    "cc" : "con ca",
}

loop = True
while loop :

    word = input('Enter your word: ')

    while loop :
        if word in teen_tudien :
            print(teen_tudien[word])
            break
        else:
            choice = input('Not found, do you want to contribute word? (Y/N) ?')
            if choice.upper() == "Y":
                update = input("Enter your mean")
                teen_tudien[word] = update
                print("Updated")
            elif choice.upper() == "N":
                print("ok fine")
                break
            else :
                print("Choose Again")
