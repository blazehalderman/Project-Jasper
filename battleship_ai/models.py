import random

# models for game pieces, players, ships, board(s)

#Piece class

class PieceClass:
    def __init__(self, char, rowX, colY, num_colY):
        self.char = char
        self.rowX = rowX
        self.colY = colY
        self.act_rowX = chr(ord('@') + (rowX//2))
        self.act_colY = num_colY

#Board class
class BoardClass:
    def __init__(self, file):
        self.file = file
        self.board_data = []
        self.board_pieces = []

    def read_board_file(self):
        with open(self.file) as f:
            for line in f:
                for i in line.strip().split('\n'):
                    self.board_data.append(i)
        f.closed
    
    def clean_board_file(self):
        stored_pieces = []
        for row in range(len(self.board_data)):
            num_colY = 0
            for col in range(len(self.board_data[row])):
                # if a | run data function for gathering points
                if(self.board_data[row][col:col+3] == '| |'):
                    num_colY+=1
                    new_piece = PieceClass(self.board_data[row][col+1], row, col+1, num_colY)
                    stored_pieces.append(new_piece)
    
        for i in stored_pieces:
            print(str(i.act_rowX) + ' ' + str(i.act_colY))

#Ship class
class ShipClass:
    def __init__(self, ship_length, ship_type):
        self.ship_length = ship_length
        self.ship_type = ship_type
        self.ship_store_cordX = 0
        self.ship_store_cordY = 0
        
#Player class
class PlayerClass:
    def __init__(self, name, board, default_ship_list):
        self.name = name
        self.board = board
        self.default_ship_list = default_ship_list
    
    # Player methods

# Battleship game class
class BattleshipGameClass:
    # define players array
    def __init__(self, player_list):
        self.player_list = player_list
    
    # game actions
    def game_start(self):
        player_name = input("Welcome to Battleship! Please enter your name: ")
        player_board = input("Please enter the Battleship map you wish to play(must follow specific formats in board.txt): ")
        
        #initalizing board, player, default ships
        board_file = BoardClass(player_board)
        board_file.read_board_file()
        board_file.clean_board_file()
        
        ship_carrier = ShipClass(5, "Aircraft Carrier")
        ship_battle = ShipClass(4, "Battleship")
        ship_destroyer = ShipClass(3, "Destroyer")
        ship_submarine = ShipClass(3, "Submarine")
        ship_patrol = ShipClass(2, "Patrol Boat")

        default_ship_array = []

        default_ship_array.append(ship_carrier)
        default_ship_array.append(ship_battle)
        default_ship_array.append(ship_destroyer)
        default_ship_array.append(ship_submarine)
        default_ship_array.append(ship_patrol)
        
        # store all information into active player
        active_player = PlayerClass(player_name, board_file, default_ship_array)
        
        #list boats size stored and types
        for i in active_player.default_ship_list:
            print(i.ship_length)
            print(i.ship_type)

    def game_end(self):
        print("game has ended!")

    def game_end_turn(self):
        print("turn has ended")

    def game_set_winner(self):
        print("winner is " + self.active_player.name)
        return