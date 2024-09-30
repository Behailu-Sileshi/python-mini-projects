from datetime import datetime as dt
from pathlib import Path


class Todo:
    def __init__(self, date, note):
        self.date = date
        self.note = note
        self.is_marked = False
    def formatted_todo(self):
        if self.is_marked:
            return f"  ☑ {self.__date.date()} {self.__note}"
        else:
            return f"  ☐ {self.__date.date()} {self.__note}"
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date):
            todo_date = dt.strptime(date, "%Y-%m-%d")
            if todo_date < dt.now():
                raise ValueError
            self.__date = todo_date
    @property
    def note(self):
        return self.__note
    @note.setter
    def note(self, note):
        self.__note = note




def create_todo():
    date = input('Input the date (YYYY-MM-DD): ')
    note = input('Input the description (note): ')
    try:
        todo = Todo(date, note)
    except ValueError:
        print("Invalid date please try again!!")
    else:
        with open('todo.txt', "a") as todo_list:
            todo_list.write(f"{todo.formatted_todo()}")
            print('you have created a todo successfully.')
def remove_todo(order):
    with open('todo.txt') as file:
        todo_list = file.readlines()
        todo_list.pop(order - 1)
        if len(todo_list) == 0:
            with open('todo.txt', 'w') as file2:
                file2.write('')
        else:
            for todo in todo_list:
                with open('todo.txt', 'w') as file2:
                    file2.write(todo)
    print('removed successfully')
def show_todo():
    print("*" * 5 , "TODO LIST ", "*" * 5)

    if not Path('todo.txt').exists():
        print('No todo item found!!')
    with open('todo.txt') as file:
        todo_list = file.readlines()
        if len(todo_list) == 0:
            print("No todo item found.")
            return False
        else:
            for index, todo in enumerate(todo_list):
                index = index + 1
                print(index, todo)
            return True
def mark_todo_as_completed(order):
    with open('todo.txt') as file:
        todo_list = file.readlines()
        marked_todo = todo_list[order - 1].replace( '☐',  '☑')
        todo_list[order - 1] = marked_todo
    with open('todo.txt', 'w') as file2:
        for todo in todo_list:
            file2.writelines(todo)

