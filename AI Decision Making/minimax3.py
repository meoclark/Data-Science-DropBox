# Deep Copy

from tic_tac_toe import *
from copy import deepcopy

my_board = [
	["1", "2", "X"],
	["4", "5", "6"],
	["7", "8", "9"]
]

new_board = deepcopy(my_board)
select_space(new_board, 5, "O")
print_board(new_board)
print_board(my_board)

# The minimax function

from tic_tac_toe import *
from copy import deepcopy

x_winning = [
	["X", "2", "O"],
	["4", "O", "6"],
	["7", "8", "X"]
]

def game_is_over(board):
  return has_won(board, "X") or has_won(board, "O") or len(available_moves(board)) == 0

def evaluate_board(board):
  if has_won(board, "X"):
    return 1
  elif has_won(board, "O"):
    return -1
  else:
    return 0

def minimax(input_board, is_maximizing):
  # Base case - the game is over, so we return the value of the board
  if game_is_over(input_board):
    return evaluate_board(input_board)
  if is_maximizing == True:
    best_value = -float("Inf")
    symbol = "X"
  else:
    best_value = float("Inf")
    symbol = "O"
  for move in available_moves(input_board):
    print(move)
    new_board = deepcopy(input_board)
    select_space(new_board, move, symbol)
  return new_board
  
print(minimax(x_winning, True))  

