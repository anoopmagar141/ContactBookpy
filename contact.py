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


if __name__ == "__main__":
    manager = ContactBookManager()
    manager.start()
