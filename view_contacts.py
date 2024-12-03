def view_contacts(contacts):
    print("\n=== View Contacts ===")
    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, 1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
