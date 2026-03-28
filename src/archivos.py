# CSV persistence module
import csv

def save_csv(inventory_list, path, include_header=True):
    # Saves inventory to CSV with validation
    if not inventory_list:
        print("Inventory empty, nothing to save.")
        return
    try:
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            if include_header:
                writer.writerow(['name', 'price', 'quantity'])
            for p in inventory_list:
                writer.writerow([p['name'], p['price'], p['quantity']])
        print(f"Inventory saved to: {path}")
    except PermissionError:
        print("Permission error to write file.")
    except Exception as e:
        print(f"Save error: {e}")

def load_csv(path, inventory_list):
    # Loads CSV with validations, overwrite or merge
    try:
        with open(path, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
        if not rows or rows[0] != ['name', 'price', 'quantity']:
            print("Invalid header.")
            return "Header error."
        del rows[0]
        new_products = []
        errors = 0
        for row in rows:
            if len(row) != 3:
                errors += 1
                continue
            try:
                name = row[0]
                price = float(row[1])
                quantity = int(row[2])
                if price < 0 or quantity < 0:
                    errors += 1
                    continue
                new_products.append({"name": name, "price": price, "quantity": quantity})
            except ValueError:
                errors += 1
        print(f"Loaded {len(new_products)} valid products, {errors} invalid rows skipped.")
        action = input("Overwrite (O) or Merge (M)? ").upper().strip()
        if action == 'O':
            inventory_list[:] = new_products
            print(f"Overwritten with {len(new_products)} products.")
        else:
            for new_p in new_products:
                for existing in inventory_list:
                    if existing['name'].lower() == new_p['name'].lower():
                        existing['quantity'] += new_p['quantity']
                        if existing['price'] != new_p['price']:
                            existing['price'] = new_p['price']
                        print(f"Merged/updated {new_p['name']}.")
                        break
                else:
                    inventory_list.append(new_p)
            print(f"Merged {len(new_products)} products.")
        return "Load complete."
    except FileNotFoundError:
        print("File not found.")
        return "File error."
    except UnicodeDecodeError:
        print("Encoding error in file.")
        return "Encoding error."
    except Exception as e:
        print(f"Generic error: {e}")
        return "Error."

