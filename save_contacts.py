import json

FILE_NAME = "contacts.txt"

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file)
