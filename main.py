# This is a To-Do List project.
from functions import *
import time

current_time = time.strftime("%b %d, %Y %H:%M:%S")
print("It's", current_time, "now")


while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = read_todos()

        todos.append(todo + '\n')

        write_todos(todos)
        print('Current todos list :')
        printlist(todos)

    elif user_action.startswith('show'):
        todos = read_todos()
        printlist(todos)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1

            cur_todos = read_todos()

            new_todo = input("Enter a new todo: ")
            cur_todos[number] = new_todo + '\n'

            write_todos(cur_todos)
        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            cur_todos = read_todos()

            todo_to_remove = cur_todos[number - 1].strip('\n')
            cur_todos.pop(number - 1)

            write_todos(cur_todos)

            msg = f"Todo '{todo_to_remove}' was removed from the list."
            print(msg)
            print("Current to do list: ")
            printlist(cur_todos)
        except IndexError:
            print('There is no item with that number index.')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid Command.")
print("Bye!")

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
