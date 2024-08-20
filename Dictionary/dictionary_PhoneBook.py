# Initialize the contact book as an empty dictionary
contact_book = {}

def add_contact(name, phone, email):
    contact_book[name] = {
        'phone': phone,
        'email': email
    }
    print(f"Added contact: {name}")

def remove_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"Removed contact: {name}")
    else:
        print(f"Contact '{name}' not found in the contact book.")

def update_contact(name, phone=None, email=None):
    if name in contact_book:
        if phone:
            contact_book[name]['phone'] = phone
        if email:
            contact_book[name]['email'] = email
        print(f"Updated contact: {name}")
    else:
        print(f"Contact '{name}' not found in the contact book.")

def display_contacts():
    if not contact_book:
        print("The contact book is empty.")
    else:
        print("Contact Book:")
        for name, details in contact_book.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Add contact")
        print("2. Remove contact")
        print("3. Update contact")
        print("4. Display contacts")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            name = input("Enter the name: ").strip()
            phone = input("Enter the phone number: ").strip()
            email = input("Enter the email: ").strip()
            add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter the name of the contact to remove: ").strip()
            remove_contact(name)
        elif choice == '3':
            name = input("Enter the name of the contact to update: ").strip()
            phone = input("Enter the new phone number (leave blank to keep current): ").strip()
            email = input("Enter the new email (leave blank to keep current): ").strip()
            update_contact(name, phone if phone else None, email if email else None)
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            print("Exiting the contact book application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")