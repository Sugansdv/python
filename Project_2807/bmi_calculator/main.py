from core.person import Person, get_obese_people
import csv

def main():
    people = []

    while True:
        try:
            name = input("Enter name (or 'exit' to quit): ")
            if name.lower() == 'exit':
                break
            weight = float(input("Enter weight (in kg or lb): "))
            height = float(input("Enter height (in cm or ft): "))
            unit = input("Enter units (kg/cm or lb/ft): ").lower()

            person = Person(name, weight, height, unit)
            person.calculate_bmi()
            person.classify_bmi()
            people.append(person)
            person.save_to_file("data/bmi_history.csv")

            print(f"{name}'s BMI is {person.bmi:.2f} - {person.bmi_category}")
        except Exception as e:
            print(f"Error: {e}")

    print("\n--- Obese People ---")
    for p in get_obese_people(people):
        print(f"{p.name} - BMI: {p.bmi:.2f}")

if __name__ == "__main__":
    main()
