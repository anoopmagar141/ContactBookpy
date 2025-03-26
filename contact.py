class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name} | Phone: {self.phone} | Email: {self.email}"


class ContactBookManager:
    def __init__(self):
        self.contacts = []

    def start(self):
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Delete Contact")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.search_contact()
            elif choice == "4":
                self.delete_contact()
            elif choice == "5":
                print("Exiting Contact Book...")
                break
            else:
                print("Invalid choice! Please try again.")

    def add_contact(self):
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        self.contacts.append(Contact(name, phone, email))
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("\nContact List:")
        for contact in self.contacts:
            print(contact)

    def search_contact(self):
        name = input("Enter name to search: ")
        found = [contact for contact in self.contacts if contact.name.lower() == name.lower()]
        if found:
            for contact in found:
                print(contact)
        else:
            print("Contact not found.")

    def delete_contact(self):
        name = input("Enter name to delete: ")
        initial_length = len(self.contacts)
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]
        if len(self.contacts) < initial_length:
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")


if __name__ == "__main__":
    manager = ContactBookManager()
    manager.start()
