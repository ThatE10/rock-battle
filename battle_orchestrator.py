import os
from itertools import combinations

import importlib.util

import game


def call_play_function(file_name):
    # Construct the module name
    module_name = file_name[:-3]  # Remove the ".py" extension
    # Load the module
    spec = importlib.util.spec_from_file_location(module_name, file_name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Check if the "play" function exists in the module
    if hasattr(module, "bot"):
        # Call the "play" function
        return module.bot



folder_path = "./bots"
bot_list  = []
if not os.path.exists(folder_path):
    print(f"The folder '{folder_path}' does not exist.")
else:
        # Iterate through all files in the folder
    for file_name in os.listdir(folder_path):
        # Get the full path of the file
        file_path = os.path.join(folder_path, file_name)

        # Check if the current item is a file (not a directory)
        if os.path.isfile(file_path):
            bot_list.append(file_name)

battle_schedule = combinations(bot_list, 2)

print(call_play_function("./bots/bot_1.py")([1,2,3],turn=1))

for match in battle_schedule:
    file_path = "./bots/"+battle[0]
    player_0 = call_play_function(file_path)

    file_path = "./bots/" + battle[1]
    player_1 = call_play_function(file_path)

    print(match)

    battle = game.game(starting_state=[0, 5, 5, 4, 3])

    while not battle.gameover:
        print("Turn 0")
        print(battle.board)
        play_0 = player_0(battle.board, turn=0)
        battle.play(play_0)

        if not battle.gameover:
            print("Turn 1")
            print(battle.board)
            play_1 = player_1(battle.board, turn=1)
            battle.play(play_1)
