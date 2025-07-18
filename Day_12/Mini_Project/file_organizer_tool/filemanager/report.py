def generate_report(files_by_type):
    print("\n--- File Organizer Report ---")
    for category, files in files_by_type.items():
        print(f"{category.capitalize()}: {len(files)} files")
        for f in files:
            print(f"  - {f}")
