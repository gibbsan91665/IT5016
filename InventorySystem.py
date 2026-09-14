# inventory_system.py
# Inventory Management System Prototype

# Global dictionary to store inventory items
# Key: Item ID, Value: Dictionary of item details
inventory = {}

# Global counter for auto-generating unique Item IDs starting at 1000
item_id_counter = 1000

# Task 1: Add Inventory Item
def add_inventory_item():
      """Prompts the user for item details, auto-generates an Item ID starting at 1000,
      stores the item in the global inventory dictionary, and returns all details.
      """
      global item_id_counter
      print("\n--- Add New Inventory Item ---")
      item_name = input("Enter Item Name: ").strip()

      # Input validation for quantity
      while True:
        try:
          quantity = int(input("Enter Quantity: "))
          if quantity < 0:
            print("Quantity cannot be negative. Try again.")
            continue
          break
        except ValueError:
          print("Invalid input! Please enter a whole number for quantity.")

    # Input validation for price
      while True:
        try:
          price = float(input("Enter Price per Item: \$"))
          if price < 0:
            print("Price cannot be negative. Try again.")
            continue
          break
        except ValueError:
          print("Invalid input! Please enter a valid number for price.")

    # Assign generated ID and increment counter
    item_id = item_id_counter
    item_id_counter += 1

    # Store in the global inventory
    inventory[item_id] = {
        "name": item_name,
        "quantity": quantity,
        "price": price,
    }

    print(
        f"\n[Success] Item added successfully! Generated Item ID: {item_id}\n"
    )
    return item_id, item_name, quantity, price

# Task 2: Calculate Total Value
def calculate_total_value():
  """Calls add_inventory_item() from Task 1, computes the total value
  (Quantity * Price), displays a user-friendly message, and returns the total.
  """
  # Call Task 1 function
  item_id, item_name, quantity, price = add_inventory_item()

  # Calculate total value
  total_val = quantity * price

  # Display user-friendly message
  print("--- Total Value Calculation ---")
    print(f"Item Name         : {item_name}")
    print(f"Item ID           : {item_id}")
    print(f"Quantity          : {quantity}")
    print(f"Price per Item    : \${price:.2f}")
    print(f"Total Stock Value : \${total_val:,.2f}")
    print("-" * 31)

    return total_val

# Task 3
def update_inventory(item_id):
  """Takes an Item ID, checks if it exists, and allows updating the

  Quantity and Price per Item. Returns an error message if not found.
  """
  # Check if item exists in inventory
  if item_id not in inventory:
    message = f"Error: Item with ID {item_id} was not found in inventory."
    print(f"\n{message}\n")
    return message

  print(f"\n--- Update Item ID {item_id} ({inventory[item_id]['name']}) ---")

  # Get new quantity
  while True:
    try:
      new_qty = int(
        input(
          f"Enter new quantity (current: {inventory[item_id]['quantity']}): "
        )
      )
      if new_qty < 0:
        print("Quantity cannot be negative. Try again.")
        continue
      break
    except ValueError:
      print("Invalid input! Please enter a whole number for quantity.")
  # Get new price
  while True:
    try:
      new_price = float(
        input(
          f"Enter new price per item (current: \${inventory[item_id]['price']:.2f}): "
        )
      )
      if new_price < 0:
        print("Price cannot be negative. Try again.")
        continue
      break
    except ValueError:
      print("Invalid input! Please enter a valid number for price.")

  #Update the record
  inventory[item_id]["quantity"] = new_qty
  inventory[item_id]["price"] = new_price

  print(f"\n[Success] Item ID {item_id} updated successfully!\n")
  return inventory[item_id]

# Task 4: Display Inventory Item
def display_inventory_item(item_id):
  """Displays formatted details of an inventory item including
  Item Name, Item ID, Quantity, and Total Value.
  """
  if item_id not in inventory:
    print(
        f"\nError: Item with ID {item_id} does not exist in inventory.\n"
    )
    return
  item = inventory[item_id]
  total_val = item["quantity"] * item["price"]

  # Formatted display
  print("\n" + "=" * 35)
  print(f"{'INVENTORY ITEM DETAILS':^35}")
  print("=" * 35)
  print(f"  Item ID     : {item_id}")
  print(f"  Item Name   : {item['name']}")
  print(f"  Quantity    : {item['quantity']}")
  print(f"  Unit Price  : \${item['price']:.2f}")
  print(f"  Total Value : \${total_val:,.2f}")
  print("=" * 35 + "\n")

# Interactive Menu: To test all tasks
if __name__ == "__main__":
  while True:
    print("========================================")
    print("  RETAIL INVENTORY MANAGEMENT PROTOTYPE ")
    print("========================================")
    print("1. Add Item (Task 1)")
    print("2. Add Item & Calculate Total Value (Task 2)")
    print("3. Update Inventory Item (Task 3)")
    print("4. Display Inventory Item (Task 4)")
    print("5. Exit")
    print("========================================")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
      add_inventory_item()
    elif choice == "2":
      calculate_total_value()
    elif choice == "3":
      try:
        item_id = int(input("Enter Item ID to update: "))
        update_inventory(item_id)
      except ValueError:
        print("Invalid input. Item ID must be a number.\n")
    elif choice == "4":
      try:
        item_id = int(input("Enter Item ID to display: "))
        display_inventory_item(item_id)
      except ValueError:
        print("Invalid input. Item ID must be a number.\n")
    elif choice == "5":
      print("\n Thank you for using the Inventory Management System")
      print("Exiting the program. Goodbye!")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 5.\n")
