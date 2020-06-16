from tic_tac_toe import *

start_board = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"]
]

x_won = [
	["X", "O", "3"],
	["4", "X", "O"],
	["7", "8", "X"]
]

o_won = [
	["O", "X", "3"],
	["O", "X", "X"],
	["O", "8", "9"]
]

tie = [
	["X", "X", "O"],
	["O", "O", "X"],
	["X", "O", "X"]
]

def game_is_over(board):
  return has_won(board, "X") or has_won(board, "O") or len(available_moves(board)) == 0

print(game_is_over(start_board))
print(game_is_over(x_won))
print(game_is_over(o_won))
print(game_is_over(tie))

def evaluate_board(board):
  if has_won(board, "X"):
    return 1
  elif has_won(board, "O"):
    return -1
  else:
    return 0
  
if (game_is_over(start_board)):
  print(evaluate_board(start_board))
if (game_is_over(x_won)):
  print(evaluate_board(x_won))
if (game_is_over(o_won)):
  print(evaluate_board(o_won))
if (game_is_over(tie)):
  print(evaluate_board(tie))