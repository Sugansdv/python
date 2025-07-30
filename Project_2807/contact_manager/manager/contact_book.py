import json
import os
from manager.contact import Contact
from manager.logger import log_actions

class ContactBook:
    def __init__(self, filepath="data/contacts.json"):
        self.contacts = {}  # key: name, value: Contact object
        self.filepath = filepath
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as file:
                try:
                    data = json.load(file)
                    for name, contact_data in data.items():
                        self.contacts[name] = Contact(**contact_data)
                except json.JSONDecodeError:
                    print("Warning: contacts.json is empty or corrupted.")
        else:
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
            with open(self.filepath, "w") as f:
                json.dump({}, f)

    def save_contacts(self):
        data = {name: contact.to_dict() for name, contact in self.contacts.items()}
        with open(self.filepath, "w") as file:
            json.dump(data, file, indent=4)

    @log_actions
    def add_contact(self, contact):
        self.contacts[contact.name] = contact

    @log_actions
    def delete_contact(self, name):
        return self.contacts.pop(name, None) is not None

    @log_actions
    def update_contact(self, name, new_contact):
        self.contacts[name] = new_contact
