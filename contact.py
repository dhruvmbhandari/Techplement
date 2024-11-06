import json
import os

# File path for storing contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return {}
    with open(CONTACTS_FILE, 'r') as f:
        return json.load(f)

# Save contacts to fil
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return
    
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    # Data validation for phone and email
    if not phone.isdigit():
        print("Invalid phone number. Please enter digits only.")
        return
    if "@" not in email or "." not in email:
        print("Invalid email address format.")
        return

    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added successfully.")

# Search for a contact by name
def search_contact(contacts):
    name = input("Enter contact name to search: ").strip()
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")

# Update an existing contact's information
def update_contact(contacts):
    name = input("Enter contact name to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return

    print("Leave field blank to keep current information.")
    phone = input("Enter new phone number: ").strip()
    email = input("Enter new email address: ").strip()

    if phone:
        if not phone.isdigit():
            print("Invalid phone number. Update failed.")
            return
        contacts[name]["phone"] = phone
    if email:
        if "@" not in email or "." not in email:
            print("Invalid email format. Update failed.")
            return
        contacts[name]["email"] = email

    print(f"Contact {name} updated successfully.")

# Display all contacts
def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    print("All Contacts:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

# Main function
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Display All Contacts")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
            save_contacts(contacts)
        elif choice == '4':
            display_contacts(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
