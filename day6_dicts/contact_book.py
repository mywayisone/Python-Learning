# 🛠️ Mini Project: Contact Book
# Features:
# - Add new contact (name, phone)
# - View all contacts
# - Search contact by name
# - Delete contact
# - Exit

# Show all menu
def show_menu():
    print("1. Add new contact (name, phone): ")
    print("2. View contacts: ")
    print("3. Search contact by name: ")
    print("4. Delete Contact: ")
    print("5. Exit: ")


# Define add_contact() function
def add_contact(new_contact, dict_of_contacts):
    key ="00" + str(len(dict_of_contacts.keys()) + 1)
    dict_of_contacts[key] = new_contact
    view_contacts(dict_of_contacts)


# Define view_contact() function
def view_contacts(dict_of_contacts):
    for key, value in dict_of_contacts.items():
        print(f"{key} ==> {value}")


# Define search_contact() function
def search_contact(name, dict_of_contacts):
    contacts = {}
    # Loop through the contact dictionary
    for key in dict_of_contacts:
        # check if the search exist in the contact name
        if name in dict_of_contacts[key]["name"]:
            # update the contacts variable if it exist
            contacts.update({key : dict_of_contacts[key]})
    if (len(contacts) > 0):
        print("Result of the search:\n")
        # Loop through if record is found through the search
        for key, value in contacts.items():
            print(f"{key} ==> {value}")
    else: print("No contact found")



# Define delete_contact() function
def delete_contact(key, dict_of_contacts):
    del dict_of_contacts[key]
    view_contacts(dict_of_contacts)

# Define the main() function
def main():

    show_menu()

    contacts = {}
    
    while True:
        user_choice = input("Enter digit corresponding to what you want to do: ")

        if user_choice == "1":
            new_contact = {}
            user_input = input("Enter the new contact e.g kunle, 08060505050: ")
            user_input = user_input.split(",")
            print(user_input)
            new_contact.update({"name" : user_input[0], "phone" : user_input[1]})
            add_contact(new_contact, contacts)
        elif user_choice == "2":
            if len(contacts.keys()):
                view_contacts(contacts)
            else: print("contact dictionary is empty")
        elif user_choice == "3":
            name = input("Enter the name: ")
            if len(contacts.keys()):
                search_contact(name, contacts)
            else: print("contact dictionary is empty")
        elif user_choice == "4":
            key = input("Enter the contact key: ")
            delete_contact(key, contacts)
        else:
            break

if __name__ == "__main__":
    main()

    

