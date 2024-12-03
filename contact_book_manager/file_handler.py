import csv
from contacts import Contact

def save_contacts_to_file(contacts, filename='contacts.csv'):
    # Sort contacts by name before saving
    sorted_contacts = sorted(contacts.values(), key=lambda contact: contact.name)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Email', 'Phone', 'Address'])
        for contact in sorted_contacts:
            writer.writerow([contact.name, contact.email, contact.phone, contact.address])

def load_contacts_from_file(filename='contacts.csv'):
    contacts = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                phone = row['Phone']
                # Validate phone number format
                if phone.isdigit() and phone.startswith('01') and len(phone) == 11:
                    contact = Contact(row['Name'], row['Email'], phone, row['Address'])
                    contacts[phone] = contact
    except FileNotFoundError:
        pass
    return contacts
