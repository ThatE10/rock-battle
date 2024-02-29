name = "Ethan N"
bot_name = "DESTROYER!"


# Function to determine the bot's move based on the current board state
def bot(board) -> (int, int):
    """
    Determines the bot's move based on the current board state.

    Args:
        board (list): A list representing the number of rocks in each rockpile.

    Returns:
        tuple: A tuple (rockpile_amount, index) representing the number of rocks to remove and the index of the rockpile.
    """
    for index, rockpile_amount in enumerate(board):
        # If the rockpile is not empty, return the number of rocks in the rockpile and its index
        if rockpile_amount//2 != 0:
            print(rockpile_amount//2)
            return index, rockpile_amount//2
