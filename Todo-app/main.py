from todo import create_todo, remove_todo, show_todo, mark_todo_as_completed



print('\t\t\t\t\t\tWelcome to todo list manager')


def edit_todo(edit):
    try:
        order = int(input('Enter the todo order: '))
    except ValueError:
        print("Invalid order, Number only.")
    else:
        edit(order)
while True:
    print(
        '''
        \t\t\t\t\t1. create todo
        \t\t\t\t\t2. show todo list
        \t\t\t\t\t3. remove todo
        \t\t\t\t\t4. mark/unmark todo as completed ''')
    try:
        choice = int(input('\tEnter your choice: '))
    except ValueError:
        print('Invalid input try again!!')
    else:
        if choice == 1:
            create_todo()
        elif choice == 2:
            show_todo()
        elif choice == 3:
            if show_todo():
                edit_todo(remove_todo)
        elif choice == 4:
            if show_todo():
                edit_todo(mark_todo_as_completed)
        else:
            print('incorrect choice.')

