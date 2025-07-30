def contact_generator(contacts_dict, keyword):
    """Generator to yield matching contacts by keyword."""
    for name, contact in contacts_dict.items():
        if keyword.lower() in name.lower():
            yield contact
