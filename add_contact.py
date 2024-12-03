def add_contact(contacts):
    print("\n=== Add Contact ===")
    name = input("Enter Name: ")
    if not name.isalpha():
        print("Error: Name must be a string.")
        return

    phone = input("Enter Phone Number: ")
    if not phone.isdigit():
        print("Error: Phone number must be an integer.")
        return

    if phone in [contact['phone'] for contact in contacts]:
        print("Error: Phone number already exists.")
        return

    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!")
