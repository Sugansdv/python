
from healthcare_records.records import add_patient_record, display_patient_records, get_patients_with_illness

# Tuple (patient ID), Dictionary (records), Set (illnesses)
medical_data = {}

# Adding sample patients
add_patient_record(medical_data, ("P001",), "Alice", 30, ["Flu", "Cold"])
add_patient_record(medical_data, ("P002",), "Bob", 45, ["Diabetes"])
add_patient_record(medical_data, ("P003",), "Charlie", 38, ["Cold", "Asthma"])

# Display all records
display_patient_records(medical_data)

# Query: patients with 'Cold'
print("Patients diagnosed with Cold:")
for pid in get_patients_with_illness(medical_data, "Cold"):
    print(pid)
