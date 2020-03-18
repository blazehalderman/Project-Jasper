import random

# models for game pieces, players, ships, board(s)

#Player class
class PlayerClass:
    def __init__(self, name):
        self.name = name

# Battleship game class
class BattleshipGameClass:
    # define players array
    def __init__(self, players, activeplayer):
        self.players = players
        self.activeplayer = activeplayer
    
    def game_start(self):
        print("game is starting!")
    
    def game_end(self):
        print("game has ended!")

    def game_end_turn(self):
        print("turn has ended")

    def game_set_winner(self):
        print("winner is " + self.activeplayer.name)
        return