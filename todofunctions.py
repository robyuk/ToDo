TODO_FILE = "todos.txt"  # Default todo file path
TODO_LIST = [TODO_FILE]


def print_todo(todos=TODO_LIST):
    """Prints the todo list in todoList"""
    # Use a breakpoint in the code line below to debug your script.
    message = "\nTo Do List: " + todos[0]
    print(message)  # Press Ctrl+F8 to toggle the breakpoint.
    print(len(message) * '-')
    for i, item in enumerate(todos[1:]):
        print(f'{i+1}. {item}', end="")
    print()


def get_userArg(userAction=""):  # Return the user argument to a userAction
    """ Returns the user argument in the string userAction"""
    try:
        return userAction.split(" ", 1)[1]
    except IndexError:
        return ""


def confirmYN(text="Confirm"):
    """ Asks the user to confirm.  Returns True if the answer is Yes, and False if the answer is no"""
    while True:
        confirm = input(text + " (Y/N)? ").strip().lower()
        try:
            match confirm[0]:
                case 'y':
                    return True
                case 'n':
                    return False
        except:
            print("Please answer yes or no.")
            continue


def getTodoList(filename=TODO_FILE, display=True):
    """ open a todo list file at filename and read the todoList
        Return the todo list with the filename as the first item """
    while filename == "":
        filename = input("Enter filename: ")
    todos = [filename]
    try:
        with open(filename, "r") as file:
            todos = todos + file.readlines()
        if display:
            print_todo(todos)
        return todos
    except FileNotFoundError:
        if confirmYN("New ToDo List," + filename):
            return todos


def write_todos(todos=TODO_LIST):
    """ Write the todos list to a file at path todos[0] """
    while todos[0] == '':
        file_name = input("Filename: ")
        todos[0] = file_name  # Insert new file name
    try:
        with open(todos[0], 'w') as file:
            file.writelines(todos[1:])
    except:
        print("Error writing Todo list to file:", todos[0])
        todos[0] = '\n'


if __name__ == '__main__':
    print("Hello from todofunctions")
    print(getTodoList())
