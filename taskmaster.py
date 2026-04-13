#importing libraties for functionalities.
import json
import random
import time
import msvcrt
    #===============Functions for gameplay=============
try:
    #==loading json file(with saved progress)==
    def load_game():
        xp = 0
        global data
        with open("player.json", "r") as f:
            data = json.load(f)
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
              "9. Quit and dont save".title())

        choice = input("Enter your choice: ")
        done = False
        while not done:
            if choice == "1":
                new_data(data["player"]["user"], data["player"][""])

            elif choice == "2":
                print("2")

            elif choice == "3":
                view_stats()

            elif choice == "4":
                add_task(data["player"]["tasks_to_do"])

            elif choice == "5":
                complete_task(data["Player"]["tasks_to_do"])

            elif choice == "6":
                print("6")

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
        user = input("Enter your new Hero Title: ")
    #==If player wants to view stats, this will print them.==
    def view_stats():
        for player in data["player"]:
            print(player["username"])
            for i in player["tasks_to_do"]:
                print(f"{i + 1}: {player["tasks_to_do"][i]}")
            print(player["tasks_done"])

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
        while not complete:
            try:
                task_to_complete = int(input("Enter your accomplished task(number): "))
                if task_to_complete >= (len(task_list)+1):
                    print("Invalid task. Please try again.")
                else:
                    del task_list[task_to_complete]
                    complete = True
            except TypeError:
                print("Task number must be an integer!")


    def choose_weapon(weapon_list):
        global weapons
        weapons = []
        for w in weapon_list:
            weapons.append(weapon_list[w])
        print("Your weapons are:")
        for item in weapons:
            print(f"{item+1}. {weapons[item]}")
        valid = False
        try:
            chosen_weapon = int(input("Enter your chosen weapon: "))
            if weapon_list[chosen_weapon - 1]==data["weapons"]["swords"][0]:
                damage = data["damage"]
        except TypeError:
            print("Invalid choice. Please try again.")

    def enemy_choose_weapon():
        pass


    def resolve_round(player_weapon, enemy_weapon):
        pass


    def boss_round(level_number):
        global win
        win = False
        print(f"===Your Opponent is....===")
        time.sleep(1)
        print(f">>=={data["bosses"][level_number]}!==<<")
        if level_number == 1:
            typing_effect("Here's how you fight the boss!")


    def can_fight_boss(level_number):
        global cost
        cost = data["prices"]["bosses"][level_number]
        print(f"To fight the boss, you need at least {cost} gold as payment.")
        if data["player"]["gold"] >= cost:
            print("Ok, you can fight the boss!")
            return True
        else:
            print("You can't fight the boss! Grind some more tasks!")
            return None


    def pay_boss_cost(level_number):
        if can_fight_boss(data["player"]["level"]-1):
            data["player"]["gold"] -= cost
            print(f"You have {data["player"]["gold"]} gold left.")
            print("Now, enter the boss arena!")


    def give_boss_reward(level_number):
        message = f"For defeating {data["bosses"][level_number]}, you get {data["rewards"][level_number]} gold!"
        typing_effect(message)
        data["player"]["gold"] += data["rewards"][level_number]



    def rebirth_player():
        pass


    def level_up():
        pass


    def check_true_ending():
        pass


    #printing intro and instructions.
    typing_effect("====<<<<WELCOME TO TASKMASTER!>>>>====\n")
    typing_effect("A project by: Augusto Alfonso Cayabyab, Juan Miguel Rivera, and Gilian Uoiea Janiola!\n")
    typing_effect("For starters, this is the whole point of taskmaster: ELIMINATE PROCRASTINATION!\n")
    typing_effect("To use this, follow the given instructions.\n")
    typing_effect("You will see a menu with 9 choices. Preferably, choose the New Profile or New username/password option to give yourself\n"
          "an identity. Now, choose Add a new task. This will aid you in completing tasks for gold. If you want to claim your reward \n"
          "after finishing a task, choose the Mark Task as Completed option. Great. You finished your first task. \n"
          "Now, you can buy items. Choose the Buy Items option. Buy ALL the items you need. Choose the Fight Boss option now.\n"
          "I'll give you instructions on how to fight it when you get there.\n")

except FileNotFoundError:
    print("No player.json File Found!")