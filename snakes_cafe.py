# turn menu section into objects with arrays as values
# When a user enters an item, the program should print an acknowledgment of their input


"""welcome_message = "Welcome to Snakes Cafe!\nPlease see our menu below.\n\nTo quit at any time, type 'quit'"
def print_message_with_astericks(message):
  message_str = str(message) 
  astericks = '*' * (len(message) + 2 )
  print(astericks)
  print(f'{message_str}')
  print(astericks)
def print_title_with_dashes(title):
  title = str(title)
  dashes = '-' * (len(title))
  print(title)
  print(dashes)
app_title = "Appetizer"
entree_title = "Entree"
dessert_title = "Dessert"
drink_title = "Drink"  
appetizers = "\n\nWing\nCookies\nSpring Rolls\n\n"
entrees = "Salmon\nSteak\nMeat Tornado\nA Literal Garden\n\n"
desserts ="Ice Cream\nCake\nPie\n\n"
drinks = "Coffee\nTea\nUnicorn Tears\n\n"
order_message = "What would you like to order?"

print_message_with_astericks(welcome_message) 

print_title_with_dashes(app_title)
print(appetizers)
print_title_with_dashes(entree_title)
print(entrees)
print_title_with_dashes(dessert_title)
print(desserts)
print_title_with_dashes(drink_title)
print(drinks)
print_message_with_astericks(order_message)
user_order = input("> ")
print(f'1 order of {user_order} has been added to your meal ')
user_order2 = input("> ")
if user_order == user_order2:
  print(f'2 orders of {user_order} has been added to your meal ')
else:
  print(f'1 order of {user_order2} has been added to your meal')"""


def print_message_with_asterisks(message):
    asterisks = '*' * (len(message) + 2)
    print(asterisks)
    print(f'{message}')
    print(asterisks)

def print_category_menu(title, items):
    print_message_with_asterisks(title)
    print(items)

def print_menu(menu):
    for category, (title, items) in menu.items():
        print_category_menu(title, items)

def acknowledge_order(item, count):
    if count == 1:
        print(f'1 order of {item} has been added to your meal')
    else:
        print(f'{count} orders of {item} have been added to your meal')

def main():
    welcome_message = "Welcome to Snakes Cafe!\nPlease see our menu below.\n\nTo quit at any time, type 'quit'"
    order_message = "What would you like to order?"

    menu = {
        'appetizers': ('Appetizer', "\n\nWing\nCookies\nSpring Rolls\n\n"),
        'entrees': ('Entree', "Salmon\nSteak\nMeat Tornado\nA Literal Garden\n\n"),
        'desserts': ('Dessert', "Ice Cream\nCake\nPie\n\n"),
        'drinks': ('Drink', "Coffee\nTea\nUnicorn Tears\n\n"),
    }

    print_message_with_asterisks(welcome_message)
    print_menu(menu)
    print_message_with_asterisks(order_message)

    user_orders = []
    while True:
        user_order = input("> ")

        if user_order.lower() == 'quit':
            break

        user_orders.append(user_order)
        acknowledge_order(user_order, len(user_orders))

if __name__ == "__main__":
    main()


