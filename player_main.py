import game
import bots.bot_1
import bots.bot_2

battle = game.game(starting_state=[0, 5, 5, 4,3])

while not battle.gameover:
    print("Turn 0")
    print(battle.board)
    play_1 = bots.bot_2.bot(battle.board,turn=0)
    battle.play(play_1)

    if not battle.gameover:
        print("Turn 1")
        print(battle.board)
        play_2 = bots.bot_2.bot(battle.board,turn=1)
        battle.play(play_2)


