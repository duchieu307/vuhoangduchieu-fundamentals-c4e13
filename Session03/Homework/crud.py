a = True
while a :
    n = input("Welcome to our shop, what do you want ?  ")
    menu = ['T-shirt, ', 'Sweater, ']
    if n.lower() == 'c':
        new = input("Enter your new item: ")
        menu.append(new)
        print('Our items: ', *menu, sep = '')
        a = False
    elif n.lower() == 'r':
        print('Our items: ', *menu, sep = '')
        a = False
    elif n.lower() == "u":
        number_items = len(menu)

        loop_update = True
        while loop_update  :
            update_position = int(input("Update position: "))
            if update_position <= number_items :
                update = input("Enter your new item: ")
                menu[update_position - 1] = update
                print('Our items: ', *menu, sep = ', ')
                loop_update = False
            else:
                print("Out of range")
                print("Try Again")
        a = False
    elif n.lower() == 'd' :
        number_items = len(menu)
        loop_delete = True
        while loop_delete :
            delete_position =  int(input("Delete position: "))
            if delete_position <= number_items:
                del menu[delete_position - 1]
                print('Our items: ', *menu, sep = '')
            else:
                print("Out of range")
                print("Try Again")
        a = False
    else:
        print("No Function")
        print("Try Again")
