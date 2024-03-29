import time
import numpy as np
from utils import TerminalText as tt
from min_max_player import predictBestNextMove
import constants

def generateLabels(N, games):
    """
    Compute labels (best moves) for the games

    Parameters
    ----------
    N (Int): Number of rows/columns in board
    games: List

    Returns
    -------
    list: Labels for the games.
    """

    start_time = time.time() # To measure script running time

    M = len(games)

    labels = np.full((M, pow(N, 2)), constants.EMPTY_CELL, np.uint8)
    print(tt.BLUE + "Generating Labels..." + tt.END)
    print("") # To prevent the code in the loop from erasing the "Board Size" line

    for i, game in enumerate(games):
        percentage = "%.2f" % (((i + 1) / M) * 100) # Limit to two decimal points
        print(tt.ERASE + tt.BLUE + "MiniMax Predicting Best Moves: " + tt.END + f"{percentage}%")
        labels[i, predictBestNextMove(game, N)] = 1

    total_time = time.time() - start_time

    print(tt.BLUE + "Generated labels" + tt.BOLD + " (best moves) " + tt.END
        + tt.BLUE + "for " + tt.END + f"{M}" + tt.BLUE + " games in" + tt.END
        + f" {'%.2f' % total_time} " + tt.BLUE + "seconds." + tt.END)

    return labels