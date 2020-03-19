import random

# models for game pieces, players, ships, board(s)

#Default Ship class

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