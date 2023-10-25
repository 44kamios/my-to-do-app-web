FILEPATH = "files/todos.txt"
def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items."""
    with open(filepath, 'r') as fileLocal:
        todosLocal = fileLocal.readlines()
    return todosLocal
def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as fileLocal:
        fileLocal.writelines(todos_arg)

print(__name__)
if __name__ == "__main__":
    print("hello from functions")