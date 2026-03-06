#importing libraties for functionalities.
import json
import random
import time
#===============Functions for gameplay=============
#==loading json file(with saved progress)==
def load_game():
    global data
    with open("player.json", "r") as f:
        data = json.load(f)
def typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)
#==saving game for progress saving==
def save_game(data):
    with open("players.json", "w") as f:
        json.dump(data, f, indent=4)
#==resetting profile for restart==
def reset_game():
    with open("players.json", "r") as f:
        data = json.load(f)
        data["player"] = {"user": "", "password": "", "tasks_to_do": [],"tasks_done": 0, "gold": 0,"level": 1, "hp": 100, "weapons_loadout": ["Bare Fists", "", ""]}
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
        if userlogin == data[0]["player"] and passlogin == data[0]["player"]["password"]:
            print("Logged in! Enjoy the experience!")
            done = True
            done = True
#==printing menu and also choice picking option
def show_menu():
    global choice
    print("The choices are numbered as follows:")
    print("1. New Password/ New Username\n"
          "2. Save/Exit Game\n"
          "3. View stats\n"
          "4. Add a new task to task list\n"
          "5. Mark task as completed\n"
          "6. Fight Boss\n"
          "7. New Profile(reset stats)\n"
          "8. Buy Items")
    choice = int(input("Enter your choice: "))
#==If player wants to view stats, this will print them.==
def view_stats():
    for player in data["player"]:
        print(player["username"])
        for i in player["tasks_to_do"]:
            print(f"{i+1}: {player["tasks_to_do"][i]}")
        print(player["tasks_done"])

def buy_items():
    bought_items = []
    for items in data["items"]:
        bought_items.append(items["title"])

def add_task(task_to_add, task_list):
    typing_effect("===Welcome to Taskmaster's===")
    typing_effect("===Task Addition Manager!===")
    task_to_add = input("Enter your task to add: ")
    task_list.append(task_to_add)
    print(f"Task {task_to_add} added to task list!")

def complete_task(task_to_complete, task_list):
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
        weapons.append(w["player"]["weapons_loadout"][w])
    print("Your weapons are:")
    for item in weapons:
        print(f"{item+1}. {weapons[item]}")
    valid = False
    try:
        chosen_weapon = int(input("Enter your chosen weapon: "))
    except TypeError:
        print("Invalid choice. Please try again.")

def enemy_choose_weapon():
    pass


def resolve_round(player_weapon, enemy_weapon):
    pass


def boss_round(data, level_number):
    global win
    win = False
    print(f"===Your Opponent is....===")
    time.sleep(1)
    print(f">>=={data["bosses"][level_number]}!==<<")
    if level_number == 1:
        print("Here's how to fight the boss!")


def can_fight_boss(data, level_number):
    global cost
    cost = data["prices"]["bosses"][level_number]
    print(f"To fight the boss, you need at least {cost} gold as payment.")
    if data["player"]["gold"] >= cost:
        print("Ok, you can fight the boss!")
        return True
    else:
        print("You can't fight the boss! Grind some more tasks!")
        return None


def pay_boss_cost(data, level_number):
    if can_fight_boss():
        data["player"]["gold"] -= cost
        print(f"You have {data["player"]["gold"]} gold left.")
        print("Now, enter the boss arena!")


def give_boss_reward(data, level_number):
    print(f"For defeating {data["bosses"][level_number]}, you get {data["rewards"][level_number]} gold!")


def rebirth_player(data):
    pass


def level_up(data):
    pass


def check_true_ending(data):
    pass


#printing intro and instructions.
print("====<<<<WELCOME TO TASKMASTER!>>>>====")
print("A project by: Augusto Alfonso Cayabyab, Juan Miguel Rivera, and Gilian Uoiea Janiola!")
print("For starters, this is the whole point of taskmaster: ELIMINATE PROCRASTINATION!")
typing_effect("To use this, follow the given instructions.")
typing_effect("You will see a menu with 7 choices. Preferably, choose the New Profile or New username/password option to give yourself\n"
      "an identity. Now, choose Add a new task. This will aid you in completing tasks for gold. If you want to claim your reward \n"
      "after finishing a task, choose the Mark Task as Completed option. Great. You finished your first task. \n"
      "Now, you can buy items. Choose the Buy Items option. Buy ALL the items you need. Choose the Fight Boss option now.\n"
      "I'll give you instructions on how to fight it when you get there.")
show_menu()