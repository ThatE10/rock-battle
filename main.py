import game
import bots.bot_1
import bots.bot_2

battle = game.game(starting_state=[0, 5, 5, 4,3])

while not battle.gameover:
    print("Turn 0")
    battle.play(bots.bot_1.bot(battle.board))

    if not battle.gameover:
        print("Turn 1")
        battle.play(bots.bot_2.bot(battle.board))

    print(battle.board)
