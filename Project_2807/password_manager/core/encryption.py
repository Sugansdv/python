import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BLOCK_SIZE = 16

def pad(s):
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

def unpad(s):
    return s[:-ord(s[-1])]

def get_key(password):
    return hashlib.sha256(password.encode()).digest()

def encrypt_data(data, key):
    key = get_key(key)
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(data).encode())
    return base64.b64encode(iv + encrypted).decode()

def decrypt_data(enc_data, key):
    try:
        enc_data = base64.b64decode(enc_data)
        iv = enc_data[:BLOCK_SIZE]
        encrypted = enc_data[BLOCK_SIZE:]
        cipher = AES.new(get_key(key), AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(encrypted).decode())
    except Exception:
        raise ValueError("Invalid decryption key or corrupted file.")
