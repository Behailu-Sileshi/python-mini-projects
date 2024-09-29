import sqlite3


class Contact:
    def __init__(self, name, phone_number, email = None):
        self.name = name
        self.phone_number = phone_number
        self.email = email
    def __str__(self):
        print(f" name: {self.name}\n phone_no: {self.phone_number}\n Email: {self.email}")

class PhoneBook:
    def __init__(self, db_name = 'phonebook'):
        self.db_name = f'data/{db_name}' + '.sqlite3'
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.__create_table()

    def __create_table(self):
        command = "CREATE TABLE IF NOT EXISTS phonebook (name VARCHAR(25), phone_number VARCHAR(15), email VARCHAR(12))"
        self.cursor.execute(command)
        self.conn.commit()
    def close(self):
        if self.cursor:
            self.cursor.close()
            self.conn.close()

    def add_contact(self, contact: Contact):
        command = "INSERT INTO phonebook (name, phone_number, email) VALUES(?, ?, ?)"
        self.cursor.execute(command, (contact.name, contact.phone_number, contact.email))
        self.conn.commit()
        print('Added Succefully')
    def edit_contact(self, phone_no, new_contact: Contact):
        if self.__find_contact(phone_no) is not None:
            command = f"UPDATE phonebook SET name = ? , phone_number = ?, email = ? WHERE phone_number = ?"
            self.cursor.execute(command, (new_contact.name, new_contact.phone_number, new_contact.email, phone_no))
            self.conn.commit()
            print('Edited successfully')
        else:
             print('No contact found with a given info.')
    def display_contact(self):
        command = "SELECT * FROM phonebook"
        cursor = self.cursor.execute(command)
        if len(cursor.fetchall()) != 0:
            for index, row in enumerate(cursor):
                print(f"{index + 1}. {row}")
        else:
            print('No contact found!!')
    def delete_contact(self, phone_no):
            if self.__find_contact(phone_no) is not None:
                command = "DELETE FROM phonebook WHERE phone_number = ?"
                self.cursor.execute(command, (phone_no ,))
                self.conn.commit()
                print('deleted successfully!')
            else:
                print('No contact found with a given info.')
    def __find_contact(self, phone_no):
        command = "SELECT * FROM phonebook WHERE phone_number = ?"
        self.cursor.execute(command, (phone_no, ))
        return self.cursor.fetchone()
        
phone = PhoneBook()
phone.display_contact()

