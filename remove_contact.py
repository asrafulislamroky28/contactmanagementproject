def remove_contact(contacts):
    print("\n=== Remove Contact ===")
    phone = input("Enter the phone number of the contact to remove: ")
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print("Contact removed successfully!")
            return
    print("Error: Contact not found.")
