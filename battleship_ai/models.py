import random

# models for game pieces, players, ships, board(s)

#Piece class

class PieceClass:
    def __init__(self, char, rowX, colY):
        self.char = char
        self.rowX = rowX
        self.colY = colY

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
        row_count = 0
        for row in range(len(self.board_data)):
            for col in range(len(self.board_data[row])):
                # if a | run data function for gathering points
                if(self.board_data[row][col:col+3] == '| |'):
                    
                    new_piece = PieceClass(self.board_data[row][col+1], row, col+1)
                    stored_pieces.append(new_piece)
        print(row_count)
        for i in stored_pieces:
            print('char: "' + str(i.char) + '" ' + str(i.rowX) + ' ' + str(i.colY))

#Ship class
class ShipClass:
    def __init__(self, ship_length, ship_type):
        self.ship_length = ship_length
        self.ship_type = ship_type
        
#Player class
class PlayerClass:
    def __init__(self, name, default_ship_list):
        self.name = name
        #self.board = board
        self.default_ship_list = default_ship_list
    
    # Player methods

# Battleship game class
class BattleshipGameClass:
    # define players array
    def __init__(self, player_list, active_player):
        self.player_list = player_list
        self.active_player = active_player
    
    def game_start(self):
        print("game is starting!")
    
    def game_end(self):
        print("game has ended!")

    def game_end_turn(self):
        print("turn has ended")

    def game_set_winner(self):
        print("winner is " + self.active_player.name)
        return