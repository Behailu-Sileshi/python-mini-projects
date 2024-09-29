import sqlite3


class Contact:
    """
    Represents a contact in the phonebook.

    Attributes:
        name (str): The contact's name.
        phone_number (str): The contact's phone number.
        email (str, optional): The contact's email address. Defaults to None.
    """
    
    def __init__(self, name, phone_number, email=None):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        """
        Returns a string representation of the contact.
        """
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email or 'N/A'}"


class PhoneBook:
    """
    Represents a phonebook that stores and manages contacts using SQLite.

    Attributes:
        db_name (str): The name of the SQLite database file.
        conn (sqlite3.Connection): The SQLite database connection.
        cursor (sqlite3.Cursor): The SQLite database cursor.
    """
    
    def __init__(self, db_name='phonebook'):
        """
        Initializes the phonebook and connects to the SQLite database.

        Args:
            db_name (str, optional): The name of the SQLite database file. Defaults to 'phonebook'.
        """
        self.db_name = f'data/{db_name}.sqlite3'
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.__create_table()

    def __create_table(self):
        """
        Creates the phonebook table if it doesn't exist.
        """
        command = """
        CREATE TABLE IF NOT EXISTS phonebook (
            name VARCHAR(25),
            phone_number VARCHAR(15),
            email VARCHAR(50) NULL
        )
        """
        self.cursor.execute(command)
        self.conn.commit()

    def close(self):
        """
        Closes the connection to the database.
        """
        if self.cursor:
            self.cursor.close()
            self.conn.close()

    def add_contact(self, contact: Contact):
        """
        Adds a new contact to the phonebook.

        Args:
            contact (Contact): The contact to be added.
        """
        command = "INSERT INTO phonebook (name, phone_number, email) VALUES (?, ?, ?)"
        self.cursor.execute(command, (contact.name, contact.phone_number, contact.email))
        self.conn.commit()
        print('Contact added successfully.')

    def edit_contact(self, phone_no, new_contact: Contact):
        """
        Edits an existing contact in the phonebook by phone number.

        Args:
            phone_no (str): The phone number of the contact to be edited.
            new_contact (Contact): The updated contact information.
        """
        if self.__find_contact(phone_no):
            command = """
            UPDATE phonebook 
            SET name = ?, phone_number = ?, email = ? 
            WHERE phone_number = ?
            """
            self.cursor.execute(command, (new_contact.name, new_contact.phone_number, new_contact.email, phone_no))
            self.conn.commit()
            print('Contact edited successfully.')
        else:
            print('No contact found with the given phone number.')

    def display_contacts(self):
        """
        Displays all contacts stored in the phonebook.
        """
        command = "SELECT * FROM phonebook"
        self.cursor.execute(command)
        contacts = self.cursor.fetchall()

        if contacts:
            for index, contact in enumerate(contacts):
                print(f"{index + 1}. Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2] or 'N/A'}")
        else:
            print('No contacts found.')

    def delete_contact(self, phone_no):
        """
        Deletes a contact from the phonebook by phone number.

        Args:
            phone_no (str): The phone number of the contact to be deleted.
        """
        if self.__find_contact(phone_no):
            command = "DELETE FROM phonebook WHERE phone_number = ?"
            self.cursor.execute(command, (phone_no,))
            self.conn.commit()
            print('Contact deleted successfully.')
        else:
            print('No contact found with the given phone number.')

    def __find_contact(self, phone_no):
        """
        Finds a contact in the phonebook by phone number.

        Args:
            phone_no (str): The phone number to search for.

        Returns:
            tuple: The contact information if found, else None.
        """
        command = "SELECT * FROM phonebook WHERE phone_number = ?"
        self.cursor.execute(command, (phone_no,))
        return self.cursor.fetchone()
