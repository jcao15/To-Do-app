FILEPATH = "files/todos.txt"
def printlist(todolist: []):
    for i, act in enumerate(todolist):
        act = act.strip('\n')
        x = f"{i + 1}-{act}"
        print(x)


def read_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_file = file_local.readlines()
    return todos_file


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the to-do items list in the text file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print('Hello')
    print(read_todos())
