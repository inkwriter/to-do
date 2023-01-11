todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    
    if user_action == "add":
        todo = input("Enter a todo: ") + "\n"

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)
    elif user_action == "show":
                
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todos = []

        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)
        print(todos)

        for index, item in enumerate(new_todos):
            row = f"{index +1} * {item}"
            print(row)

    elif user_action == "edit":
        number = int(input("Number of the todo to edit: "))
        number = number - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action == "complete":
        number = int(input("The number that was removed from the list: "))

        with open("todos.txt", "r") as file:
            todos = file.readlines()
        index = number - 1
        todo_to_remove = todos[index].strip("\n")
        todos.pop(index)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list."

    elif user_action == "exit":
        break
    else:
        print("Please choose add, show, edit, or exit!")

print("Bye")


