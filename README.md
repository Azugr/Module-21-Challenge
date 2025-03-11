# Takeout Restaurant Order System

## Description
This Python-based terminal application allows customers to place orders at a takeout restaurant, view an itemized receipt, and check their total bill. It is designed to be accessible for individuals with hearing and vocal impairments by providing a fully text-based interface.

## Features
- Displays a restaurant menu with categorized items and prices.
- Allows users to select items, specify quantities, and update their order.
- Handles incorrect inputs gracefully, defaulting to sensible values.
- Provides an itemized receipt at the end with clear pricing and totals.
- Ensures accessibility with a simple and intuitive interface.

## Folder Structure
```
takeout_order_system/
│── main.py                # Main entry point of the program
│── menu.py                # Contains the restaurant menu
│── order.py               # Handles order placement and updates
│── receipt.py             # Generates and prints the receipt
│── utility.py             # Helper functions for input validation and formatting
│── README.md              # Project documentation
│── requirements.txt       # Dependencies (if any)
└── images/                # Screenshots of the application
```

## Installation
1. Clone this repository:
   ```bash
   git clone 
   cd takeout_order_system
   ```
2. Ensure you have Python installed (version 3.6 or higher).
3. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the program:
   ```bash
   python main.py
   ```
2. Follow the on-screen instructions to place an order.
3. View the itemized receipt at the end.

## Example
```
Welcome to the Generic Takeout Restaurant!

Menu:
1. Burrito - Chicken - $4.49
2. Burrito - Beef - $5.49
...
Enter the number of the item you want to order (or 'q' to quit): 1
How many Burrito - Chicken would you like? 2
...
Itemized Receipt:
--------------------------------------------------
Item Name                     Price     Quantity  
--------------------------------------------------
Burrito - Chicken             $4.49     2        
--------------------------------------------------
Total Price: $8.98
```

## License
This project is licensed under the MIT License.

## 🎥 Walkthrough Video
A walkthrough video is included in the submission. It covers:
[🔗 https://drive.google.com/file/d/1VryIqEdwrhgXbFb_e2sPVa81e4wFrOQW/view?usp=drive_link]()

## Author
María Azucena García Rodríguez - Developed for a Python terminal project challenge.

## Acknowledgments
- Instructor guidance from the Python course.
- Open-source resources for best practices.
