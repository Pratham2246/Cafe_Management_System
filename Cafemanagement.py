# Expanded Menu dictionary
menu = {
    'Tea': 10,
    'Coffee': 20,
    'Pasta': 60,
    'Burger': 70,
    'Pizza': 80,
    'Sandwich': 80,
    'Dosa': 100,
    'Idli': 30,
    'Vada': 25,
    'Samosa': 15,
    'Paneer Butter Masala': 120,
    'Chole Bhature': 90,
    'Fried Rice': 70,
    'Noodles': 60,
    'Ice Cream': 50,
    'Cold Drink': 25,
    'Momos': 40,
    'French Fries': 35
}

print("Welcome to Pratham Restaurant!\n")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")
print("\n")

# Initialize order
order_total = 0
ordered_items = []

while True:
    item = input("Enter the name of the item you want to order (or type 'done' to finish): ").title()
    
    if item == 'Done':
        break
    
    if item in menu:
        order_total += menu[item]
        ordered_items.append(item)
        print(f"✅ {item} added to your order. Current total: Rs{order_total}\n")
    else:
        print(f"❌ Sorry, {item} is not available in our restaurant.\n")

# Show final bill
if ordered_items:
    print("\n--- Your Final Bill ---")
    for i in ordered_items:
        print(f"{i}: Rs{menu[i]}")
    print(f"Total Amount to Pay: Rs{order_total}")
    print("----------------------")
else:
    print("No items were ordered. Thank you for visiting!")
