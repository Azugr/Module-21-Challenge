def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.
    """
    order = []
    menu_items = get_menu_items_dict(menu)
    print("Welcome to the Generic Take Out Restaurant.\n")
    
    
    while True:
        print_menu_heading()
        for index, item in menu_items.items():
            print_menu_line(index, item["Item name"].split(" - ")[0], item["Item name"].split(" - ")[1], item["Price"])
        
        menu_selection = input("Type menu number: ")
        order = update_order(order, menu_selection, menu_items)
        
        keep_ordering = input("Would you like to keep ordering? (N) to quit: ")
        if keep_ordering.lower() == 'n':
            print("Thank you for your order.\n")
            prices_list = [item["Price"] * item["Quantity"] for item in order]
            order_total = round(sum(prices_list), 2)
            break
    
    return order, order_total


def update_order(order, menu_selection, menu_items):
    """
    Checks if the customer menu selection is valid, then updates the order.
    """
    if not menu_selection.isdigit() or int(menu_selection) not in menu_items:
        print(f"\n{menu_selection} was not a menu option.\n")
        return order
    
    menu_selection = int(menu_selection)
    item_name = menu_items[menu_selection]["Item name"]
    price = menu_items[menu_selection]["Price"]
    
    quantity = input(f"What quantity of {item_name} would you like? \n(This will default to 1 if number is not entered)\n")
    quantity = int(quantity) if quantity.isdigit() else 1
    
    order.append({"Item name": item_name, "Price": price, "Quantity": quantity})
    return order


def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.
    """
    for item in receipt:
        print_receipt_line(item["Item name"], item["Price"], item["Quantity"])


##################################################
#  STARTER CODE (DO NOT MODIFY BELOW THIS LINE)
##################################################

def print_receipt_line(item_name, price, quantity):
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")

def print_receipt_heading():
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")

def print_receipt_footer(total_price):
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")

def print_menu_heading():
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")

def print_menu_line(index, food_category, meal, price):
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    i_spaces = " " * (6 if index < 10 else 5)
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")

def get_menu_items_dict(menu):
    menu_items = {}
    i = 1
    for food_category, options in menu.items():
        for meal, price in options.items():
            menu_items[i] = {"Item name": f"{food_category} - {meal}", "Price": price}
            i += 1
    return menu_items

def get_menu_dictionary():
    meals = {
        "Burrito": {"Chicken": 4.49, "Beef": 5.49, "Vegetarian": 3.99},
        "Rice Bowl": {"Teriyaki Chicken": 9.99, "Sweet and Sour Pork": 8.99},
        "Sushi": {"California Roll": 7.49, "Spicy Tuna Roll": 8.49},
        "Noodles": {"Pad Thai": 6.99, "Lo Mein": 7.99, "Mee Goreng": 8.99},
        "Pizza": {"Cheese": 8.99, "Pepperoni": 10.99, "Vegetarian": 9.99},
        "Burger": {"Chicken": 7.49, "Beef": 8.49}
    }
    return meals

if __name__ == "__main__":
    meals = get_menu_dictionary()
    receipt, total_price = place_order(meals)
    print("This is what we are preparing for you.\n")
    print_receipt_heading()
    print_itemized_receipt(receipt)
    print_receipt_footer(total_price)
