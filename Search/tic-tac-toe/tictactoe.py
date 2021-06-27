"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    number_x = 0
    number_o = 0

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == X:
                number_x += 1
            elif board[i][j] == O:
                number_o += 1

    if number_x > number_o:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_cells = []
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                available_cells.append([i,j])
    return available_cells


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    print(board)
    print(action)
    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)
    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[2][0] == board[1][1] == board[0][2]:
        return board[2][0]
    else:
        return None

def terminal(board):

    has_empty_cells = False
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                has_empty_cells = True

    return not(has_empty_cells) or winner(board)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move



def max_value(board):
    if terminal(board):
        return utility(board), None
    v = float('-inf')
    m = None
    for action in actions(board):
        value, move = min_value(result(board, action))
        if value > v:
            v = value
            m = action
            if v == 1:
                return v, m
    return v, m

def min_value(board):
    if terminal(board):
        return utility(board), None
    v = float('inf')
    m = None
    for action in actions(board):
        value, move = max_value(result(board, action))
        if value < v:
            v = value
            m = action
            if v == -1:
                return v, m
    return v, m