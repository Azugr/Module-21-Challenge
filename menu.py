MENU = {
    "Burritos": [
        {"name": "Burrito - Chicken", "price": 4.49},
        {"name": "Burrito - Beef", "price": 5.49},
        {"name": "Burrito - Vegetarian", "price": 3.99}
    ],
    "Rice Bowls": [
        {"name": "Rice Bowl - Teriyaki Chicken", "price": 9.99},
        {"name": "Rice Bowl - Sweet and Sour Pork", "price": 8.99}
    ],
    "Sushi": [
        {"name": "Sushi - California Roll", "price": 7.49},
        {"name": "Sushi - Spicy Tuna Roll", "price": 8.49}
    ],
    "Noodles": [
        {"name": "Noodles - Pad Thai", "price": 6.99},
        {"name": "Noodles - Lo Mein", "price": 7.99},
        {"name": "Noodles - Mee Goreng", "price": 8.99}
    ],
    "Pizza": [
        {"name": "Pizza - Cheese", "price": 8.99},
        {"name": "Pizza - Pepperoni", "price": 10.99},
        {"name": "Pizza - Vegetarian", "price": 9.99}
    ],
    "Burgers": [
        {"name": "Burger - Chicken", "price": 7.49},
        {"name": "Burger - Beef", "price": 8.49}
    ]
}

def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items mapped to their numbers.
    """
    menu_items = {}
    item_number = 1

    for category, items in menu.items():
        for item in items:
            menu_items[str(item_number)] = item
            item_number += 1

    return menu_items


def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item Name                        | Price")
    print("-------|----------------------------------|-------")


def print_menu_line(index, food_category, meal, price):
    """
    Prints a formatted line of the menu.
    """
    print(f"{index:2} | {food_category} - {meal:30} | ${price:.2f}")

