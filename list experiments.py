import random
tasks = []
php = 100
chp = 120
print("1. Add Task\n"
      "2. Delete Task\n"
      "3. Edit Task name\n"
      "4. Complete Task\n"
      "5. Fight\n"
      "6. Exit Taskmaster")
choice = int(input("Enter a choice from 1 - 6: "))
while choice != 7 or (choice < 1 or choice >6):
    if choice == 1:
        task = input('Enter a task to add to to-do list and "0" to stop: ')
        while task != "0" or len(tasks) < 12:
            if task == "0":
                break
            else:
                print(f"Task '{task}' added to to-do list.")
                print("Task list: ")
                tasks.append(task)
                for i in range(0,len(tasks)):
                    print(f"{i + 1}. {tasks[i]}")
                task = input('Enter a task to add to to-do list and "0" to stop: ')
                if task == "0":
                    break
    elif choice == 2:
        for i in range(0,len(tasks)):
            print(f"{i + 1}. {tasks[i - 1]}")
        remove = int(input("Enter task number to remove or '0' to stop: "))
        while remove <= len(tasks) or len(tasks) != 0 or remove < 1 or remove != 0:
            if remove == 0:
                break
            print(f'Task "{tasks[remove - 1]}" removed.')
            del tasks[remove - 1]
            for i in range(0,len(tasks)):
                    print(f"{i + 1}. {tasks[i]}")
            remove = int(input("Enter task number to remove or '0' to stop: "))
    elif choice == 3:
        for i in range(0,len(tasks)):
            print(f"{i + 1}. {tasks[i - 1]}")
        edit = int(input("Enter task number to edit or '0' to stop: "))
        while edit <= len(tasks) or len(tasks) != 0 or edit< 1:
            tasks[edit - 1] = input("Enter new task name: ")
            print(f'Task "{tasks[edit - 1]}" edited is the new name of task no. {edit}.')
            for i in range(0,len(tasks)):
                print(f"{i + 1}. {tasks[i ]}")
            edit = int(input("Enter task number to edit or '0' to stop: "))
    elif choice == 4:
        for i in range(0,len(tasks)):
            print(f"{i + 1}. {tasks[i ]}")
        complete = int(input("Enter task number accomplished or '0' to stop: "))
        while edit <= len(tasks) or len(tasks) != 0 or edit< 1:
            print(f'Task "{tasks[edit - 1]}" accomplished.')
            del tasks[edit - 1]
            for i in range(0,len(tasks)):
                print(f"{i + 1}. {tasks[i ]}")
            complete = int(input("Enter task number accomplished or '0' to stop: "))
    elif choice == 5:
        pattack = int(input("Enter 1 for Blade, 2 for Bow, or 3 for Shield."))
        while chp > 0 or php > 0:
            attacks = ["Blade", "Bow", "Shield"]
            cattack = random.randint(0,2)
            if pattack == cattack:
                print(f" Player chose: {attacks[pattack - 1]}")
                print(f" Computer chose: {attacks[cattack]}")
                chp -= 5
                php -= 5
                print(f"Computer: {chp}")
                print(f"Player: {php}")
            if attacks[pattack - 1] == "Blade" and attacks[cattack] == "Bow" or attacks[pattack - 1] == "Shield" and attacks[cattack] == "Bow" or attacks[cattack - 1] == "Blade" and attacks[pattack] == "Shield":
                print(f" Player chose: {attacks[pattack - 1]}")
                print(f" Computer chose: {attacks[cattack]}")
                php -= 10
                print(f"Computer: {chp}")
                print(f"Player: {php}")
            if attacks[cattack ] == "Blade" and attacks[pattack-1] == "Bow" or attacks[cattack ] == "Shield" and attacks[pattack - 1] == "Bow" or attacks[cattack ] == "Blade" and attacks[cattack] == "Shield":
                print(f" Player chose: {attacks[pattack - 1]}")
                print(f" Computer chose: {attacks[cattack]}")
                chp -= 10
                print(f"Computer: {chp}")
                print(f"Player: {php}")
            pattack = int(input("Enter 1 for Blade, 2 for Bow, or 3 for Shield."))
            if chp == 0:
                print ('Player wins!')
                break
            elif php == 0:
                print('Computer Wins!')
                break
            pattack = int(input("Enter 1 for Blade, 2 for Bow, or 3 for Shield."))
    choice = int(input("Enter a choice from 1 - 6: "))
print('Goodbye, user!')



