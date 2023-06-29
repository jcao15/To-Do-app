import functions
import PySimpleGUI as Gui

label = Gui.Text("Type in a to-do")
input_box = Gui.InputText(tooltip="Enter todo", key="todo")
add_button = Gui.Button("Add")
list_box = Gui.Listbox(values=functions.read_todos(),
                       key="todos",
                       enable_events=True, size=(45, 10))
edit_button = Gui.Button("Edit")

window = Gui.Window("My To-Do App",
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
                    font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todos"])
    match event:
        case "Add":
            todos = functions.read_todos()
            new_todo = values['todo']
            todos.append(new_todo)
            functions.write_todos(todos)

            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.read_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case Gui.WIN_CLOSED:
            break

window.close()
