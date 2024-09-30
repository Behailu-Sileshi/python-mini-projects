from todo_manager import Todo, TodoList, FileStorage


def main():
    file = FileStorage()
    todo_list = TodoList(file)
    print('\t\t\t\tWelcome to Todo List Manager')
    
    while True:
        print(
            '''
            \t\t1. Create Todo
            \t\t2. Show Todo List
            \t\t3. Remove Todo
            \t\t4. Mark/Unmark Todo as Completed 
            \t\t5. Exit
            '''
        )
        try:
            choice = int(input('\tEnter your choice: '))
            if choice == 1:
                todo = create_todo()
                todo_list.add(todo)
            elif choice == 2:
                todo_list.show()  
            elif choice == 3:
                todo_list.show()  
                try:
                    order = int(input("Enter todo order to delete: "))
                    todo_list.remove(order)
                except (IndexError, ValueError):
                    print("Todo not found or invalid input! Numbers only.")
            elif choice == 4:
                todo_list.show()  
                try:
                    order = int(input("Enter todo order to mark/unmark: "))
                    todo_list.mark_as_completed(order)
                except (IndexError, ValueError):
                    print("Todo not found or invalid input! Numbers only.")
            elif choice == 5:
                print('Exiting...')
                break
            else:
                print('Incorrect choice.')
        except ValueError:
            print('Invalid input. Please enter a valid number.')

            
def create_todo():
    """Handles user input for creating a todo, using Todo class validation."""
    while True:
        date = input('Input date (YYYY-MM-DD): ')
        note = input('Input note: ')
        try:
            return Todo(date, note)
        except ValueError as e:
            print(f"Error: {e}. Please try again.")


if __name__ == '__main__':
    main()

