import requests

BASE_URL = "http://127.0.0.1:5000"


# VIEW ALL ITEMS

def view_inventory():
    try:
        response = requests.get(f"{BASE_URL}/inventory")
        print(response.json())
    except:
        print("Error: Could not fetch inventory")



# VIEW SINGLE ITEM

def view_item():
    item_id = input("Enter item ID: ")

    try:
        response = requests.get(f"{BASE_URL}/inventory/{item_id}")
        print(response.json())
    except:
        print("Error fetching item")


# ADD ITEM

def add_item():
    print("\nEnter product details:")

    product_name = input("Product name: ")
    brand = input("Brand: ")
    price = input("Price: ")
    stock = input("Stock: ")

    data = {
        "status": 1,
        "product": {
            "product_name": product_name,
            "brands": brand,
            "ingredients_text": "N/A",
            "categories": "N/A",
            "quantity": "N/A"
        },
        "price": int(price),
        "stock": int(stock)
    }

    try:
        response = requests.post(f"{BASE_URL}/inventory", json=data)
        print(response.json())
    except:
        print("Error adding item")


# UPDATE ITEM

def update_item():
    item_id = input("Enter item ID to update: ")

    price = input("New price (leave blank to skip): ")
    stock = input("New stock (leave blank to skip): ")

    data = {}

    if price:
        data["price"] = int(price)
    if stock:
        data["stock"] = int(stock)

    try:
        response = requests.patch(f"{BASE_URL}/inventory/{item_id}", json=data)
        print(response.json())
    except:
        print("Error updating item")



# DELETE ITEM

def delete_item():
    item_id = input("Enter item ID to delete: ")

    try:
        response = requests.delete(f"{BASE_URL}/inventory/{item_id}")
        print(response.json())
    except:
        print("Error deleting item")



# SEARCH OPENFOODFACTS

def search_api():
    query = input("Enter barcode or product name: ")

    # Try barcode first
    try:
        response = requests.get(f"{BASE_URL}/search?barcode={query}")
        print(response.json())
    except:
        print("Error searching API")



# MENU

def menu():
    while True:
        print("\n============================")
        print(" INVENTORY MANAGEMENT SYSTEM")
        print("============================")
        print("1. View Inventory")
        print("2. View Item")
        print("3. Add Item")
        print("4. Update Item")
        print("5. Delete Item")
        print("6. Search Product (OpenFoodFacts)")
        print("7. Exit")

        choice = input("\nChoose option: ")

        if choice == "1":
            view_inventory()
        elif choice == "2":
            view_item()
        elif choice == "3":
            add_item()
        elif choice == "4":
            update_item()
        elif choice == "5":
            delete_item()
        elif choice == "6":
            search_api()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# RUN PROGRAM

if __name__ == "__main__":
    menu()