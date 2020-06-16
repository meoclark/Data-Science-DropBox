# Implement Alpha-Beta Pruning

"""
Alpha-beta pruning is accomplished by keeping track of two variables for each node — alpha and beta. alpha keeps track of the minimum score the maximizing player can possibly get. It starts at negative infinity and gets updated as that minimum score increases.

On the other hand, beta represents the maximum score the minimizing player can possibly get. It starts at positive infinity and will decrease as that maximum possible score decreases.

For any node, if alpha is greater than or equal to beta, that means that we can stop looking through that node’s children.

To implement this in our code, we’ll have to include two new parameters in our function — alpha and beta. When we first call minimax() we’ll set alpha to negative infinity and beta to positive infinity.

We also want to make sure we pass alpha and beta into our recursive calls. We’re passing these two values down the tree.

Next, we want to check to see if we should reset alpha and beta. In the maximizing case, we want to reset alpha if the newly found best_value is greater than alpha. In the minimizing case, we want to reset beta if best_value is less than beta.

Finally, after resetting alpha and beta, we want to check to see if we can prune. If alpha is greater than or equal to beta, we can break and stop looking through the other potential moves.
"""

from connect_four import *
import random
random.seed(108)

def minimax(input_board, is_maximizing, depth, alpha, beta):
  # Base case - the game is over, so we return the value of the board
  if game_is_over(input_board) or depth == 0:
    return [evaluate_board(input_board), "", alpha, beta]
  best_move = ""
  if is_maximizing == True:
    best_value = -float("Inf")
    symbol = "X"
  else:
    best_value = float("Inf")
    symbol = "O"
  for move in available_moves(input_board):
    new_board = deepcopy(input_board)
    select_space(new_board, move, symbol)
    hypothetical_value = minimax(new_board, not is_maximizing, depth - 1, alpha, beta)[0]
    if is_maximizing == True and hypothetical_value > best_value:
      best_value = hypothetical_value
      best_move = move
      alpha = max(alpha, best_value)
    if is_maximizing == False and hypothetical_value < best_value:
      best_value = hypothetical_value
      best_move = move
      beta = min(beta, best_value)
    if alpha > beta:
      break
  return [best_value, best_move, alpha, beta]
  
print_board(board)  
print(minimax(board, True, 6, -float("Inf"), float("Inf")))


# Review

from connect_four import *

def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
      # Fill in the third parameter for the first player's "intelligence"
      result = minimax(my_board, True, 6, -float("Inf"), float("Inf"))
      print( "X Turn\nX selected ", result[1])
      print(result[1])
      select_space(my_board, result[1], "X")
      print_board(my_board)

      if not game_is_over(my_board):
        #Fill in the third parameter for the second player's "intelligence"
        result = minimax(my_board, False, 6, -float("Inf"), float("Inf"))
        print( "O Turn\nO selected ", result[1])
        print(result[1])
        select_space(my_board, result[1], "O")
        print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")

two_ai_game()