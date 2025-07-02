contacts = {}
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added successfully.")
def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("Contact not found.")
def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")
def display_contacts():
    if contacts:
        print("All contacts:")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")
    else:
        print("No contacts to display.")
while True:
    print("\nContact Book Menu")
    print("1. Add New Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        display_contacts()
    elif choice == '5':
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice. Please try again.")