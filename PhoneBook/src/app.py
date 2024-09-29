from pathlib import Path
from phone_book import PhoneBook, Contact

def main():
    phonebook = PhoneBook()
    # while True:
    try:
        
            choice = int(input(
                """
                Welcome to phonebook mini app
                    1. Create contact
                    2. Edit contact
                    3. Delete contact
                    4. Display contacts
                    5. Type any other character to exist
                Enter your choice: """
                ))
    except ValueError:
        print("please Enter number only!!")
    else:
            if choice == 1:
                phonebook.add_contact(accept_contact_info())
            elif choice == 2:
                phone_no = input('Enter the contact phone number you want to edit: ')
                phonebook.edit_contact(phone_no, accept_contact_info())
            elif choice == 3:
                phone_no = input('Enter the phone number you want to delete: ')
                phonebook.delete_contact(phone_no)
            elif choice == 4:
                phonebook.display_contact()
           

            


def accept_contact_info():
    while True:
        name = input('Input full name: ').strip()
        email = input('Input email address(optional): ').strip()
        phone_number = input('Input phone number: ').strip()
        if name == '' or  phone_number == '':
            print('please input all necessary info!')
        else:
            contact = Contact(name, phone_number, email)
            return contact
if __name__ == "__main__":
    main()
    

