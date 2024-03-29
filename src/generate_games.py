import time
import numpy as np
import copy
from utils import TerminalText as tt
from referee import getGameState
import constants

def reduceDimensions(matrix):
    """
    Decrease any list/matrix dimensions by one.

    Parameters
    ----------
    matrix: Multidimensional Array

    Returns
    -------
    list: The matrix after reducing it's dimensions.
    """
    # Doesn't accept vectors/(1-dimensional matrices)
    # If matrix is a vector return it without changes
    if (type(matrix[0]) is not list): return matrix
    new_matrix = []
    for item in matrix:
        new_matrix += item
    return new_matrix

def playLevelDeeper(prev_boards, n, p_type):
    size = pow(n, 2)
    current_boards = []
    for prev_board in prev_boards:
        for i in range(size):
            current_board = copy.deepcopy(prev_board)
            if current_board[i] != constants.EMPTY_CELL: continue
            current_board[i] = p_type
            if getGameState(np.reshape(current_board, (-1, n))) == constants.GAME_INCOMPLETE:
                # Prevent duplicates
                isUnique = True
                for board in current_boards:
                    if (board == current_board).all():
                        isUnique = False
                if isUnique:
                    current_boards.append(current_board)
    return current_boards

def generateGames(N):
    """
    Generates all possible valid uncompleted Tic Tac Toe games on an NxN board.

    Parameters
    ----------
    N (Int): Number of rows/columns in board

    Returns
    -------
    list: All possible valid uncompleted games.
    """

    start_time = time.time() # To measure script running time

    NxN = pow(N, 2)

    base_board = [[np.full(NxN, constants.EMPTY_CELL, np.uint8)]]
    boards = base_board + ([[]] * (NxN)) # Generated boards will be put here

    print(tt.BLUE + "Generating Games..." + tt.END)
    print("") # To prevent the code in the loop from erasing the "Board Size" line

    for i in range(NxN - 1):
        percentage = "%.2f" % (((i + 2) / NxN) * 100) # Limit to two decimal points
        print(tt.ERASE + tt.BLUE + "Brute Force Generating All Games: " + tt.END + f"{percentage}%")
        boards[i + 1] = playLevelDeeper(boards[i], N, (i % 2) + 1)
    
    games = reduceDimensions(boards)
    M = len(games)

    total_time = time.time() - start_time

    print(tt.BLUE + "Generated " + tt.END + f"{M}" + tt.BLUE + " games in" + tt.END
        + f" {'%.2f' % total_time} " + tt.BLUE + "seconds." + tt.END)

    return games