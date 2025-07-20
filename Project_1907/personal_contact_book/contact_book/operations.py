import os
import json

CONTACTS_FILE = os.path.join("data", "contacts.txt")

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return {}
    with open(CONTACTS_FILE, "r") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts, name, phone, email, tags, category):
    contacts[name] = {
        "phone": phone,
        "email": email,
        "tags": list(tags),
        "category": category
    }
    print(f" Contact '{name}' added.")

def update_contact(contacts, name, phone=None, email=None, tags=None, category=None):
    if name in contacts:
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        if tags:
            contacts[name]["tags"] = list(tags)
        if category:
            contacts[name]["category"] = category
        print(f" Contact '{name}' updated.")
    else:
        print(f" Contact '{name}' not found.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f" Contact '{name}' deleted.")
    else:
        print(f" Contact '{name}' not found.")

def search_contact(contacts, name):
    return contacts.get(name, None)

def list_contacts(contacts):
    for name in sorted(contacts):
        info = contacts[name]
        print(f"\n👤 {name}")
        print(f" Phone: {info['phone']}")
        print(f" Email: {info['email']}")
        print(f" Tags: {', '.join(info['tags'])}")
        print(f" Category: {info['category']}")
