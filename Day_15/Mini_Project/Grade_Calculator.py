def get_valid_grade():
    try:
        grade = float(input("Enter grade (0–100): "))
        if not (0 <= grade <= 100):
            raise ValueError("❌ Grade must be between 0 and 100.")
        return grade
    except ValueError as e:
        print(e)
        return get_valid_grade()  # Recursively retry

def grade_calculator():
    grades = []
    while True:
        option = input("Add grade? (yes/no): ").strip().lower()
        if option == "no":
            break
        elif option == "yes":
            grade = get_valid_grade()
            grades.append(grade)
        else:
            print(" Invalid option.")

    try:
        average = sum(grades) / len(grades)
        print(f"\n Average Grade: {average:.2f}")
    except ZeroDivisionError:
        print("❌ No valid grades entered.")
    finally:
        print(f" Total Valid Grades: {len(grades)}")

if __name__ == "__main__":
    grade_calculator()
