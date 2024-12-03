from contacts import ContactsManager, Contact
from file_handler import save_contacts_to_file, load_contacts_from_file
from tabulate import tabulate

def display_menu():
    print("\n===============================")
    print("\nContact Book Management")
    print("\n===============================")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contacts")
    print("5. Exit")

def get_contact_details():
    name = input("Enter Name: ").strip().title()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone Number (format: 01*********): ").strip()
    address = input("Enter Address: ").strip()

    if not phone.isdigit() or not phone.startswith('01') or len(phone) != 11:
        raise ValueError("Phone number must be an 11-digit number starting with '01'...")
    return name, email, phone, address

def display_contacts(contacts):
    table = [[idx + 1, contact.name, contact.email, contact.phone, contact.address] 
            for idx, contact in enumerate(contacts)]
    headers = ["ID", "Name", "Email", "Phone", "Address"]
    print(tabulate(table, headers, tablefmt="grid"))

def main():
    contacts_manager = ContactsManager()
    contacts_manager.contacts = load_contacts_from_file()

    while True:
        display_menu()
        choice = input("Select an option: ").strip()

        if choice == '1':
            try:
                name, email, phone, address = get_contact_details()
                if phone in contacts_manager.contacts:
                    print("Error: This phone number is already assigned to another contact.")
                else:
                    contact = Contact(name, email, phone, address)
                    contacts_manager.add_contact(contact)
                    # Save the updated and sorted contacts
                    save_contacts_to_file(contacts_manager.contacts)
                    print("Contact added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            contacts = contacts_manager.view_contacts()
            if contacts:
                print("\nContacts:")
                display_contacts(contacts)
            else:
                print("No contacts available.")

        elif choice == '3':
            query = input("Enter name or part of the name to search for deletion: ").strip()
            results = contacts_manager.search_contacts(query)
            if results:
                print("\nSearch Results:")
                display_contacts(results)
                try:
                    selected_id = int(input("Enter the ID of the contact to delete: ").strip())
                    if 1 <= selected_id <= len(results):
                        contact_to_delete = results[selected_id - 1]
                        contacts_manager.remove_contact(contact_to_delete.phone)
                        # Save the updated and sorted contacts
                        save_contacts_to_file(contacts_manager.contacts)
                        print("Contact deleted successfully.")
                    else:
                        print("Invalid ID.")
                except ValueError:
                    print("Please enter a valid numeric ID.")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            query = input("Enter name or part of the name to search: ").strip()
            results = contacts_manager.search_contacts(query)
            if results:
                print("\nSearch Results:")
                display_contacts(results)
            else:
                print("No contacts found.")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
