import csv

def add_contact():
    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    phone = input("Enter phone: ").strip()

    with open("contacts.csv", "a", newline="") as file:
        fieldnames = ["name", "email", "phone"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # If file is empty, write header
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({"name": name, "email": email, "phone": phone})

    print("Contact added!")

def main():
    add_contact()

if __name__ == "__main__":
    main()
    
