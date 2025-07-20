def search_by_name(employees, name):
    results = [e for e in employees if name.lower() in e['name'].lower()]
    if results:
        for e in results:
            print(f"ID: {e['id'][0]} | Name: {e['name']} | Department: {e['department']}")
    else:
        print("No matching employee found.")

def search_by_department(employees, dept):
    results = [e for e in employees if dept.lower() == e['department'].lower()]
    if results:
        for e in results:
            print(f"ID: {e['id'][0]} | Name: {e['name']} | Department: {e['department']}")
    else:
        print("No employees in this department.")
