# 📦 2. Product Inventory
# products = {
#     "P001": {"name": "Laptop", "price": 4500, "stock": 5},
#     "P002": {"name": "Mouse", "price": 500, "stock": 15},
# }

# - Add new products
# - List all
# - Check stock before selling

# Define show_menu() function 
def show_menu():
    print("1. Add new products")
    print("2. List all products")
    print("3. Check stock of a product before selling")

# Define add_product() function
def add_product(new_product, products):
    key = "P00" + str(len(products) + 1)
    products[key] = new_product
    view_products(products)

# Define view_products() function
def view_products(products):
    if len(products):
        for key, value in products.items():
            print(f"{key} ==> {value}")
    else: print("The products record is empty")

# Define check_stock() function
def check_stock(product_key, products):
    if len(products):
        if products[product_key]["stock"] > 0:
            print(f"\nProduct is available. You can purchase maximum of {products[product_key]["stock"]}\n")
        else: print("Sorry! Product is out of stock")
    else: print("There is no product in stock")
    view_products(products)

# Define main() function
def main():

    show_menu()

    products = {}

    while True:
        user_choice = input("Enter digit corresponding to what you want to do: ")

        if user_choice == "1":
            new_product = {}
            user_input = input("Enter the new product e.g name, price, stock: ")
            user_input = user_input.split(",")
            new_product.update({"name" : user_input[0], "price" : user_input[1], "stock" : int(user_input[2])})
            add_product(new_product, products)
        elif user_choice == "2":
            view_products(products)
        elif user_choice == "3":
            key = input("Enter the product key: ")
            check_stock(key, products)
        else: 
            break


if __name__ == "__main__":
    main()