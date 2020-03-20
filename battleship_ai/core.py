from .models import(BoardClass, ShipClass, PlayerClass, BattleshipGameClass)

# core game function (read, write, storing contents)

#create ship types

ship_carrier = ShipClass(5, "Aircraft Carrier")
ship_battle = ShipClass(4, "Battleship")
ship_destroyer = ShipClass(3, "Destroyer")
ship_submarine = ShipClass(3, "Submarine")
ship_patrol = ShipClass(2, "Patrol Boat")

default_ship_array = [5]

default_ship_array.append(ship_carrier)
default_ship_array.append(ship_battle)
default_ship_array.append(ship_destroyer)
default_ship_array.append(ship_submarine)
default_ship_array.append(ship_patrol)

# initialize board

player_board = BoardClass("board.txt")
player_board.read_board_file(player_board.file)

enemy_board = BoardClass("board.txt")
enemy_board.read_board_file(enemy_board.file)

player_board.clean_board_file(player_board.board_data)

# gets player name

# player_name = input("Welcome to Battleship! Please enter your name: ")

# initialize player
# active_player = PlayerClass(player_name, )
