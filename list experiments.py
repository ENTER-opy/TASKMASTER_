import json
import random
import time
print("WELCOME TO TASMKMASTER!")
print("A project by: Augusto Alfonso Cayabyab, Juan Miguel Rivera, and Gilian Uoiea Janiola!")
print("For starters, this is the whole point of taskmaster: ELIMINATE PROCRASTINATION!")
print("To use this, follow the given instructions.")
print("You will see a menu with 7 choices. Preferably, choose the New Profile or New username/password option to give yourself\n"
      "an identity. Now, choose Add Task. This will aid you in completing tasks for gold. If you want to claim your reward \n"
      "after finishing a task, choose the Mark Task as Completed option. Great. You finished your first task. \n"
      "Now, you can buy items. Choose the Buy Items option. ")
def load_game():
    global data
    with open("player.json", "r") as f:
        data = json.load(f)

def save_game(data):
    with open("players.json", "w") as f:
        json.dump(data, f, indent=4)

def reset_game():
    with open("players.json", "r") as f:
        data = json.load(f)


def create_player(username, password):

    done = False
    while not done:
        data[0]["player"]["username"] = input("Enter your preferred Hero Title: ")
        passlogin = input("Enter your Hero's Code (password): ")

def sign_in():
    done = False
    while not done:
        userlogin = input("Enter your Hero Title: ")
        passlogin = input("Enter your Hero's Code (password): ")
        if userlogin == data[0]["player"] and passlogin == data[0]["player"]["password"]:
            done = True

def show_menu():
    print("1. New Password/ New Username\n"
          "2. Save/Exit Game\n"
          "3. View stats\n"
          "4. Add a new task to task list\n"
          "5. Mark task as completed\n"
          "6. Fight Boss\n"
          "7. New Profile(reset stats)\n"
          "8. Buy Items")
    choice = int(input("Enter your choice: "))
    return choice


def view_stats(data):
    for player in data["player"]:
        print(player["username"])
        for i in player["tasks_to_do"]:
            print(f"{i+1}: {player["tasks_to_do"][i]}")
        print(player["tasks_done"])


def add_task(data):
    name = input("Enter Task Name:")
    json.update("tasks_to_do"):name)
    with open("players.json", "w") as f:
        json.dump(data, f, indent=4)



def complete_task(data):
    pass


def choose_weapon():
    pass


def enemy_choose_weapon():
    pass


def resolve_round(player_weapon, enemy_weapon):
    pass


def boss_round():
    pass


def boss_battle(data, level_number):
    pass


def can_fight_boss(data, level_number):
    pass


def pay_boss_cost(data, level_number):
    pass


def give_boss_reward(data, level_number):
    pass


def rebirth_player(data):
    pass


def level_up(data):
    pass


def check_true_ending(data):
    pass


def game_loop():
    pass





