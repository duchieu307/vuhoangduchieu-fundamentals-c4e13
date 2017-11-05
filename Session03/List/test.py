menu = ['com', 'chao', 'bun']
print(*menu, sep= " ")
print("*" * 20)
menu.remove("bun")
print(*menu, sep = ' ')
if "chan ga" in menu :
    menu.remove("chan ga")
else:
    print("chan ga not in list")
