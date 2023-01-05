todos = []

while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip()
    
    if user_action == "add":
        todo = input("Enter a todo: ")
        todos.append(todo)
    elif user_action == "show":
        for item in todos:
            print(item)
    elif user_action == "edit":
        number = int(input("Number of the todo to edit: "))
        number = number - 1
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo
    elif user_action == "exit":
        break
    else:
        print("Please choose add, show, or exit!")

print("Bye")


