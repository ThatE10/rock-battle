class game():
    def __init__(self, starting_state=[]):
        self.gameover = False
        self.turn = 0
        self.round = 0
        self.board = []
        if starting_state == []:
            pass
        else:
            self.board = starting_state

    def play(self, play):
        rockpile_num, amount = play

        if rockpile_num >= len(self.board):
            pass  # throw error

        if self.board[rockpile_num] < amount:
            pass  # throw different error

        self.board[rockpile_num] -= amount

        if all(rockpile == 0 for rockpile in self.board):
            self.gameover = True
            print(f"Game over Player[{self.turn}] wins!")
        self.round += 1
        self.turn = 0 if self.turn else 1


def player(board) -> (int, int):
    awaiting_valid_response = True
    while awaiting_valid_response:
        # Prints graphics
        print("Your turn!")
        for index, rockpile_amt in enumerate(board):
            print(f"[{index}]: {"#" * rockpile_amt}")
            print()

        try:
            play = input("Please type your next move: ")
            rockpile, amount = [int(a) for a in play.split()]

            if rockpile >= len(board):
                raise ValueError("Invalid rockpile number. Please choose a valid rockpile.")

            if board[rockpile] < amount:
                raise ValueError("Not enough rocks in the chosen rockpile.")

            return (rockpile, amount)

        except ValueError as ve:
            if "unpack" in str(ve):
                print("First value index, second value amount")
            else:
                print(ve)

        except IndexError:
            print("Index out of range. Please provide a valid input.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

