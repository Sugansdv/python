import os

def rename_txt_files(folder_path):
    try:
        files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
        files.sort()  # Optional: for predictable order

        count = 1
        for file in files:
            old_path = os.path.join(folder_path, file)
            new_name = f"file_{count}.txt"
            new_path = os.path.join(folder_path, new_name)

            # Handle duplicates: file_1.txt already exists
            suffix = 1
            while os.path.exists(new_path):
                new_name = f"file_{count}_{suffix}.txt"
                new_path = os.path.join(folder_path, new_name)
                suffix += 1

            os.rename(old_path, new_path)
            print(f"Renamed '{file}' → '{new_name}'")
            count += 1

    except FileNotFoundError:
        print(" Folder not found.")
    except Exception as e:
        print(f" Error: {e}")

# Example usage
if __name__ == "__main__":
    folder = input("Enter folder path: ").strip()
    rename_txt_files(folder)
