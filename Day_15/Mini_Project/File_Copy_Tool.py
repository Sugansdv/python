# file_copy_tool.py

import os
import logging

# Setup logging
logging.basicConfig(filename='file_copy_errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def copy_file(source_path, destination_path):
    try:
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Source file not found: {source_path}")

        if os.path.getsize(source_path) == 0:
            raise ValueError("Source file is empty!")

        with open(source_path, 'r') as src:
            data = src.read()

        with open(destination_path, 'w') as dest:
            dest.write(data)

        print(" File copied successfully!")

    except FileNotFoundError as e:
        print(f" Error: {e}")
        logging.error(e)

    except PermissionError as e:
        print(" Permission denied while accessing file.")
        logging.error(e)

    except ValueError as e:
        print(f" {e}")
        logging.error(e)

    except Exception as e:
        print(f" Unexpected error: {e}")
        logging.error("Unexpected: %s", e)

    finally:
        print(" Copy operation finished.")

# Example run
if __name__ == "__main__":
    src = input("Enter source file path: ")
    dest = input("Enter destination file path: ")
    copy_file(src, dest)
