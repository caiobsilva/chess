import chess
from random import sample

class Player():
  PIECE_WEIGHTS = {
    None: 0,
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
  }
  RANDOM = 0
  MINIMAX = 1

  def __init__(self, color, is_bot, strategy=None) -> None:
    self.color = color
    self.is_bot = is_bot
    self.strategy = strategy

  def move(self, board, position=None) -> chess.Move:
    if not self.is_bot:
      return chess.Move.from_uci(position)
    elif self.strategy == Player.RANDOM:
      return sample(list(board.legal_moves), 1)[0]
    elif self.strategy == Player.MINIMAX:
      return self.minimax_root(board, 4, True)
    pass

  def minimax_root(self, board, depth, maximizing_player) -> chess.Move:
    best_move = None
    best_value = alpha = -float('inf')
    beta = float('inf')

    for movement in board.legal_moves:
      board.push(movement)
      value = max(best_value, self.minimax(board, alpha, beta, depth - 1, not maximizing_player))
      board.pop()
      if value > best_value:
        best_move = movement
        best_value = value
    return best_move

  def minimax(self, board, alpha, beta, depth, maximizing_player) -> int:
    if depth == 0 or board.is_game_over():
      return self.evaluate(board)
    if maximizing_player:
      value = alpha
      for movement in board.legal_moves:
        board.push(movement)
        value = max(value, self.minimax(board, alpha, beta, depth - 1, False))
        board.pop()
        alpha = max(alpha, value)
        if beta <= alpha:
          return value
      return value
    else:
      value = beta
      for movement in board.legal_moves:
        board.push(movement)
        value = min(value, self.minimax(board, alpha, beta, depth - 1, True))
        board.pop()
        beta = min(beta, value)
        if beta <= alpha:
          return value
      return value

  def evaluate(self, board) -> int:
    whites = blacks = 0
    for square in chess.SQUARES:
      piece = board.piece_at(square)
      if not piece:
        continue
      if piece.color == chess.WHITE:
        whites += Player.PIECE_WEIGHTS[piece.piece_type]
      else:
        blacks += Player.PIECE_WEIGHTS[piece.piece_type]
    # print(whites - blacks)
    return whites - blacks
