import add_contact
import view_contacts
import remove_contact
import search_contact
import load_contacts
import save_contacts

def main():
    contacts = load_contacts.load_contacts()  # Call the `load_contacts` function from the `load_contacts` module
    while True:
        print("\n=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact.add_contact(contacts)  # Call the `add_contact` function from the `add_contact` module
        elif choice == '2':
            view_contacts.view_contacts(contacts)  # Call the `view_contacts` function from the `view_contacts` module
        elif choice == '3':
            remove_contact.remove_contact(contacts)  # Call the `remove_contact` function from the `remove_contact` module
        elif choice == '4':
            search_contact.search_contact(contacts)  # Call the `search_contact` function from the `search_contact` module
        elif choice == '5':
            save_contacts.save_contacts(contacts)  # Call the `save_contacts` function from the `save_contacts` module
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
