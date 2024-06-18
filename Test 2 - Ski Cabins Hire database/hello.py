print('Welcome to Party Phone Orders')

menu_items = {
    1: {"name": "Bouncy Castle", "price": 5},
    2: {"name": "Balloon Kit", "price": 5},
    3: {"name": "Party Hats", "price": 5},
    4: {"name": "Tables", "price": 7},
    5: {"name": "Chairs", "price": 7},
    6: {"name": "Banners", "price": 7}
}

def display_menu():
    print("Menu:")
    for item_id, item in menu_items.items():
        print(f"{item_id}. {item['name']} - ${item['price']}")

def get_order_type():
    while True:
        order_type = input("Is this order for pickup or delivery? (P/D): ")
        if order_type.lower() == "p":
            return "pickup"
        elif order_type.lower() == "d":
            return "delivery"
        else:
            print("Invalid input. Please try again.")

def get_customer_name():
    return input("Enter customer name: ")

def get_address_and_phone_number():
    address = input("Enter customer address: ")
    phone_number = input("Enter customer phone number: ")
    return address, phone_number

def get_order_items():
    order_items = []
    while True:
        display_menu()
        item_id = int(input("Enter the number of the item to order (or 0 to finish): "))
        if item_id == 0:
            break
        elif item_id in menu_items:
            order_items.append(menu_items[item_id])
        else:
            print("Invalid item number. Please try again.")
    return order_items

def calculate_total_cost(order_items, delivery_charge=0):
    total_cost = sum(item["price"] for item in order_items) + delivery_charge
    return total_cost

def display_order(order_items, customer_name, address=None, phone_number=None, delivery_charge=0):
    print("Order Summary:")
    print(f"Customer Name: {customer_name}")
    if address and phone_number:
        print(f"Address: {address}")
        print(f"Phone Number: {phone_number}")
    print(f"Items Ordered: {order_items}")
    for item in order_items:
        print(f"  {item['name']} - ${item['price']}")
    print(f"Delivery: {delivery_charge} ")
    print(f"Total Cost: ${calculate_total_cost(order_items, delivery_charge)}")

def main():
    while True:
        order_type = get_order_type()
        customer_name = get_customer_name()
        if order_type == "delivery":
            address, phone_number = get_address_and_phone_number()
            delivery_charge = 10
        else:
            address = phone_number = None
            delivery_charge = 0
        order_items = get_order_items()
        display_order(order_items, customer_name, address, phone_number, delivery_charge)
        response = input("Would you like to place another order? (y/n): ")
        if response.lower()!= "y":
            break

if __name__ == "__main__":
    main()