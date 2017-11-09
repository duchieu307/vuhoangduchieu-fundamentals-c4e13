inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['pocket'] = 'key'
print(inventory['pocket'])
print()
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(inventory['pocket'])
print()
inventory['backpack'].remove('dagger')

print(inventory['backpack'])
print()
inventory['gold'] = inventory['gold'] + 50
print(inventory['gold'])
