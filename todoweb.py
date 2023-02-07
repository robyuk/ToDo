import streamlit as st
from os import path
from todofunctions import getTodoList, write_todos

_debug_ = False
TODO_FILE = "todos.txt"
NEW_TODO_PROMPT = "Enter a new todo"
NL = '\n'

if path.exists(TODO_FILE):
    todoList = getTodoList(display=_debug_)
else:
    todoList = [TODO_FILE]
    write_todos(todoList)


def add_todo():
    new_todo = st.session_state['new_todo'].strip().capitalize()

    if _debug_:
        print(new_todo)
        print(st.session_state)

    if new_todo == '' or new_todo == ' ':
        return
    
    todoList.append(new_todo + NL)
    write_todos(todoList)

# Gui.theme


if "visibility" not in st.session_state:
    st.session_state.visibility = "hidden"
    st.session_state.disabled = False
    st.session_state.placeholder = NEW_TODO_PROMPT

st.title("My Todo List")
st.subheader("A simple Todo list app")
st.write("A simple app to increase productivity")

# st.checkbox("Label of the checkbox")

for index, todo in enumerate(todoList[1:], start=1):
    st.checkbox(todo, key=index)

text_input = st.text_input("newTodo",
                           label_visibility=st.session_state.visibility,
                           placeholder=st.session_state.placeholder,
                           disabled=st.session_state.disabled,
                           on_change=add_todo, key='new_todo')

if _debug_:
    if text_input:
        st.write("In the new todo box, you entered: ", text_input)
    st.write("session_state:")
    st.write(st.session_state)
    print(text_input)
    print('End.')

for num in range(len(todoList)-1, 1, -1):
    if st.session_state[str(num)]:  # get the state of the checkbox
        if _debug_:
            print("Remove", todoList[num])
        st.write(f'Completed: {todoList.pop(num)}')  # Pop the item checked
        write_todos(todoList)
        #
        # The next two lines don't work on Windows 10 with streamlit 1.17.0
        # ie. the checked to-do is not removed from the displayed web page
        # until the next event
        del st.session_state[str(num)]  # delete the checkbox from the displayed list
        var = st.experimental_rerun     # re-run the script to re-display the web page

