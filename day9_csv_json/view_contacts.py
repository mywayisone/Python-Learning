import csv

def view_contacts():
    try:
        with open("contacts.csv", "r") as file:
            reader = csv.DictReader(file)
            for i, contact in enumerate(reader, start=1):
                print(f"{i}. {contact['name']} - {contact['email']} - {contact['phone']}")
    except FileNotFoundError:
        print("No contacts found.")

def main():
    view_contacts()

if __name__ == "__main__":
    main()