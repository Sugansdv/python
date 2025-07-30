import os
from core.entry import PasswordEntry
from core.encryption import encrypt_data, decrypt_data
from core.auth import logged_in
import json
import random
import string

class PasswordManager:
    def __init__(self, key, filepath="data/passwords.enc"):
        self.filepath = filepath
        self.key = key
        self.authenticated = True
        self.passwords = []
        self.compromised = set()
        self.load_passwords()

    def load_passwords(self):
        if not os.path.exists(self.filepath):
            return
        with open(self.filepath, "r") as file:
            encrypted = file.read()
            try:
                decrypted = decrypt_data(encrypted, self.key)
                self.passwords = [PasswordEntry(**entry) for entry in json.loads(decrypted)]
            except Exception:
                self.authenticated = False
                print("Failed to decrypt data. Are you using the correct key?")

    def save_passwords(self):
        data = [entry.__dict__ for entry in self.passwords]
        encrypted = encrypt_data(json.dumps(data), self.key)
        with open(self.filepath, "w") as file:
            file.write(encrypted)

    @logged_in
    def add_password(self, website, username, password):
        entry = PasswordEntry(website, username, password)
        self.passwords.append(entry)
        if len(password) < 8:
            self.compromised.add(password)
        self.save_passwords()

    @logged_in
    def retrieve_passwords(self):
        return self.passwords

    @logged_in
    def delete_password(self, website):
        self.passwords = [p for p in self.passwords if p.website != website]
        self.save_passwords()

    @logged_in
    def generate_strong_password(self, length=12):
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))

    @logged_in
    def weak_passwords(self):
        for entry in self.passwords:
            if len(entry.password) < 8:
                yield entry
