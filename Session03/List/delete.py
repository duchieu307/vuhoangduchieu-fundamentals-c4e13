menu = ['chao', "my", "com", 'bun']
print("Here your menu", *menu, sep = ', ')
print('*' * 20)
n = input("what do you want to remove")
print(n)
if n in menu :
    menu.remove(n)
else :
    print(n, "not in list")
print('*' * 20)
print('Your menu is', *menu, sep = ', ')
