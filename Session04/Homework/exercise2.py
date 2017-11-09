princess = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}
for keys, values in stock.items():
    print(keys, values, sep = ': ')
    print('price', princess[keys], sep = ': ')
total = 0
for keys, values in princess.items():
    price = values * stock[keys]
    total = total + price
print(total)
