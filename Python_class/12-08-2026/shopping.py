def add_product(cart):
    product_id = input("Enter product ID: ")

    if product_id in cart:
        print("Product already exists in the cart.")
        return

    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    cart[product_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    print("Product added successfully.")


def update_quantity(cart):
    product_id = input("Enter product ID: ")

    if product_id in cart:
        quantity = int(input("Enter new quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        cart[product_id]["quantity"] = quantity
        print("Quantity updated successfully.")
    else:
        print("Product not found.")


def remove_product(cart):
    product_id = input("Enter product ID: ")

    if product_id in cart:
        del cart[product_id]
        print("Product removed successfully.")
    else:
        print("Product not found.")


def search_product(cart):
    product_id = input("Enter product ID: ")

    if product_id in cart:
        product = cart[product_id]

        print("\nProduct Details")
        print("Product ID:", product_id)
        print("Product Name:", product["name"])
        print("Price:", product["price"])
        print("Quantity:", product["quantity"])
    else:
        print("Product not found.")


def display_cart(cart):
    if not cart:
        print("Cart is empty.")
        return

    print("\n--- Shopping Cart ---")

    for product_id, product in cart.items():
        subtotal = product["price"] * product["quantity"]

        print("\nProduct ID:", product_id)
        print("Product Name:", product["name"])
        print("Price: ₹", product["price"])
        print("Quantity:", product["quantity"])
        print("Subtotal: ₹", subtotal)


def calculate_total(cart):
    total = 0

    for product in cart.values():
        total += product["price"] * product["quantity"]

    return total


def display_bill(cart):
    total = calculate_total(cart)

    print("\n--- BILL ---")
    print("Total Bill: ₹", total)

    if total > 5000:
        discount = total * 0.10
        final_amount = total - discount

        print("Discount (10%): ₹", discount)
        print("Final Payable Amount: ₹", final_amount)
    else:
        print("Discount: ₹0")
        print("Final Payable Amount: ₹", total)


cart = {}

while True:

    print("\n========== SHOPPING CART ==========")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. Remove Product")
    print("4. Search Product")
    print("5. Display Cart")
    print("6. Calculate Total Bill")
    print("7. Apply Discount and Display Final Bill")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product(cart)

    elif choice == "2":
        update_quantity(cart)

    elif choice == "3":
        remove_product(cart)

    elif choice == "4":
        search_product(cart)

    elif choice == "5":
        display_cart(cart)

    elif choice == "6":
        total = calculate_total(cart)
        print("Total Bill: ₹", total)

    elif choice == "7":
        display_bill(cart)

    elif choice == "8":
        print("Thank you for using the Shopping Cart System.")
        break

    else:
        print("Invalid choice. Please try again.")
