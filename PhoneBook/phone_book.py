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
        self.db_name = db_name + '.sqlite3'
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
        if self.conn:
            self.conn.close()

    def add_contact(self, contact: Contact):
        command = "INSERT INTO phonebook (name, phone_number, email) VALUES(?, ?, ?)"
        self.cursor.execute(command, (contact.name, contact.phone_number, contact.email))
        self.conn.commit()
    def edit_contact(self, name, new_contact: Contact):
        command = f"UPDATE phonebook SET name = ? , phone_number = ?, email = ? WHERE name = ?"
        self.cursor.execute(command, (new_contact.name, new_contact.phone_number, new_contact.email, name))
        self.conn.commit()
    def delete_contact(self, name):
        command = "DELETE FROM phonebook WHERE name = ?"
        self.cursor.execute(command, (name ,))
        self.conn.commit()







phonebook = PhoneBook()
contact = Contact('beya', '0931250190')
ct = Contact('meron', '0953579959')
# phonebook.add_contact(contact)
phonebook.delete_contact("meron")
phonebook.close()


