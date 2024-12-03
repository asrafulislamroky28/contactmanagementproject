def search_contact(contacts):
    print("\n=== Search Contacts ===")
    query = input("Enter search term (name, phone, email, or address): ")
    results = [contact for contact in contacts if query.lower() in str(contact.values()).lower()]
    if results:
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No contacts found.")
