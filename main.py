import player
import game

match = game.Game()
plr = player.Player(0, False)
bot = player.Player(1, True, player.Player.MINIMAX)

while not match.board.is_game_over():
  print(match)
  # print(board)
  if match.is_player_turn():
    pos = input("\nInsert position\n")
    position = plr.move(match.board, pos)
    match.move(position)
  else:
    position = bot.move(match.board)
    match.move(position)
