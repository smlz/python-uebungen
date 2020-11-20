"""
Ein Todo-Listen Programm
"""
import os.path

fname = "todo.data"

print("Welcome to your todo list")

todos = []

if os.path.exists(fname):
    print("Loading saved todos")
    with open(fname) as f:
        for line in f:
            todos.append(line.strip())

changes = False
done = False
while not done:
    print("What would you like to do? List, Add, Remove or Quit?")
    eingabe = input("> ").lower()

    if eingabe in ("quit", "q", "x"):
        if changes:
            eingabe  = input("Save changes? [yN]").lower().strip()
            if eingabe and eingabe[0] == "y":
                with open(fname, "w") as f:
                    for todo in todos:
                        print(todo, file=f)
        done = True

    elif eingabe in ("list", "li", "l"):
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo}")
    elif eingabe in ("add", "a"):
        todo = input("Was must du erledigen? ")
        todos.append(todo)
        changes = True

    elif eingabe in ("remove", "rem", "r", "del"):
        todo = input("Was hast du erledigt? ")
        try:
            num = int(todo)
            if 0 < num <= len(todos):
                del todos[num - 1]
            else:
                print("Ungültige Nummer")
        except:
            if todo in todos:
                todos.remove(todo)
                changes = True
            else:
                print(f"'{todo}' wurde nicht gefunden")
