import csv
import logging

class InvalidCSVFormatError(Exception):
    pass

def csv_uploader(file_path):
    logging.basicConfig(filename='invalid_rows.log', level=logging.INFO)
    print(f"\n Uploading {file_path}...\n")

    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            if 'name' not in reader.fieldnames or 'age' not in reader.fieldnames:
                raise InvalidCSVFormatError(" CSV must contain 'name' and 'age' columns.")
            
            for row in reader:
                try:
                    name = row['name']
                    age = int(row['age'])
                    if age < 0:
                        raise ValueError("Age cannot be negative.")
                    print(f" {name} - {age} years")
                except Exception as e:
                    logging.info(f"Invalid row: {row} -> {e}")

    except FileNotFoundError:
        print(" File not found.")
    except InvalidCSVFormatError as e:
        print(e)
    except Exception as e:
        print(" Unknown error:", e)
    else:
        print(" File processed successfully.")
    finally:
        print(" Upload finished.\n")

csv_uploader("people.csv")
