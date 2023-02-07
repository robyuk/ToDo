# Press Shift+F10 to execute
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Starting values:
TODO_FILE = "todos.txt"  # Default to-do file path
TODO_LIST = [TODO_FILE]   # Default to-do list

import time
from todofunctions import getTodoList, write_todos, confirmYN, print_todo, get_userArg
# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print(time.strftime("It is %H:%M on %d %b %Y"))
    todofile = TODO_FILE  # Default todos file
    userPrompt = "Enter a ToDo: "
    actionPrompt = "Type new, open, add, edit, remove, list, save, or quit: "
#    todoList = TODO_LIST
    userAction = "Ask"  # Dummy value to satisfy the condition in the first loop of the while
    todoList = getTodoList(todofile)  # Get the default todos

    while not userAction == "":  # Exit if userAction is empty
        match userAction[0]:
            case 'n':
                todoList = getTodoList(userArg)
            case 'o':
                todoList = getTodoList(userArg)
            case 'a':
                todo = userArg
                while todo == "":
                    todo = input(userPrompt)
                todoList.append(todo.strip().capitalize() + '\n')
                print(todoList)
                write_todos(todoList)

            case 'e':   # edit an item in the list
                todo = ""
                if userArg == "":
                    print_todo(todoList)
                    try:
                        num = int(input("\nEnter number of item to replace (0 to exit): "))
                    except ValueError:
                        num = 0
                elif userArg.isdigit():
                    num = int(userArg)
                else:
                    try:
                        num, todo = userArg.split(" ", 1)
                        num = int(num)
                    except ValueError:
                        num = 0
                        print("Invalid edit command.  The correct syntax is:")
                        print("e[dit] [n [todo]]")
                        print("Where n is the number of an existing todo item to be edited")
                        print("and todo is the todo to replace that item.")

                if num < len(todoList):
                    if num > 0 and confirmYN(f'Edit: {num}. {todoList[num]}'):  # Confirm the item to be edited
                        todo = input(userPrompt).strip().capitalize()  # input the new item
                        todoList[num] = todo + '\n'  # replace with the new item
                        write_todos(todoList)
                else:
                    print(f"There is no item with that number: ({num}).")

            case 'r':
                try:
                    num = int(userArg)
                except ValueError:
                    print_todo(todoList)
                    try:
                        num = int(input("\nEnter number of item to remove (0 to exit): "))
                    except ValueError:
                        num = 0
                if num < len(todoList):
                    if num > 0 and confirmYN(f'Remove: {num}. {todoList[num]}'):
                        print(f'Removed: {num}. {todoList.pop(num)}')
                        write_todos(todoList)
                else:
                    print("There is no item with that number")

            case 'l':
                print_todo(todoList)
            case 's':
                if not userArg == "":  # Save to a new filename
                    todoList[0] = userArg
                write_todos(todoList)
            case 'q':
                break
            case _else:
                pass

        userAction = input(actionPrompt).strip().lower()  # Get the next user action
        userArg = get_userArg(userAction)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
