import chess
import os
from random import sample

PIECE_WEIGHTS = {
  None: 0,
  chess.PAWN: 100,
  chess.ROOK: 500,
  chess.KNIGHT: 320,
  chess.BISHOP: 330,
  chess.QUEEN: 900,
  chess.KING: 20000
}

def whose_turn():
  print("White's turn\n") if board.turn == chess.WHITE else print("Black's turn\n")

def move(movement):
  board.push(movement) if movement in board.legal_moves else None

def evaluate(board):
  top_value = 0
  for movement in board.legal_moves:
    weight = PIECE_WEIGHTS[board.piece_type_at(movement.from_square)]
    if weight > top_value:
      top_value = weight
  return top_value

def minimax_root(board, depth, maximizing_player):
  best_move = None
  best_value = alpha = -float('inf')
  beta = float('inf')

  for movement in board.legal_moves:
    move(movement)
    value = max(best_value, minimax(board, alpha, beta, depth - 1, not maximizing_player))
    board.pop()
    if value > best_value:
      best_move = movement
      best_value = value
  return best_move

def minimax(board, alpha, beta, depth, maximizing_player):
  if depth == 0 or board.is_game_over():
    return evaluate(board)
  if maximizing_player:
    value = alpha
    for movement in board.legal_moves:
      move(movement)
      value = max(value, minimax(board, alpha, beta, depth - 1, False))
      board.pop()
      alpha = max(alpha, value)
      if beta <= alpha:
        return value
    return value
  else:
    value = beta
    for movement in board.legal_moves:
      move(movement)
      value = min(value, minimax(board, alpha, beta, depth - 1, True))
      board.pop()
      beta = min(beta, value)
      if beta <= alpha:
        return value
    return value

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
    # position = sample(list(board.legal_moves), 1)[0]
    position = minimax_root(board, 5, True)
    move(position)
