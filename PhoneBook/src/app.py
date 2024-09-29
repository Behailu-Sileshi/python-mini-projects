from phone_book import PhoneBook, Contact

def main():
    """
    Main function to run the phonebook application.
    Displays a menu for the user to choose an action and processes their input.
    """
    phonebook = PhoneBook()

    while True:
        try:
            choice = int(input(
                """
                Welcome to Phonebook Mini App
                    1. Create Contact
                    2. Edit Contact
                    3. Delete Contact
                    4. Display Contacts
                    5. Exit
                Enter your choice: """
            ))

            if choice == 1:
                phonebook.add_contact(accept_contact_info())
            elif choice == 2:
                phone_no = input('Enter the contact phone number you want to edit: ')
                phonebook.edit_contact(phone_no, accept_contact_info())
            elif choice == 3:
                phone_no = input('Enter the phone number you want to delete: ')
                phonebook.delete_contact(phone_no)
            elif choice == 4:
                phonebook.display_contacts()
            elif choice == 5:
                print("Exiting the Phonebook. Goodbye!")
                break  # Exit the loop and end the program
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
                
        except ValueError:
            print("Please enter a valid number only!")

def accept_contact_info():
    """
    Prompts the user for contact information until valid input is received.

    Returns:
        Contact: A Contact object containing the user's input.
    """
    while True:
        name = input('Input full name: ').strip()
        email = input('Input email address (optional): ').strip()
        phone_number = input('Input phone number: ').strip()

        if not name or not phone_number:
            print('Please input all necessary information!')
        else:
            return Contact(name, phone_number, email)

if __name__ == "__main__":
    main()
