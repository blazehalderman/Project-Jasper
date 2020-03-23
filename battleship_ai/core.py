from .models import(BoardClass, ShipClass, PlayerClass, BattleshipGameClass)

# core game function (read, write, storing contents)

# initialize variables

player_list = []

# gets player name
current_session = BattleshipGameClass(player_list)

current_session.game_start()
