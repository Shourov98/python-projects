# contacts.py

class Contact:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self):
        return f"{self.name}, {self.email}, {self.phone}, {self.address}"


class ContactsManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        if contact.phone in self.contacts:
            raise ValueError("This phone number is already assigned to another contact.")
        self.contacts[contact.phone] = contact

    def remove_contact(self, phone):
        if phone in self.contacts:
            del self.contacts[phone]
        else:
            raise ValueError("Contact not found.")

    def view_contacts(self):
        return list(self.contacts.values())

    def search_contacts(self, query):
        return [contact for contact in self.contacts.values() if query.lower() in contact.name.lower()]