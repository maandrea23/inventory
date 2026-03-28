# Services for inventory CRUD and stats
from inventory import inventory as input_validator

def add_product(inventory_list, name, price, quantity):
    # Adds a product to the inventory
    product = {"name": name, "price": price, "quantity": quantity}
    inventory_list.append(product)
    print(f"Product '{name}' added successfully.")

def show_inventory(inventory_list):
    # Shows inventory or indicates if empty
    if not inventory_list:
        print("Inventory is empty.")
        return
    print("\\n--- INVENTORY ---")
    for p in inventory_list:
        print(f"Product: {p['name']} | Price: {p['price']} | Quantity: {p['quantity']}")
    print("-----------------")

def search_product(inventory_list, name):
    # Searches for product by name (case insensitive), returns dict or None
    for p in inventory_list:
        if p['name'].lower() == name.lower():
            print(f"Found: {p['name']} | Price: {p['price']} | Quantity: {p['quantity']}")
            return p
    print("Product not found.")
    return None

def update_product(inventory_list, name, new_price=None, new_quantity=None):
    # Updates price and/or quantity of the product
    p = search_product(inventory_list, name)
    if p:
        if new_price is not None:
            p['price'] = new_price
        if new_quantity is not None:
            p['quantity'] = new_quantity
        print(f"Product '{name}' updated.")

def delete_product(inventory_list, name):
    # Deletes product by name
    p = search_product(inventory_list, name)
    if p:
        inventory_list.remove(p)
        print(f"Product '{name}' deleted.")

def calculate_statistics(inventory_list):
    # Calculates and shows advanced stats. Returns dict
    if not inventory_list:
        print("No products for statistics.")
        return {}
    subtotal = lambda p: p["price"] * p["quantity"]
    total_units = sum(p["quantity"] for p in inventory_list)
    total_value = sum(subtotal(p) for p in inventory_list)
    most_expensive = max(inventory_list, key=lambda p: p["price"])
    highest_stock = max(inventory_list, key=lambda p: p["quantity"])
    stats = {
        'total_units': total_units,
        'total_value': total_value,
        'most_expensive': (most_expensive['name'], most_expensive['price']),
        'highest_stock': (highest_stock['name'], highest_stock['quantity'])
    }
    print(f"\\n--- STATISTICS ---")
    print(f"Total units: {total_units}")
    print(f"Total value: {total_value}")
    print(f"Most expensive: {most_expensive['name']} (${most_expensive['price']})")
    print(f"Highest stock: {highest_stock['name']} ({highest_stock['quantity']})")
    print("--------------------")
    return stats

def choose(option, inventory_list):
    # Processes menu option with validations
    try:
        if option == 1:
            name = input_validator(str, "Product name: ", "Name cannot be empty.")
            price = input_validator(float, "Price: ", "Price must be >0.")
            quantity = input_validator(int, "Quantity: ", "Quantity must be >0.")
            add_product(inventory_list, name, price, quantity)
        elif option == 2:
            show_inventory(inventory_list)
        elif option == 3:
            name = input("Name to search: ").strip()
            search_product(inventory_list, name)
        elif option == 4:
            name = input("Name to update: ").strip()
            p_str = input("New price (enter to skip): ")
            q_str = input("New quantity (enter to skip): ")
            new_p = float(p_str) if p_str.strip() else None
            new_q = int(q_str) if q_str.strip() else None
            update_product(inventory_list, name, new_p, new_q)
        elif option == 5:
            name = input("Name to delete: ").strip()
            delete_product(inventory_list, name)
        elif option == 6:
            calculate_statistics(inventory_list)
        elif option == 7:
            path = input("CSV save path (e.g. inventory.csv): ").strip()
            from archivos import save_csv
            save_csv(inventory_list, path)
        elif option == 8:
            path = input("CSV load path: ").strip()
            from archivos import load_csv
            load_csv(path, inventory_list)
        elif option == 9:
            print("Thank you for using the system. Goodbye!")
        else:
            print("Invalid option.")
    except KeyboardInterrupt:
        print("\\nExiting...")
    except Exception as e:
        print(f"Operation error: {str(e)}. Back to menu.")

