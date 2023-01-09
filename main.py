todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    
    if user_action == "add":
        todo = input("Enter a todo: ")
        todos.append(todo)
    elif user_action == "show":
        for index, item in enumerate(todos):
            row = f"{index +1} -{item}"
            print(row)
    elif user_action == "edit":
        number = int(input("Number of the todo to edit: "))
        number = number - 1
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo
    elif user_action == "complete":
        number = int(input("Number of the todo to complete: "))
        todos.pop(number -1)
    elif user_action == "exit":
        break
    else:
        print("Please choose add, show, edit, or exit!")

print("Bye")


