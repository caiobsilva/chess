import chess
import os
from random import sample

def whose_turn():
  print("White's turn\n") if board.turn == chess.WHITE else print("Black's turn\n")

def move(movement):
  board.push(movement) if movement in board.legal_moves else None

board = chess.Board()

while not board.is_game_over():
  os.system('cls' if os.name == 'nt' else 'clear')
  whose_turn()
  print(board)
  if board.turn == chess.WHITE:
    pos = input("\nMake a move!\n")
    position = chess.Move.from_uci(pos)
    move(position)
  else:
    position = sample(list(board.legal_moves), 1)[0]
    move(position)
