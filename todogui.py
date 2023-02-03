from todofunctions import write_todos, getTodoList
from os import path
import PySimpleGUI as Gui
# import todofunctions

_debug_ = False
TODOFILE = "todos.txt"

# Gui.theme('Default')  # https://www.pysimplegui.org/en/latest/readme/#themes

if path.exists(TODOFILE):
    todoList = getTodoList(display=False)
else:
    todoList = [TODOFILE]
    write_todos(todoList)

label = Gui.Text("Type in a to-do")
input_box = Gui.InputText(tooltip="Enter to-do", key="new_todo")
add_button = Gui.Button("Add", tooltip="Add Todo", key="Add")
edit_button = Gui.Button("Edit")
complete_button = Gui.Button("Complete")
todoListBox = Gui.Listbox(values=todoList[1:], tooltip="Select a to-do", key="todoList",
                          enable_events=True, size=(45, 10))
exit_button = Gui.Button("Exit")
MessageLabel = Gui.Text(key="message")

layout = [[label],
          [input_box, add_button],
          [todoListBox, edit_button, complete_button],
          [exit_button, MessageLabel]]

font = ("Helvetica", 20)

window = Gui.Window('ToDo List', layout=layout, font=font)

while True:
    event, values = window.read()
    if _debug_:
        print(event, values)

    match event:
        case "todoList":  # Event when an item is selected in the list
            window["new_todo"].update(value=values["todoList"][0])
            window["message"].update(value="")
        case "Add":
            new_todo = values["new_todo"]
            if new_todo == "":
                message = "Empty todo"
                if _debug_:
                    print(message)
                window["message"].update(value=message)
                continue
            todoList = getTodoList(display=False)
            todoList.append(new_todo.strip().capitalize() + '\n')
            if _debug_:
                print(todoList)
            write_todos(todoList)
            message = f"Added: {new_todo}"
            window["message"].update(value=message)
            window["new_todo"].update(value="")
            window["todoList"].update(values=todoList[1:])
        case "Edit":
            todos = values["todoList"]
            if len(todos) == 1:
                todo = values["todoList"][0]
            else:
                message = "Please select one to-do in the list box"
                if _debug_:
                    print(message)
                window["message"].update(value=message)
                continue
            new_todo = values["new_todo"]
            if new_todo == "":
                message = "Please enter a todo to replace the selected item"
                if _debug_:
                    print(message)
                window["message"].update(value=message)
                continue
            if _debug_:
                print(todoList)
            num = todoList.index(todo)

            todoList[num] = new_todo.capitalize().strip() + '\n'  # replace with the new item
            if _debug_:
                print(todoList)
            write_todos(todoList)
            window["todoList"].update(values=todoList[1:])
            message = f"Edited: {todo} to: {new_todo}"
            if _debug_:
                print(message)
            window["message"].update(value=message)
        case "Complete":
            todos = values["todoList"]
            if len(todos) == 1:
                todo = values["todoList"][0]
            else:
                message = "Please select only one to-do in the list box"
                if _debug_:
                    print(message)
                window["message"].update(value=message)
                continue
            num = todoList.index(todo)
            message = f'Removed: {todoList.pop(num)}'
            if _debug_:
                print(message)
            write_todos(todoList)
            window["todoList"].update(values=todoList[1:])
            window["message"].update(value=message)
            window["new_todo"].update(value="")
        case "Exit":
            break
        case Gui.WIN_CLOSED:
            break

window.close()
