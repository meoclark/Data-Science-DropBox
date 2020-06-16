# minimax algorithm

"""
The minimax algorithm is a decision-making algorithm that is used for finding the best move in a two player game. 
It’s a recursive algorithm — it calls itself. In order for us to determine if making move A is a good idea, 
we need to think about what our opponent would do if we made that move.
"""

from tic_tac_toe import *

my_board = [
	["1", "2", "X"],
	["4", "5", "6"],
	["7", "8", "9"]
]

print_board(my_board)

select_space(my_board, 5, "O")
print_board(my_board)

select_space(my_board, 1, "X")
select_space(my_board, 2, "X")
print(available_moves(my_board))

print(has_won(my_board, "X"))
print(has_won(my_board, "O"))
print_board(my_board)

