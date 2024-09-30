from datetime import datetime as dt
from pathlib import Path
from typing import List


class Todo:
    def __init__(self, date, note):
        self.__date = date
        self.__note = note

    def formatted_todo(self):
        return f"☐ {self.date} {self.note}\n"

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        try:
            parsed_date = dt.strptime(date, "%Y-%m-%d")
            if parsed_date < dt.now():
                raise ValueError("Date cannot be in the past.")
            self.__date = parsed_date
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        

    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note):
        self.__note = note


class FileStorage:
    """Handles file operations for the todo list."""
    FILE_PATH = Path('data/todo.txt')

    def __init__(self):
        self.FILE_PATH.parent.mkdir(exist_ok=True)

    def save_todos(self, todos: List[str]):
        """Save all todos to the file."""
        with self.FILE_PATH.open("w") as file:
            file.writelines(todos)

    def load_todos(self) -> List[str]:
        """Load todos from the file."""
        if not self.FILE_PATH.exists():
            return []
        with self.FILE_PATH.open() as file:
            return file.readlines()

    def delete_file(self):
        """Delete the todo file if it exists."""
        if self.FILE_PATH.exists():
            self.FILE_PATH.unlink()


class TodoList:
    """Manages a list of todos."""
    def __init__(self, storage: FileStorage):
        self.storage = storage
        self.todos = self.storage.load_todos()

    def add(self, todo: Todo):
        self.todos.append(todo.formatted_todo())
        self.storage.save_todos(self.todos)
        print('Todo created successfully.')

    def remove(self, order: int):
        if order < 1 or order > len(self.todos):
            raise IndexError("Invalid order number.")
        self.todos.pop(order - 1)
        if self.todos:
            self.storage.save_todos(self.todos)
        else:
            self.storage.delete_file()
        print('Todo removed successfully.')

    def show(self):
        if not self.todos:
            print('No todo items found!')
        else:
            for index, todo in enumerate(self.todos, start=1):
                print(f"{index}. {todo.strip()}")

    def mark_as_completed(self, order: int):
        if order < 1 or order > len(self.todos):
            raise IndexError
        self.todos[order - 1] = self.todos[order - 1].replace('☐', '☑')
        self.storage.save_todos(self.todos)
        print(f"Todo {order} marked as completed.")
