# Initialize the inventory as an empty list
inventory = []

def add_item(name, price, quantity):
    item = (name, price, quantity)
    inventory.append(item)
    print(f"Added {quantity} of {name} at ${price} each to the inventory.")

def remove_item(name):
    global inventory
    inventory = [item for item in inventory if item[0] != name]
    print(f"Removed {name} from the inventory.")

def update_quantity(name, quantity):
    global inventory
    inventory = [(item[0], item[1], quantity) if item[0] == name else item for item in inventory]
    print(f"Updated {name} quantity to {quantity}.")

def display_inventory():
    print("Current Inventory:")
    for item in inventory:
        print(f"Name: {item[0]}, Price: ${item[1]}, Quantity: {item[2]}")

if __name__ == "__main__":
    add_item("Apple", 0.5, 100)
    add_item("Banana", 0.3, 150)
    display_inventory()
    update_quantity("Apple", 120)
    display_inventory()
    remove_item("Banana")
    display_inventory()
