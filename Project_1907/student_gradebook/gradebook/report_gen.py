def generate_report_card(students, roll):
    for s in students:
        if s['info'][0] == roll:
            name = s['info'][1]
            grades = s['grades']
            print("\n Report Card")
            print("=" * 30)
            print(f"Name     : {name}")
            print(f"Roll No. : {roll}")
            print("-" * 30)
            if grades:
                for subject, mark in grades.items():
                    print(f"{subject:<15}: {mark}")
                avg = sum(grades.values()) / len(grades)
                print("-" * 30)
                print(f"Average  : {avg:.2f}")
            else:
                print("No grades recorded.")
            print("=" * 30)
            return
    print(" Student not found.")
