from cipher_tool.cipher import Cipher

if __name__ == "__main__":
    key = input("Enter secret key: ").strip()
    cipher = Cipher(key)

    choice = input("1. Encrypt File\n2. Decrypt File\nChoose (1/2): ").strip()
    file_path = input("Enter file path: ").strip()

    try:
        if choice == "1":
            cipher.encrypt_file(file_path)
            print("File encrypted successfully.")
        elif choice == "2":
            cipher.decrypt_file(file_path)
            print("File decrypted successfully.")
        else:
            print("Invalid choice.")
    except Exception as e:
        print("Error:", e)
