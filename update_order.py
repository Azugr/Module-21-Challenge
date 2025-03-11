def update_order(order, menu_selection, menu_items):
    """
    Updates the order based on the user's selection.

    Parameters:
    order (list): A list of dictionaries containing the menu item name, price, and quantity ordered.
    menu_selection (str): The customer's menu selection.
    menu_items (dictionary): A dictionary containing the menu items and their prices.

    Returns:
    order (list): A list of dictionaries containing the updated order.
    """
    # Check if the selection is a number
    if not menu_selection.isdigit():
        print(f"Invalid input: {menu_selection}. Please enter a valid number or item name.")
        return order

    menu_selection = int(menu_selection)

    # Check if the selection exists in the menu
    if str(menu_selection) not in menu_items:
        print(f"Invalid selection: {menu_selection}. Please enter a valid menu item.")
        return order

    # Retrieve the selected item from the menu
    selected_item = menu_items[str(menu_selection)]

    # Ask for quantity
    quantity = input(f"How many {selected_item['name']} would you like? ")

    # Validate quantity
    if not quantity.isdigit():
        print("Invalid quantity. Defaulting to 1.")
        quantity = 1
    else:
        quantity = int(quantity)

    # Add item to order
    order.append({"Item name": selected_item['name'], "Price": selected_item['price'], "Quantity": quantity})
    print(f"Added {quantity} {selected_item['name']}(s) to your order.")

    return order
