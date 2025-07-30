import os
from cryptography.fernet import Fernet, InvalidToken
from cipher_tool.utils import generate_fernet_key
from cipher_tool.logger import log_encryptions

class Cipher:
    def __init__(self, secret: str):
        self.secret = secret
        self.key = generate_fernet_key(secret)
        self.fernet = Fernet(self.key)

    @log_encryptions
    def encrypt_file(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError("File not found.")

        with open(file_path, "rb") as f:
            data = f.read()

        encrypted = self.fernet.encrypt(data)

        with open(file_path + ".enc", "wb") as f:
            f.write(encrypted)

    @log_encryptions
    def decrypt_file(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError("File not found.")

        with open(file_path, "rb") as f:
            encrypted_data = f.read()

        try:
            decrypted = self.fernet.decrypt(encrypted_data)
        except InvalidToken:
            raise ValueError("Invalid key or corrupted file.")

        output_path = file_path.replace(".enc", ".dec")

        with open(output_path, "wb") as f:
            f.write(decrypted)
