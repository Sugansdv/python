

def add_patient_record(records, patient_id, name, age, illness_list):
    illness_set = set(illness_list)
    records[patient_id] = {
        'name': name,
        'age': age,
        'illnesses': illness_set
    }

def display_patient_records(records):
    for pid, details in records.items():
        print(f"Patient ID: {pid}")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Illnesses: {', '.join(details['illnesses'])}")
        print('-' * 30)

def get_patients_with_illness(records, illness_name):
    return [pid for pid, details in records.items() if illness_name in details['illnesses']]
