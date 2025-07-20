def get_unique_people(appointments):
    people = set()
    for appt_list in appointments.values():
        for _, person, _ in appt_list:
            people.add(person)
    return people
