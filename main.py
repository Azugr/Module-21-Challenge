from menu import MENU
from order import place_order
from receipt import print_itemized_receipt

def main():
    print("Welcome to the Generic Takeout Restaurant!")
    order, total_price = place_order(MENU)
    print_itemized_receipt(order, total_price)

if __name__ == "__main__":
    main()
