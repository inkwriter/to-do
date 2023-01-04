todos = []

while True:
    user_action = input("Type add, show, or exit: ")
    user_action = user_action.strip()
    
    if user_action == 'add':
        todo = input("Enter a todo: ")
        todos.append(todo)
    elif user_action == 'show':
        for item in todos:
            print(item)
    elif user_action == 'exit':
        break
print("Bye")


