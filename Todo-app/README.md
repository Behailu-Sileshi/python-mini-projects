**Todo List Manager**

# Overview

A simple command-line Todo List Manager that allows users to create, view, remove, and mark todos as completed. The application ensures that all todos have valid dates and provides error messages for invalid inputs.

# Features

- Create Todos: Add a new todo with a specific date and note.
- Show Todos: Display all current todos.
- Remove Todos: Delete a todo by its order in the list.
- Mark Todos as Completed: Mark or unmark a todo as completed.
- Input Validation: Ensures the date format is correct and not in the past.

# Technologies Used

- Python 3.12
- datetime module for date handling
- File handling for data persistence

# Installation
1. Clone the repository:

    git clone https://github.com/yourusername/todo-list-manager.git

2. Navigate to the project directory:

    cd todo-list-manager
Ensure you have Python 3.12 installed on your machine.

# Usage

Run the application:
    
    python main.py

Follow the on-screen prompts to manage your todo list.

Example Commands

    Enter 1 to create a new todo.
    Enter 2 to display the list of todos.
    Enter 3 to remove a todo by its order.
    Enter 4 to mark a todo as completed.
    Enter 5 to exit the application.

# Error Handling
The application will handle the following errors:

- Invalid date format: Prompts the user to enter a date in the correct format (YYYY-MM-DD).
- Past dates: Notifies the user that the date cannot be in the past.
- Invalid order number: Notifies the user when trying to remove or mark a todo that does not exist.

# License

This project is licensed under the MIT License - see the LICENSE file for details.
Contributing

Feel free to fork the repository and submit pull requests if you want to contribute to this project.
# Author
[Behailu Sileshi](https://github.com/Behailu-Sileshi)
