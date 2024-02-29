import game
import bots.bot_1
import bots.bot_2

battle = game.game(starting_state=[0, 5, 5, 4,3])

while not battle.gameover:
    print("Turn 0")
    play_1 = bots.bot_2.bot(battle.board)
    battle.play(play_1)

    if not battle.gameover:
        print("Turn 1")
        play_2 = bots.bot_2.bot(battle.board)
        battle.play(play_2)

    print(battle.board)
