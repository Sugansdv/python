import csv
import os

FILENAME = "students.csv"

def add_student():
    name = input("Enter student name: ").strip()
    roll = input("Enter roll number: ").strip()
    try:
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Invalid marks. Please enter a number.")
        return

    file_exists = os.path.isfile(FILENAME)

    with open(FILENAME, "a", newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Roll", "Marks"])  # Write header if file doesn't exist
        writer.writerow([name, roll, marks])
    print(" Student data added.")

def view_students():
    if not os.path.exists(FILENAME):
        raise FileNotFoundError(" CSV file not found. Please add student data first.")

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        records = list(reader)

    if len(records) <= 1:
        print("No student records yet.")
        return

    print("\n Student Records:")
    for row in records:
        print(f"{' | '.join(row)}")

    # Extract only marks from rows (excluding header)
    marks = [float(row[2]) for row in records[1:]]

    average = sum(marks) / len(marks)
    topper_index = marks.index(max(marks)) + 1  # +1 to account for header
    topper = records[topper_index]

    print(f"\n Average Marks: {average:.2f}")
    print(f" Topper: {topper[0]} (Roll: {topper[1]}, Marks: {topper[2]})")

def main():
    print("=== Student Marks Recorder ===")
    while True:
        print("\nOptions:")
        print("1. Add Student Record")
        print("2. View All Records + Stats")
        print("3. Exit")

        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            try:
                view_students()
            except FileNotFoundError as e:
                print(e)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
