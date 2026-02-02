def load_tasks():
    try:
        with open('tasks.txt', 'r', encoding='utf-8') as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.txt', 'w', encoding='utf-8') as f:
        for task in tasks:
            f.write(task + '\n')

tasks = load_tasks()

while True:
    try:
        user_input = int(input('\nJust enter the number to execute the following:\n---Menu---\n1. Add Tasks\n2. View Tasks\n3. Mark done\n4. Delete Tasks\n5. Delete all tasks\n6. Exit\nEnter: '))
    except ValueError:
        print('Please choose a valid option (1-6)')
        continue

    # Adding Tasks
    if user_input == 1:
        print('\nEnter "Done" when done entering you tasks')
        while True:
            user_tasks = input('Enter your tasks: ').lower()
            if user_tasks != 'done':
                tasks.append(user_tasks.title())
            elif user_tasks == 'done':
                break
        save_tasks(tasks)

    # Viewing the Tasks
    elif user_input == 2:
        print('\n--Tasks--')
        if not tasks:
            print('No Tasks Yet.')
        else:
            for i, task in enumerate(tasks, start=1):
                print(f'{i}. {task}')

    # Marking tasks as done
    elif user_input == 3:
        print('\n--Tasks--')
        if not tasks:
            print('No tasks to mark done.')
            continue

        for i, task in enumerate(tasks, start=1):
            print(f'{i}. {task}')
        
        try:
            done_task = int(input('Enter task number to mark done: ').strip())
        except ValueError:
            print('Please enter a valid number.')
            continue
        
        if 1 <= done_task <= len(tasks):
            index = done_task - 1
            selected_task = tasks[index]
            if "✅" in selected_task:
                print("Already done.")
            else:
                tasks[index] += " ✅"
                save_tasks(tasks)
                print("Marked done!")
        else:
            print('Invalid task number.')

    # Deleting the tasks
    elif user_input == 4:
        print('\n--Tasks--')
        if not tasks:
            print('No Tasks Yet.')
            continue
        else:
            for i, task in enumerate(tasks, start=1):
                print(f'{i}. {task}')

        try:
            delete_task = int(input('Enter task number to delete: ').strip())
        except ValueError:
            print('Please enter a valid number.')
            continue

        if 1 <= delete_task <= len(tasks):
            index = delete_task - 1
            deleted = tasks.pop(index)
            save_tasks(tasks)
            print(f'Deleted: {deleted}')
        else:
            print('Invalid task number.')

    # Deleting all tasks at once
    elif user_input == 5:
        print('\n--Tasks--')
        if not tasks:
            print('No Tasks Yet.')
            continue
        else:
            for i, task in enumerate(tasks, start=1):
                print(f'{i}. {task}')

        delete_all = (input('Are you sure to delete all tasks? Y/N ').strip().lower())

        if delete_all == 'y':
            tasks.clear()
            save_tasks(tasks)
            print('All tasks deleted.')
        elif delete_all == 'n':
            continue
        else:
            print('Please enter Y for yes or N for No.')

    # Exiting the Program
    elif user_input == 6:
        print('Goodbye')
        break
    