def print_itemized_receipt(order, total_price):
    print("\nItemized Receipt:")
    print("--------------------------------------------------")
    print(f"{'Item Name':<30}{'Price':<10}{'Quantity':<10}")
    print("--------------------------------------------------")
    
    for item in order:
        item_name = item['name']
        item_price = item['price']
        item_quantity = item['quantity']
        
        # Send the extracted values to the print_receipt_line function
        print_receipt_line(item_name, item_price, item_quantity)
    
    print("--------------------------------------------------")
    print(f"Total Price: ${total_price:.2f}")

def print_receipt_line(name, price, quantity):
    print(f"{name:<30}${price:<10.2f}{quantity:<10}")
