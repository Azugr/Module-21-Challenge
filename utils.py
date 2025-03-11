def place_order(menu):
    order = []
    total_price = 0

    while True:
        print("\n=========== MENU ===========\n")
        all_items = {}
        item_number = 1

        for category, items in menu.items():
            print(f"\n--- {category} ---\n")
            for item in items:
                formatted_name = item['name'].lower().replace(" ", "-")
                print(f"{item_number:<3} {item['name']:<30} ${item['price']:.2f}")
                all_items[str(item_number)] = item
                all_items[formatted_name] = item  
                all_items[item['name'].lower()] = item  
                item_number += 1
            print()  

        item_choices = input("\nEnter item numbers or names separated by commas (e.g., 1,4,pizza) or 'q' to quit: ").strip()
        if item_choices.lower() == 'q':
            break

        selected_items = [choice.strip().lower().replace(" ", "-") for choice in item_choices.split(",")]
        
        for item_choice in selected_items:
            if item_choice not in all_items:
                print(f"Invalid input: {item_choice}. Please enter a valid number or item name.")
                continue
            
            selected_item = all_items[item_choice]
            quantity = input(f"How many {selected_item['name']} would you like? ")

            if not quantity.isdigit():
                print("Invalid quantity. Defaulting to 1.")
                quantity = 1
            else:
                quantity = int(quantity)

            order.append({"name": selected_item['name'], "price": selected_item['price'], "quantity": quantity})
            print(f"Added {quantity} {selected_item['name']}(s) to your order.")
        
        continue_ordering = input("\nWould you like to continue ordering? (y/n): ").strip().lower()
        if continue_ordering == 'n':
            break

    total_price = round(sum(item['price'] * item['quantity'] for item in order), 2)
    return order, total_price