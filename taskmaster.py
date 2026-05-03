#importing libraties for functionalities.
import json
import random
import time
#===============Functions for gameplay=============
try:
    #==loading json file(with saved progress)==
    def load_game():
        xp = 0
        with open("player.json", "r") as f:
            global data
            data = json.load(f)
            return data

    def typing_effect(text):
        for char in text:
            print(char, end="", flush=True)
            time.sleep(0.05)
    #==saving game for progress saving==
    def save_game():
        with open("players.json", "w") as f:
            json.dump(data, f, indent=4)
    #==resetting profile for restart==
    def reset_game():
        with open("players.json", "r") as f:
            data = json.load(f)
            data["player"] = {"player": {"user": "", "password": "", "tasks_to_do": [],"tasks_done": 0, "gold": 0,"level": 1, "hp": 100, "weapons_loadout": ["Bare Fists", "", ""], "xp": 0, "lvl":1, "task_reward":  5}}
            with open("players.json", "w") as f:
                json.dump(data, f, indent=4)
    #==new profile addition==
    def create_player():
        done = False
        while not done:
            data["player"]["username"] = input("Enter your preferred Hero Title: ")
            data["player"]["password"] = input("Enter your preferred Hero's Code (password): ")
    #==login for security purposes==
    def sign_in():
        done = False
        while not done:
            userlogin = input("Enter your Hero Title: ")
            passlogin = input("Enter your Hero's Code (password): ")
            if userlogin == data["player"]["user"] and passlogin == data[0]["player"]["password"]:
                print("Logged in! Enjoy the experience!")
                done = True
                done = True
    #==printing menu and also choice picking option
    def show_menu():
        global choice
        print("The choices are numbered as follows:")
        print("1. New Password/ New Username\n"
              "2. Save and Exit Game\n"
              "3. View stats\n"
              "4. Add a new task to task list\n"
              "5. Mark task as completed\n"
              "6. Fight Boss\n"
              "7. New Profile(reset stats)\n"
              "8. Buy Items\n"
              "9. Delete Progress".title())

        choice = input("Enter your choice: ")
        done = False
        while not done:
            if choice == "1":
                new_data(data[0]["player"]["user"], data[0]["player"]["password"])

            elif choice == "2":
                save_game()
                print("Please Come Back.")
                done = True

            elif choice == "3":
                view_stats()

            elif choice == "4":
                add_task(data[0]["player"]["tasks_to_do"])

            elif choice == "5":
                complete_task(data[0]["player"]["tasks_to_do"])

            elif choice == "6":
                can_fight_boss(data[0]["player"]["level"])
                pay_boss_cost(data[0]["player"]["level"])
                boss_round(data[0]["player"]["level"])
                while data[6]["boss_hp"][data[0]["player"]["level"]] != 0:
                    while data[0]["player"]["hp"] != 0:
                        resolve_round(choose_weapon(data[0]["player"]["weapons_loadout"]), enemy_choose_weapon(), enemy_choose_weapon())

            elif choice == "7":
                print("7")

            elif choice == "8":
                buy_items()

            elif choice == "9":
                done = True
            else:
                print("INVALID INPUT ... TRY AGAIN")
            choice = input("Enter your choice: ")
    def new_data(user, passw):
        raz = int(input("1.New user\n2.New Password\nEnter your choice:"))
        if raz == 1:
            user = input("Enter your new Hero Title: ")
        elif raz ==2:
            passw = input("Enter your new passcode: ")
    #==If player wants to view stats, this will print them.==
    def view_stats():
        stats = {}
        stats.update(data[0]['player'])
        print(stats['user'])
        print("Tasks to do:")
        for player in stats['tasks_to_do']:
            print(f"{0+1}.{player}")
        print(f"Tasks Accomplished: {stats["tasks_done"]}")
        print(f"Gold: {stats["gold"]}")
        print(f"Level {stats["level"]}")
        print(f"Player HP: {stats["hp"]}")
        print(f"Loadout:\nSword:{stats['weapons_loadout']['sword']}\nBow:{stats['weapons_loadout']['bow']}\nShield:{stats['weapons_loadout']['shield']}")
        print(f"Reward for Completing a task: {stats['task_reward']} Gold")
        show_menu()


        while True:
            choice = input("Enter 0 to exit: ")
            print(" ")

            if choice == '0':
                show_menu()
            else:
                print("INVALID INPUT")
                time.sleep(0.1)
                print(".")
                time.sleep(0.2)
                print("TRY AGAIN")
                time.sleep(0.2)
                print(" ")

    def buy_items():
        bought_items = []
        for items in data["items"]:
            bought_items.append(items["title"])

    def add_task(task_list):
        typing_effect("===Welcome to Taskmaster's===")
        typing_effect("===Task Addition Manager!===")
        task_to_add = input("Enter your task to add: ")
        task_list.append(task_to_add)
        print(f"Task {task_to_add} added to task list!")

    def complete_task(task_list):
        complete = False
        typing_effect("===Welcome to Taskmaster's===")
        typing_effect("===Task Completion Reward Manager!===")
        for item in task_list:
            print(f"{item+1}. {task_list[item]}")
        print(f"13. Exit")
        while not complete:
            try:
                task_to_complete = int(input("Enter your accomplished task(number): "))
                if task_to_complete >= (len(task_list)+1):
                    print("Invalid task. Please try again.")
                else:
                    del task_list[task_to_complete]
                    complete = True
                if task_to_complete==13:
                    show_menu()
            except TypeError:
                print("Task number must be an integer!")
        if complete == True:
            data[0]["player"]["tasks_done"] + 1
            data[0]["player"]["gold"] + data[0]["player"]["task_reward"]
            complete = not complete


    def choose_weapon(weapon_list):
        global weapons
        weapons = []
        for w in weapon_list:
            weapons.append(weapon_list[w])
        print("Your weapons are:")
        for item in enumerate(weapons):
            print(f"{item[0]+1}. {weapons[item[0]]}")
        valid = False
        try:
            chosen_weapon = int(input("Enter your chosen weapon: "))
        except TypeError:
            print("Invalid choice. Please try again.")
        print(f"You have chosen to use {weapons[chosen_weapon-1]}")

    def enemy_choose_weapon():
        echoose = random.randint(0,2)
        if echoose == 0:
            eweap = data[7]["boss_items"]["sword"]
        elif echoose == 1:
            eweap = data[7]["boss_items"]["bow"]
        elif echoose == 2:
            eweap = data[7]["boss_items"]["shield"]
        print(f"{data[6]["bosses"][data[0]["player"]["level"]]} uses {eweap}")

    def resolve_round(chosen_weapon, eweap, echoose):
      if data[6]["boss_hp"][data[0]["player"]["level"]] != 0:
       if data[0]["player"]["hp"] != 0:
         if eweap != False:
           if chosen_weapon != False:
             if echoose==chosen_weapon:
                 print("Tie")
                 eweap = False
                 chosen_weapon = False
             elif chosen_weapon-1 == 0:
                if eweap == "shield":
                #deal damage to enemy
                    eweap = False
                    chosen_weapon = False
                    pass
                elif eweap == "bow":
                #do damage to player
                    eweap = False
                    chosen_weapon = False
                    pass
             elif chosen_weapon-1 == 1:
                if eweap == "shield":
                #do dmg to player
                    eweap = False
                    chosen_weapon = False
                    pass
                elif eweap == "sword":
                #do dmg to enemy
                    eweap = False
                    chosen_weapon = False
                    pass
             elif chosen_weapon-1 == 3:
                if eweap == "bow":
                    #do dmg to enemy
                    eweap = False
                    chosen_weapon = False
                    pass
                elif eweap == "sword":
                    # do dmg to player
                    eweap = False
                    chosen_weapon = False
                    pass
           else:
             choose_weapon(data[0]["player"]["weapons_loadout"])
         else:
           enemy_choose_weapon()
       else:
         loss(data[0]["player"]["level"])
      else:
          pass


    def boss_round(level_number):
        global win
        win = False
        print(f"===Your Opponent is....===")
        time.sleep(1)
        print(f">>=={data[6]["bosses"][level_number]}!==<<")
        if level_number == 1:
            typing_effect("Here's how you fight the boss!")
            typing_effect("Pr")


    def can_fight_boss(level_number):
        data
        global cost
        cost = data[3]["prices"]["bosses"][level_number]
        print(f"To fight the boss, you need at least {cost} gold as payment.")
        if data[0]["player"]["gold"] >= cost:
            print("Ok, you can fight the boss!")
            return True
        else:
            print("You can't fight the boss! Grind some more tasks!")
            return None


    def pay_boss_cost(level_number):
        if can_fight_boss(data[0]["player"]["level"]-1):
            level_number["player"]["gold"] -= cost
            print(f"You have {level_number["player"]["gold"]} gold left.")
            print("Now, enter the boss arena!")


    def give_boss_reward(level_number):
        message = f"For defeating {level_number["bosses"][level_number]}, you get {level_number["rewards"][level_number]} gold!"
        typing_effect(message)
        data["player"]["gold"] += data["rewards"][level_number]

    def loss():
        messages = ["It is too early for death.", "Save us!", "We NEED you.", "FIGHT FOR THE LAND OF LYSTE!", "Prove yourself to him.", f"{data["bosses"][level_number]} is waiting for you."]
        messages2 = ["Get Up.", "Wake Up.", ""]
        message = random.choice(messages)
        message2 = random.choice(messages2)
        typing_effect(message)
        typing_effect(message2)

    def rebirth_player(level):
        if level <= 4:
            typing_effect(f"The Land of Lyste is safe once again thanks to you, o great {data['player']['user']} the Taskmaster.")
            typing_effect("Do you wish to rebirth and start your journey anew?(yes/no): ")
            level += 1


    def check_true_ending(level):
        if level == 4:
            print(f"Four times you have started your journey anew, and four times have you have fought ")


    #printing intro and instructions.
    load_game()
    intro = input("Skip intro?(yes/no): ")
    Yes=["yes", "y", "Yes", "YES", "Y"]
    No= ["N", "n", "no", "NO", "N"]
    if intro in Yes:
        show_menu()
    elif intro in No:
        typing_effect("====<<<<WELCOME TO TASKMASTER!>>>>====\n")
        typing_effect("A project by: Augusto Alfonso Cayabyab, Juan Miguel Rivera, and Gilian Uoiea Janiola!\n")
        typing_effect("For starters, this is the whole point of taskmaster: ELIMINATE PROCRASTINATION!\n")
        typing_effect("")
        typing_effect("To use this, follow the given instructions.\n")
        typing_effect("You will see a menu with 9 choices. Preferably, choose the New Profile or New username/password option to give yourself\n"
            "an identity. Now, choose Add a new task. This will aid you in completing tasks for gold. If you want to claim your reward \n"
            "after finishing a task, choose the Mark Task as Completed option. Great. You finished your first task. \n"
            "Now, you can buy items. Choose the Buy Items option. Buy ALL the items you need. Choose the Fight Boss option now.\n"
            "I'll give you instructions on how to fight it when you get there.\n")
        show_menu()


except FileNotFoundError:
    print("No player.json File Found!")