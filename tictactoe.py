"""
Tic Tac Toe Player
"""

import math

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
    count_x = sum(1 for i in range(3) for j in range(3) if board[i][j] == X)
    count_o = sum(1 for i in range(3) for j in range(3) if board[i][j] == O)
    return X if count_x == count_o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if i not in range(3) or j not in range(3):
        raise ValueError("Action out of bounds")
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid action: cell is not empty")
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for i in range(3):
        if board[i][0] is not EMPTY and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    # Check columns
    for j in range(3):
        if board[0][j] is not EMPTY and board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]
    # Diagonals
    if board[0][0] is not EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] is not EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    # If any empty cell exists, not terminal
    return all(board[i][j] is not EMPTY for i in range(3) for j in range(3))


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    if w == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action (i, j) for the current player on the board.
    Uses alpha-beta pruning for efficiency. Returns None if board is terminal.
    """

    if terminal(board):
        return None

    current = player(board)

    # Deterministic action ordering for reproducible behavior:
    possible_actions = sorted(actions(board))

    def max_value(b, alpha, beta):
        if terminal(b):
            return utility(b)
        v = -math.inf
        for a in sorted(actions(b)):
            v = max(v, min_value(result(b, a), alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(b, alpha, beta):
        if terminal(b):
            return utility(b)
        v = math.inf
        for a in sorted(actions(b)):
            v = min(v, max_value(result(b, a), alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    best_action = None
    if current == X:
        best_val = -math.inf
        alpha = -math.inf
        beta = math.inf
        for action in possible_actions:
            v = min_value(result(board, action), alpha, beta)
            if v > best_val:
                best_val = v
                best_action = action
            alpha = max(alpha, best_val)
            if alpha >= beta:
                break
    else:
        best_val = math.inf
        alpha = -math.inf
        beta = math.inf
        for action in possible_actions:
            v = max_value(result(board, action), alpha, beta)
            if v < best_val:
                best_val = v
                best_action = action
            beta = min(beta, best_val)
            if alpha >= beta:
                break

    return best_action

