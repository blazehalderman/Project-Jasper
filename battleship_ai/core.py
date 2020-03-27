from .models import(BoardClass, ShipClass, PlayerClass, BattleshipGameClass)

# core game function (read, write, storing contents)

# initialize variables

# gets player name
current_session = BattleshipGameClass()
player = current_session.game_start()
current_session.game_run(player)
