import os

# Simple XOR cipher
def xor_cipher(data, key=123):
    return bytes([b ^ key for b in data])

# Encrypt a file
def encrypt_file(input_path, output_path):
    if not os.path.exists(input_path):
        print(" File does not exist.")
        return

    try:
        with open(input_path, "rb") as infile:
            data = infile.read()

        encrypted_data = xor_cipher(data)

        with open(output_path, "wb") as outfile:
            outfile.write(encrypted_data)

        print(f" File encrypted and saved as: {output_path}")
    except Exception as e:
        print(" Encryption error:", e)

# Decrypt a file
def decrypt_file(input_path, output_path):
    if not os.path.exists(input_path):
        print(" Encrypted file not found.")
        return

    try:
        with open(input_path, "rb") as infile:
            data = infile.read()

        decrypted_data = xor_cipher(data)

        with open(output_path, "wb") as outfile:
            outfile.write(decrypted_data)

        print(f" File decrypted and saved as: {output_path}")
    except Exception as e:
        print(" Decryption error:", e)

# Menu system
def main():
    print("=== File Encryption & Decryption Tool ===")
    print("1. Encrypt a File")
    print("2. Decrypt a File")
    choice = input("Choose (1/2): ").strip()

    if choice == "1":
        src = input("Enter path of file to encrypt: ").strip()
        dest = input("Enter name for encrypted file (e.g., secret.bin): ").strip()
        encrypt_file(src, dest)
    elif choice == "2":
        src = input("Enter path of file to decrypt (.bin): ").strip()
        dest = input("Enter name for decrypted file (e.g., output.txt): ").strip()
        decrypt_file(src, dest)
    else:
        print(" Invalid choice.")

if __name__ == "__main__":
    main()
