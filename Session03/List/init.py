# menu = ['chan ga', 'dui ga', 'canh ga']
# print(*menu, sep=', ')
# print('* ' * 10)
# menu.append('co ga')
# print(*menu, sep=', ')
menu = ['pizza', 'hamburger', 'sandwich']
# for item in menu:
#     print(item.upper())
# for index, item in enumerate(menu):
#     print(index + 1,". ", item, sep='')
#
print("Here your menu")
for index, item in enumerate(menu):
    print(enumerate(menu))
    print(index + 1,".", item)
print('*' * 20)
n = int(input('Position you want to update ? '))
m = input('Your replacing favorite')
menu[n-1] = m     #update
print(*menu, sep=' ')
