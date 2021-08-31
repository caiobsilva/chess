import chess
import os

class Game():
  UNICODE_WHITE = {
    chess.PAWN: "\u2659",
    chess.ROOK: "\u2656",
    chess.KNIGHT: "\u2658",
    chess.BISHOP: "\u2657",
    chess.QUEEN: "\u2655",
    chess.KING: "\u2654"
  }

  UNICODE_BLACK = {
    chess.PAWN: "\u265F",
    chess.ROOK: "\u265C",
    chess.KNIGHT: "\u265E",
    chess.BISHOP: "\u265D",
    chess.QUEEN: "\u265B",
    chess.KING: "\u265A"
  }

  def __init__(self) -> None:
    self.board = chess.Board()

  def __str__(self) -> str:
    self.clear_stdout()
    return self.formatted_player_turn() + self.unicode_formatted_board()

  def move(self, movement) -> None:
    self.board.push(movement) if movement in self.board.legal_moves else None

  def is_player_turn(self) -> bool:
    return self.board.turn == chess.WHITE

  def formatted_player_turn(self) -> str:
    return "White's turn\n" if self.board.turn == chess.WHITE else "Black's turn\n"

  def unicode_formatted_board(self) -> str:
    pieces = []
    for square in chess.SQUARES:
      piece = self.board.piece_at(square)
      if not piece:
        pieces.append(".")
      elif piece.color == chess.WHITE:
        pieces.append(Game.UNICODE_WHITE[piece.piece_type])
      else:
        pieces.append(Game.UNICODE_BLACK[piece.piece_type])
    table = "\n".join([" ".join(pieces[i:i+8]) for i in range(0, len(pieces), 8)])
    return table

  def clear_stdout(self) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
