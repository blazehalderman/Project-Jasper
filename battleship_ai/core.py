from .models import(ShipClass, PlayerClass, BattleshipGameClass)

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

def read_board_file(file):
    with open(file) as f:
        board_array = f.readlines()
    f.closed
    return (board_array)

board_array = read_board_file("board.txt")

# gets player name

# player_name = input("Welcome to Battleship! Please enter your name: ")

# initialize player
# active_player = PlayerClass(player_name, )
